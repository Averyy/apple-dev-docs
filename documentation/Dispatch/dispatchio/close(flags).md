# close(flags:)

**Framework**: Dispatch  
**Kind**: method  
**Role**: Instance Method

Closes the channel to new read and write operations.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func close(flags: DispatchIO.CloseFlags = [])
```

## Discussion

After calling this method, do not schedule any more read or write operations on the channel. Doing so causes an error to be sent to your handler.

If the [`stop`](./closeflags/stop.md) option is specified in the flags parameter, the system attempts to interrupt any outstanding read and write operations on the I/O channel. If you specify this flag, the corresponding handlers may be invoked with partial results. In addition, the final invocation of the handler is passed the `POSIXErrorCode.ECANCELED` error code to indicate that the operation was interrupted. If you do not specify the [`stop`](./closeflags/stop.md) flag, read and write operations on the channel run to completion as normal.

## Parameters

- `flags`: The options to use when closing the channel. For a list of possible values, see [`DispatchIO.CloseFlags`](./closeflags.md).

## See Also

### Closing the File
- [DispatchIO.CloseFlags](./closeflags.md)
  Additional flags to use when closing an I/O channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchio/close(flags:))*