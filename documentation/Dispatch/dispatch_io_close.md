# dispatch_io_close

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Closes the specified channel to new read and write operations.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void dispatch_io_close(dispatch_io_t channel, dispatch_io_close_flags_t flags);
```

## Discussion

After calling this function, you should not schedule any more read or write operations on the channel. Doing so causes an error to be sent to your handler.

If the [`DISPATCH_IO_STOP`](./dispatch_io_stop.md) option is specified in the `flags` parameter, the system attempts to interrupt any outstanding read and write operations on the I/O channel. Even if you specify this flag, the corresponding handlers may be invoked with partial results. In addition, the final invocation of the handler is passed the `ECANCELED` error code to indicate that the operation was interrupted. If you do not specify the [`DISPATCH_IO_STOP`](./dispatch_io_stop.md) flag, read and write operations on the channel run to completion as normal.

## Parameters

- `channel`: The channel to close.
- `flags`: The options to use when closing the channel. For a list of possible values, see [`dispatch_io_close_flags_t`](./dispatch_io_close_flags_t.md).

## See Also

### Closing the File
- [dispatch_io_close_flags_t](./dispatch_io_close_flags_t.md)
  Additional flags to use when closing an I/O channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_io_close)*