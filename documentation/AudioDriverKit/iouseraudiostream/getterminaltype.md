# GetTerminalType

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the terminal type of the stream.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
IOUserAudioStreamTerminalType GetTerminalType();
```

## Return Value

The stream’s terminal type.

## Discussion

This method synchronizes by using the work queue created by the object.

## See Also

### Working with Stream Terminals
- [SetTerminalType](./setterminaltype.md)
  Sets the terminal type of the stream.
- [IOUserAudioStreamTerminalType](../audiodriverkit-page/iouseraudiostreamterminaltype.md)
  Constants that describe the terminal type of an audio stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream/getterminaltype)*