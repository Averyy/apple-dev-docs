# manufacturerName

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The name of the manufacturer of the audio unit component.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var manufacturerName: String { get }
```

```objc
@property (nonatomic, readonly) NSString * manufacturerName;
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
- [var componentURL: URL?](./componenturl.md)
  The URL of the audio unit component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponent/manufacturername)*