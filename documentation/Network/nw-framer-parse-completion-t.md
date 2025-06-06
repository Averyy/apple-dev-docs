# nw_framer_parse_completion_t

**Framework**: Network  
**Kind**: typealias

A handler that examines a range of data being sent or received.

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
typealias nw_framer_parse_completion_t = (UnsafeMutablePointer<UInt8>?, Int, Bool) -> Int
```

#### Return Value

Return the number of bytes by which to increment the input or output cursor. Once the cursor is moved, previous bytes will no longer be delivered to [`nw_framer_parse_input(_:_:_:_:_:)`](nw_framer_parse_input(_:_:_:_:_:).md) and [`nw_framer_deliver_input_no_copy(_:_:_:_:)`](nw_framer_deliver_input_no_copy(_:_:_:_:).md) for input data, or [`nw_framer_parse_output(_:_:_:_:_:)`](nw_framer_parse_output(_:_:_:_:_:).md) and [`nw_framer_write_output_no_copy(_:_:)`](nw_framer_write_output_no_copy(_:_:).md) for output messages.

## Parameters

- `buffer`: The pointer to bytes to parse.
- `buffer_length`: The length of the buffer.
- `is_complete`: A boolean indicating if this span of bytes represents the end of a message.

## See Also

- [func nw_framer_set_output_handler(nw_framer_t, nw_framer_output_handler_t)](nw_framer_set_output_handler(_:_:).md)
  Sets a block to handle new outbound messages.
- [typealias nw_framer_output_handler_t](nw_framer_output_handler_t.md)
  A handler that notifies your protocol about a new outbound message.
- [func nw_framer_parse_output(nw_framer_t, Int, Int, UnsafeMutablePointer<UInt8>?, (UnsafeMutablePointer<UInt8>?, Int, Bool) -> Int) -> Bool](nw_framer_parse_output(_:_:_:_:_:).md)
  Examines the content of output data while inside your output handler.
- [func nw_framer_write_output(nw_framer_t, UnsafePointer<UInt8>, Int)](nw_framer_write_output(_:_:_:).md)
  Sends arbitrary output data in a buffer from your protocol to the next protocol.
- [func nw_framer_write_output_data(nw_framer_t, dispatch_data_t)](nw_framer_write_output_data(_:_:).md)
  Sends arbitrary output data from your protocol to the next protocol.
- [func nw_framer_write_output_no_copy(nw_framer_t, Int) -> Bool](nw_framer_write_output_no_copy(_:_:).md)
  Sends a specific number of bytes from a message while inside your output handler.
- [func nw_framer_pass_through_output(nw_framer_t)](nw_framer_pass_through_output(_:).md)
  Indicates that your protocol no longer needs to handle output data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_framer_parse_completion_t)*