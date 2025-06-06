# AudioUnitExtensionSetComponentList(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Allows the implementor of an audio unit extension to dynamically modify the list of component registrations for the extension.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func AudioUnitExtensionSetComponentList(_ extensionIdentifier: CFString, _ audioComponentInfo: CFArray?) -> OSStatus
```

#### Return Value

An OSStatus result code.

#### Discussion

The bundle identifier of the process that calls this function must prefix or match the extension identifier.

For an example of the array of dictionaries, see [`Audio Components`](audio-components.md).

## Parameters

- `extensionIdentifier`: The bundle identifier of the audio unit extension.
- `audioComponentInfo`: An array of dictionaries, one for each component registration.

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
- [protocol AUAudioUnitFactory](auaudiounitfactory.md)
  An object that creates a version 3 audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitextensionsetcomponentlist(_:_:))*