# SetTerminalType

**Framework**: AudioDriverKit  
**Kind**: method

Sets the terminal type of the stream.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetTerminalType(IOUserAudioStreamTerminalType in_terminal_type);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If successful, changing the available formats sends a notification to the host to update the object state.

## Parameters

- `in_terminal_type`: The   to set.

## See Also

- [GetTerminalType](iouseraudiostream/getterminaltype.md)
  Gets the terminal type of the stream.
- [IOUserAudioStreamTerminalType](audiodriverkit/iouseraudiostreamterminaltype.md)
  Constants that describe the terminal type of an audio stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream/setterminaltype)*