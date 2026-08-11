# AUHeadTrackingBinauralRenderer

**Framework**: Audio Toolbox  
**Kind**: class

A subclass of AUAudioUnit specifically for 3rd party spatial Audio Units.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class AUHeadTrackingBinauralRenderer
```

## Mentions

- [Rendering Spatial Audio from Bluetooth headphones](rendering-spatial-audio-from-bluetooth-headphones.md)

#### Overview

This class adds spatial-audio-specific head tracking properties beyond the standard AUAudioUnit interface.

When the user selects matching Bluetooth headphones for the current audio route and the system has a 3rd Party Spatial Audio Extension installed that supports them, the system automatically loads this AUAudioUnit subclass into the audio signal chain while head tracking remains active on the host device.

Only the audio mix engine may use AUHeadTrackingBinauralRenderer Audio Units to provide on demand Bluetooth head tracking support. See the 3rd Party Spatial Audio Extension programming guide for more information.

## Topics

### Instance Properties
- [var deviceUID: String?](auheadtrackingbinauralrenderer/deviceuid.md)
  The Unique Identifier (UID) of the Bluetooth headphone device providing IMU sensor data for head tracking.
- [var isDisabled: Bool](auheadtrackingbinauralrenderer/isdisabled.md)
  Indicates whether the host is bypassing the renderer due to poor performance.
- [var isHeadTracking: Bool](auheadtrackingbinauralrenderer/isheadtracking.md)
  Indicates whether the host currently has enabled head tracking for this spatial Audio Unit.

## Relationships

### Inherits From
- [AUAudioUnit](auaudiounit.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating an audio unit extension](../AVFAudio/creating-an-audio-unit-extension.md)
  Build an extension by using an Xcode template.
- [Creating custom audio effects](../AVFAudio/creating-custom-audio-effects.md)
  Add custom audio-effect processing to apps like Logic Pro X and GarageBand by creating Audio Unit (AU) plug-ins.
- [Incorporating Audio Effects and Instruments](incorporating-audio-effects-and-instruments.md)
  Add custom audio processing and MIDI instruments to your app by hosting Audio Unit (AU) plug-ins.
- [Debugging Out-of-Process Audio Units on Apple Silicon](debugging-out-of-process-audio-units-on-apple-silicon.md)
  Connect to out-of-process audio units using the Xcode debugger.
- [Rendering Spatial Audio from Bluetooth headphones](rendering-spatial-audio-from-bluetooth-headphones.md)
  Create a Spatial Audio extension that allows Bluetooth headphones to track the wearer’s head movements for spatial audio playback.
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
- [func AudioUnitExtensionCopyComponentList(CFString) -> Unmanaged<CFArray>?](audiounitextensioncopycomponentlist(_:).md)
  Returns the component registrations for a given audio unit extension.
- [func AudioUnitExtensionSetComponentList(CFString, CFArray?) -> OSStatus](audiounitextensionsetcomponentlist(_:_:).md)
  Allows the implementor of an audio unit extension to dynamically modify the list of component registrations for the extension.
- [protocol AUAudioUnitFactory](auaudiounitfactory.md)
  An object that creates a version 3 audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auheadtrackingbinauralrenderer)*