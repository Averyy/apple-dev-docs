# availableArchitectures

**Framework**: AVFAudio  
**Kind**: property

An array of architectures that the audio unit supports.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var availableArchitectures: [NSNumber] { get }
```

#### Discussion

This is an `NSArray` of `NSNumbers` where each entry corresponds to one of the constants in Mach-O Architecture in [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle).

## See Also

- [var audioComponentDescription: AudioComponentDescription](avaudiounitcomponent/audiocomponentdescription.md)
  The audio component description.
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
- [func supportsNumberInputChannels(Int, outputChannels: Int) -> Bool](avaudiounitcomponent/supportsnumberinputchannels(_:outputchannels:).md)
  Gets a Boolean value that indicates whether the audio unit component supports the specified number of input and output channels.
- [var typeName: String](avaudiounitcomponent/typename.md)
  The audio unit component type.
- [var version: Int](avaudiounitcomponent/version.md)
  The audio unit component version number.
- [var versionString: String](avaudiounitcomponent/versionstring.md)
  A string that represents the audio unit component version number.
- [var componentURL: URL?](avaudiounitcomponent/componenturl.md)
  The URL of the audio unit component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponent/availablearchitectures)*