# SetTerminalType

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the terminal type of the stream.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetTerminalType(IOUserAudioStreamTerminalType in_terminal_type);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

If successful, changing the available formats sends a notification to the host to update the object state.

## Parameters

- `in_terminal_type`: The [`IOUserAudioStreamTerminalType`](../audiodriverkit-page/iouseraudiostreamterminaltype.md) to set.

## See Also

### Working with Stream Terminals
- [GetTerminalType](./getterminaltype.md)
  Gets the terminal type of the stream.
- [IOUserAudioStreamTerminalType](../audiodriverkit-page/iouseraudiostreamterminaltype.md)
  Constants that describe the terminal type of an audio stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream/setterminaltype)*