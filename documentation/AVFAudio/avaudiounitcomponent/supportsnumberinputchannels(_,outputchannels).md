# supportsNumberInputChannels(_:outputChannels:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Gets a Boolean value that indicates whether the audio unit component supports the specified number of input and output channels.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func supportsNumberInputChannels(_ numInputChannels: Int, outputChannels numOutputChannels: Int) -> Bool
```

```objc
- (BOOL) supportsNumberInputChannels:(NSInteger) numInputChannels outputChannels:(NSInteger) numOutputChannels;
```

## Return Value

A value of [`true`](../../Swift/true.md) if the audio unit component supports the specified number of input and output channels; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `numInputChannels`: The number of input channels.
- `numOutputChannels`: The number of output channels.

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
- [var typeName: String](./typename.md)
  The audio unit component type.
- [var version: Int](./version.md)
  The audio unit component version number.
- [var versionString: String](./versionstring.md)
  A string that represents the audio unit component version number.
- [var componentURL: URL?](./componenturl.md)
  The URL of the audio unit component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponent/supportsnumberinputchannels(_:outputchannels:))*