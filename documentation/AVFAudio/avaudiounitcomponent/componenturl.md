# componentURL

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The URL of the audio unit component.

**Availability**:
- macOS 10.10+ - Deprecated in 10.11

## Declaration

```swift
var componentURL: URL? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSURL * componentURL;
```

## See Also

### Getting Audio Unit component information
- [var audioComponentDescription: AudioComponentDescription](./audiocomponentdescription.md)
  The audio component description.
- [var availableArchitectures: [NSNumber]](./availablearchitectures.md)
  An array of architectures that the audio unit supports.
- [var configurationDictionary: [String : Any]](./configurationdictionary.md)
  The audio unit component’s configuration dictionary.
- [var hasCustomView: Bool](./hascustomview.md)
  A Boolean value that indicates whether the audio unit component has a custom view.
- [var hasMIDIInput: Bool](./hasmidiinput.md)
  A Boolean value that indicates whether the audio unit component has MIDI input.
- [var hasMIDIOutput: Bool](./hasmidioutput.md)
  A Boolean value that indicates whether the audio unit component has MIDI output.
- [var manufacturerName: String](./manufacturername.md)
  The name of the manufacturer of the audio unit component.
- [var name: String](./name.md)
  The name of the audio unit component.
- [var passesAUVal: Bool](./passesauval.md)
  A Boolean value that indicates whether the audio unit component passes the validation tests.
- [var isSandboxSafe: Bool](./issandboxsafe.md)
  A Boolean value that indicates whether the audio unit component is safe for sandboxing.
- [func supportsNumberInputChannels(Int, outputChannels: Int) -> Bool](./supportsnumberinputchannels%28_,outputchannels%29.md)
  Gets a Boolean value that indicates whether the audio unit component supports the specified number of input and output channels.
- [var typeName: String](./typename.md)
  The audio unit component type.
- [var version: Int](./version.md)
  The audio unit component version number.
- [var versionString: String](./versionstring.md)
  A string that represents the audio unit component version number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponent/componenturl)*