# Rendering Spatial Audio from Bluetooth headphones

**Framework**: Audio Toolbox

Create a Spatial Audio extension that allows Bluetooth headphones to track the wearer’s head movements for spatial audio playback.

#### Overview

To integrate a Bluetooth headphone into the Spatial Audio routing system, implement an audio extension called an *audio unit*. The system adds the audio unit to the audio signal chain when someone is listening to audio on the headphones and Spatial Audio is active. When the listener disables Spatial Audio or connects to a different audio device, the system removes your audio unit.

You deliver this renderer by subclassing [`AUHeadTrackingBinauralRenderer`](auheadtrackingbinauralrenderer.md), which is itself a subclass of [`AUAudioUnit`](auaudiounit.md). Package your subclass as a Spatial Audio App Extension; see [`Creating an audio unit extension`](https://developer.apple.com/documentation/avfaudio/creating-an-audio-unit-extension) for an example of creating an audio app extension. Your extension runs in a process encapsulated by the system for security and performance. In addition to the audio unit, publish your headphone’s head-tracking capabilities using [`AudioAccessoryKit`](https://developer.apple.com/documentation/audioaccessorykit) so the system can match your device to the correct renderer.

The system exclusively controls spatialization state through three KVO properties your audio unit subclass observes: [`deviceUID`](auheadtrackingbinauralrenderer/deviceuid.md) identifies the paired device and, together with `AUHeadTrackingBinauralRenderer/headTrackingIsEnabled`, signals when your renderer begins data retrieval; `AUHeadTrackingBinauralRenderer/isBypassed` is the system’s safety valve, signaling when it removes your audio unit from the signal chain.

> ❗ **Important**: You can develop and test an app that uses `AUHeadTrackingBinauralRenderer` on devices in any region. The class currently builds only for development or Ad Hoc testing. The class will support App Store submission and alternative distribution at a later time. Customer installations of your app can use the framework only on devices located in the EU that are signed in with an Apple Account with an EU country or region.

#### Deliver the Audio Unit

Subclassing [`AUHeadTrackingBinauralRenderer`](auheadtrackingbinauralrenderer.md) is your entry point into the Spatial Audio routing system. The system identifies your audio unit using the [`AudioComponentDescription`](audiocomponentdescription.md) type, which requires the component type [`kAudioUnitType_HeadTrackingBinauralRenderer`](kaudiounittype_headtrackingbinauralrenderer.md), the four-character code `'auht'`.

Declare your audio unit in your App Extension’s `Info.plist` under the `AudioComponents` key. Include the type, a four-character subtype unique to your audio unit, a four-character manufacturer code, a display name, and a version number:

```xml
<key>AudioComponents</key>
<array>
    <dict>
        <key>type</key>
        <string>auht</string>
        <key>subtype</key>
        <string>abcd</string>
        <key>manufacturer</key>
        <string>Mfgr</string>
        <key>name</key>
        <string>AcmeCorp: Spatial Renderer</string>
        <key>version</key>
        <integer>1</integer>
    </dict>
</array>
```

The App Extension’s principal class must conform to [`AUAudioUnitFactory`](auaudiounitfactory.md) and implement [`createAudioUnit(with:)`](auaudiounitfactory/createaudiounit(with:).md) to return an instance of your subclass:

```swift
final class MyAudioUnitFactory: NSObject, AUAudioUnitFactory {
    func createAudioUnit(
        with desc: AudioComponentDescription
    ) throws -> AUAudioUnit {
        return try MyBinauralRenderer(componentDescription: desc)
    }
}
```

#### Observe Head Tracking State

Respond when a listener turns head tracking on or off by observing the `AUHeadTrackingBinauralRenderer/headTrackingIsEnabled` property. The system sets this KVO-compliant property; you don’t have to set it yourself.

Set up your observation in your subclass initializer or in [`allocateRenderResources()`](auaudiounit/allocaterenderresources().md), and store the returned token so the observation stays active:

```swift
var headTrackingObservation: NSKeyValueObservation?

headTrackingObservation = observe(
    \.headTrackingIsEnabled,
    options: [.new]
) { [weak self] _, change in
    guard let self, let enabled = change.newValue else { return }
    if enabled {
        self.startHeadTracking()
    } else {
        self.stopHeadTracking()
    }
}
```

#### Retrieve Head Tracking Data

To identify the Bluetooth headphone currently matched to your audio unit observe the [`deviceUID`](auheadtrackingbinauralrenderer/deviceuid.md) property. The system sets this KVO-compliant property lets you know when to begin or stop retrieving head tracking data; you don’t have to set it yourself.

The value is a `String?` containing a 32-bit unsigned integer in decimal notation, not a UUID, the same value used by [`AudioAccessoryKit`](https://developer.apple.com/documentation/audioaccessorykit). Don’t store this value; it isn’t a UUID, despite being a string. When the property becomes non-`nil`, use the value to request head orientation data from `AudioAccessoryKit`. When the property becomes `nil`, stop any active data retrieval and release associated resources.

Wait until both [`deviceUID`](auheadtrackingbinauralrenderer/deviceuid.md) is non-`nil` and `AUHeadTrackingBinauralRenderer/headTrackingIsEnabled` is `true` before starting data retrieval:

```swift
var deviceUIDObservation: NSKeyValueObservation?

deviceUIDObservation = observe(
    \.deviceUID,
    options: [.new]
) { [weak self] _, change in
    // Begin retrieval only when `headTrackingIsEnabled` is also `true`.
    guard let self else { return }
    if let uid = change.newValue.flatMap({ $0 }) {
        self.beginRetrievingHeadData(deviceUID: uid)
    } else {
        self.stopRetrievingHeadData()
    }
}
```

#### Handle Bypass

If your Audio Unit exceeds its power budget or causes audio dropouts, the system sets `AUHeadTrackingBinauralRenderer/isBypassed` to `true` to remove your Audio Unit from the signal chain.

Observe the property and respond gracefully when the system bypasses your audio unit. Release compute-intensive resources, stop head-tracking data retrieval, and reset your renderer state. When ``AUHeadTrackingBinauralRenderer/isBypassed`returns to`false`, restore your rendering resources and resume normal operation, as shown below.

```swift
var bypassObservation: NSKeyValueObservation?

bypassObservation = observe(
    \.isBypassed,
    options: [.new]
) { [weak self] _, change in
    // `isBypassed` can be set from any thread; synchronize access
    // to shared rendering state appropriately.
    guard let self, let bypassed = change.newValue else { return }
    if bypassed {
        self.stopRetrievingHeadData()
        self.releaseRenderResources()
    } else {
        self.restoreRenderResources()
    }
}
```

> ❗ **Important**: The system can set `AUHeadTrackingBinauralRenderer/isBypassed` from any thread. Keep your observer implementation thread-safe.

## See Also

- [Creating an audio unit extension](../avfaudio/creating-an-audio-unit-extension.md)
  Build an extension by using an Xcode template.
- [Creating custom audio effects](../avfaudio/creating-custom-audio-effects.md)
  Add custom audio-effect processing to apps like Logic Pro X and GarageBand by creating Audio Unit (AU) plug-ins.
- [Incorporating Audio Effects and Instruments](incorporating-audio-effects-and-instruments.md)
  Add custom audio processing and MIDI instruments to your app by hosting Audio Unit (AU) plug-ins.
- [Debugging Out-of-Process Audio Units on Apple Silicon](debugging-out-of-process-audio-units-on-apple-silicon.md)
  Connect to out-of-process audio units using the Xcode debugger.
- [class AUAudioUnit](auaudiounit.md)
  A class that defines a host’s interface to an audio unit.
- [class AUAudioUnitBus](auaudiounitbus.md)
  A class that defines an input or output connection point on an audio unit.
- [class AUAudioUnitBusArray](auaudiounitbusarray.md)
  A class that defines a container for an audio unit’s input or output busses.
- [class AUAudioUnitPreset](auaudiounitpreset.md)
  A class that describes an interface for custom parameter settings provided by the audio unit developer.
- [class AUAudioUnitV2Bridge](auaudiounitv2bridge.md)
  A class that wraps a version 2 audio unit as version 3 audio unit.
- [class AUHeadTrackingBinauralRenderer](auheadtrackingbinauralrenderer.md)
  A subclass of AUAudioUnit specifically for 3rd party spatial Audio Units.
- [func AudioUnitExtensionCopyComponentList(CFString) -> Unmanaged<CFArray>?](audiounitextensioncopycomponentlist(_:).md)
  Returns the component registrations for a given audio unit extension.
- [func AudioUnitExtensionSetComponentList(CFString, CFArray?) -> OSStatus](audiounitextensionsetcomponentlist(_:_:).md)
  Allows the implementor of an audio unit extension to dynamically modify the list of component registrations for the extension.
- [protocol AUAudioUnitFactory](auaudiounitfactory.md)
  An object that creates a version 3 audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/rendering-spatial-audio-from-bluetooth-headphones)*