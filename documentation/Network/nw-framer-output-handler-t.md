# nw_framer_output_handler_t

**Framework**: Network  
**Kind**: typealias

A handler that notifies your protocol about a new outbound message.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias nw_framer_output_handler_t = (nw_framer_t, nw_framer_message_t, Int, Bool) -> Void
```

#### Discussion

The output handler is your opportunity to encapsulate or encode a signle application message. You should write any output using [`nw_framer_write_output(_:_:_:)`](nw_framer_write_output(_:_:_:).md), [`nw_framer_write_output_data(_:_:)`](nw_framer_write_output_data(_:_:).md), or [`nw_framer_write_output_no_copy(_:_:)`](nw_framer_write_output_no_copy(_:_:).md) before returning from the output handler. If you do not write a message, the application message will be discarded.

## Parameters

- `framer`: The framer instance associated with the connection.
- `message`: The framer message passed by the application.
- `message_length`: The length of the message content being sent.
- `is_complete`: A boolean indicating if this the last chunk of a message.

## See Also

- [func nw_framer_set_output_handler(nw_framer_t, nw_framer_output_handler_t)](nw_framer_set_output_handler(_:_:).md)
  Sets a block to handle new outbound messages.
- [func nw_framer_parse_output(nw_framer_t, Int, Int, UnsafeMutablePointer<UInt8>?, (UnsafeMutablePointer<UInt8>?, Int, Bool) -> Int) -> Bool](nw_framer_parse_output(_:_:_:_:_:).md)
  Examines the content of output data while inside your output handler.
- [typealias nw_framer_parse_completion_t](nw_framer_parse_completion_t.md)
  A handler that examines a range of data being sent or received.
- [func nw_framer_write_output(nw_framer_t, UnsafePointer<UInt8>, Int)](nw_framer_write_output(_:_:_:).md)
  Sends arbitrary output data in a buffer from your protocol to the next protocol.
- [func nw_framer_write_output_data(nw_framer_t, dispatch_data_t)](nw_framer_write_output_data(_:_:).md)
  Sends arbitrary output data from your protocol to the next protocol.
- [func nw_framer_write_output_no_copy(nw_framer_t, Int) -> Bool](nw_framer_write_output_no_copy(_:_:).md)
  Sends a specific number of bytes from a message while inside your output handler.
- [func nw_framer_pass_through_output(nw_framer_t)](nw_framer_pass_through_output(_:).md)
  Indicates that your protocol no longer needs to handle output data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_framer_output_handler_t)*