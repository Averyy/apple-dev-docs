# supportsNumberInputChannels(_:outputChannels:)

**Framework**: AVFAudio  
**Kind**: method

Gets a Boolean value that indicates whether the audio unit component supports the specified number of input and output channels.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func supportsNumberInputChannels(_ numInputChannels: Int, outputChannels numOutputChannels: Int) -> Bool
```

#### Return Value

A value of [`true`](https://developer.apple.com/documentation/swift/true) if the audio unit component supports the specified number of input and output channels; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `numInputChannels`: The number of input channels.
- `numOutputChannels`: The number of output channels.

## See Also

- [var audioComponentDescription: AudioComponentDescription](avaudiounitcomponent/audiocomponentdescription.md)
  The audio component description.
- [var availableArchitectures: [NSNumber]](avaudiounitcomponent/availablearchitectures.md)
  An array of architectures that the audio unit supports.
- [var configurationDictionary: [String : Any]](avaudiounitcomponent/configurationdictionary.md)
  The audio unit component’s configuration dictionary.
- [var hasCustomView: Bool](avaudiounitcomponent/hascustomview.md)
  A Boolean value that indicates whether the audio unit component has a custom view.
- [var hasMIDIInput: Bool](avaudiounitcomponent/hasmidiinput.md)
  A Boolean value that indicates whether the audio unit component has MIDI input.
- [var hasMIDIOutput: Bool](avaudiounitcomponent/hasmidioutput.md)
  A Boolean value that indicates whether the audio unit component has MIDI output.
- [var manufacturerName: String](avaudiounitcomponent/manufacturername.md)
  The name of the manufacturer of the audio unit component.
- [var name: String](avaudiounitcomponent/name.md)
  The name of the audio unit component.
- [var passesAUVal: Bool](avaudiounitcomponent/passesauval.md)
  A Boolean value that indicates whether the audio unit component passes the validation tests.
- [var isSandboxSafe: Bool](avaudiounitcomponent/issandboxsafe.md)
  A Boolean value that indicates whether the audio unit component is safe for sandboxing.
- [var typeName: String](avaudiounitcomponent/typename.md)
  The audio unit component type.
- [var version: Int](avaudiounitcomponent/version.md)
  The audio unit component version number.
- [var versionString: String](avaudiounitcomponent/versionstring.md)
  A string that represents the audio unit component version number.
- [var componentURL: URL?](avaudiounitcomponent/componenturl.md)
  The URL of the audio unit component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponent/supportsnumberinputchannels(_:outputchannels:))*