# AUAudioUnitFactory

**Framework**: Audio Toolbox  
**Kind**: protocol

An object that creates a version 3 audio unit.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol AUAudioUnitFactory : NSExtensionRequestHandling
```

#### Overview

In most cases, if your audio unit specifies parameters to configure its behavior, it should provide a custom user interface to control those parameters. You create this user interface by subclassing the [`AUViewController`](https://developer.apple.com/documentation/CoreAudioKit/AUViewController) class and implementing this protocol on your subclass.

If your audio unit doesn’t provide a custom user interface, subclass the [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class) class instead. In this case, the hosting app must create a generic user interface for your audio unit.

## Topics

### Required Methods
- [func createAudioUnit(with: AudioComponentDescription) throws -> AUAudioUnit](auaudiounitfactory/createaudiounit(with:).md)
  Creates an instance of an extension’s audio unit.

## Relationships

### Inherits From
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitfactory)*