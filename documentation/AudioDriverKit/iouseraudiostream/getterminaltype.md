# GetTerminalType

**Framework**: AudioDriverKit  
**Kind**: method

Gets the terminal type of the stream.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
IOUserAudioStreamTerminalType GetTerminalType();
```

#### Return Value

The stream’s terminal type.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

- [SetTerminalType](iouseraudiostream/setterminaltype.md)
  Sets the terminal type of the stream.
- [IOUserAudioStreamTerminalType](audiodriverkit/iouseraudiostreamterminaltype.md)
  Constants that describe the terminal type of an audio stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream/getterminaltype)*