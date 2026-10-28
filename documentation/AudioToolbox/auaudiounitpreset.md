# AUAudioUnitPreset

**Framework**: Audio Toolbox  
**Kind**: class  
**Role**: Class

A class that describes an interface for custom parameter settings provided by the audio unit developer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AUAudioUnitPreset
```

```objc
@interface AUAudioUnitPreset : NSObject
```

## Overview

These presets often produce a useful sound or starting point.

For more details on working with Audio Unit presets, see [Audio Units - How to correctly save and restore Audio Unit presets.](https://developer.apple.com/library/archive/technotes/tn2157/_index.html#//apple_ref/doc/uid/DTS40011953) Note that the version 3 [`fullState`](./auaudiounit/fullstate.md) property is bridged to the version 2 `kAudioUnitProperty_ClassInfo` API. Similarly, the version 3 [`fullStateForDocument`](./auaudiounit/fullstatefordocument.md) property is bridged to the version 2 `kAudioUnitProperty_ClassInfoFromDocument` API.

## Topics

### Preset Properties
- [var name: String](./auaudiounitpreset/name.md)
  The preset’s name.
- [var number: Int](./auaudiounitpreset/number.md)
  The preset’s unique numeric identifier.
### Initializers
- [init?(coder: NSCoder)](./auaudiounitpreset/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Audio Units
- [Creating an Audio Unit extension](../AVFAudio/creating-an-audio-unit-extension.md)
  Build an extension by using an Xcode template.
- [Creating custom audio effects](../AVFAudio/creating-custom-audio-effects.md)
  Add custom audio-effect processing to apps like Logic Pro X and GarageBand by creating Audio Unit (AU) plug-ins.
- [Incorporating Audio Effects and Instruments](./incorporating-audio-effects-and-instruments.md)
  Add custom audio processing and MIDI instruments to your app by hosting Audio Unit (AU) plug-ins.
- [Debugging Out-of-Process Audio Units on Apple Silicon](./debugging-out-of-process-audio-units-on-apple-silicon.md)
  Connect to out-of-process audio units using the Xcode debugger.
- [Rendering Spatial Audio from Bluetooth headphones](./rendering-spatial-audio-from-bluetooth-headphones.md)
  Create a Spatial Audio extension that allows Bluetooth headphones to track the wearer’s head movements for spatial audio playback.
- [class AUAudioUnit](./auaudiounit.md)
  A class that defines a host’s interface to an audio unit.
- [class AUAudioUnitBus](./auaudiounitbus.md)
  A class that defines an input or output connection point on an audio unit.
- [class AUAudioUnitBusArray](./auaudiounitbusarray.md)
  A class that defines a container for an audio unit’s input or output busses.
- [class AUAudioUnitV2Bridge](./auaudiounitv2bridge.md)
  A class that wraps a version 2 audio unit as version 3 audio unit.
- [class AUHeadTrackingBinauralRenderer](./auheadtrackingbinauralrenderer.md)
  A subclass of AUAudioUnit specifically for 3rd party spatial Audio Units.
- [func AudioUnitExtensionCopyComponentList(CFString) -> Unmanaged<CFArray>?](./audiounitextensioncopycomponentlist%28_%29.md)
  Returns the component registrations for a given audio unit extension.
- [func AudioUnitExtensionSetComponentList(CFString, CFArray?) -> OSStatus](./audiounitextensionsetcomponentlist%28_,_%29.md)
  Allows the implementor of an audio unit extension to dynamically modify the list of component registrations for the extension.
- [protocol AUAudioUnitFactory](./auaudiounitfactory.md)
  An object that creates a version 3 audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitpreset)*