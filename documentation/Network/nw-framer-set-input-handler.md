# nw_framer_set_input_handler(_:_:)

**Framework**: Network  
**Kind**: func

Sets a block to handle new inbound data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func nw_framer_set_input_handler(_ framer: nw_framer_t, _ input_handler: @escaping nw_framer_input_handler_t)
```

## See Also

- [typealias nw_framer_input_handler_t](nw_framer_input_handler_t.md)
  A handler that notifies your protocol that new inbound data is available to parse.
- [func nw_framer_parse_input(nw_framer_t, Int, Int, UnsafeMutablePointer<UInt8>?, (UnsafeMutablePointer<UInt8>?, Int, Bool) -> Int) -> Bool](nw_framer_parse_input(_:_:_:_:_:).md)
  Examines the content of input data while inside your input handler block.
- [typealias nw_framer_parse_completion_t](nw_framer_parse_completion_t.md)
  A handler that examines a range of data being sent or received.
- [func nw_framer_deliver_input(nw_framer_t, UnsafePointer<UInt8>, Int, nw_framer_message_t, Bool)](nw_framer_deliver_input(_:_:_:_:_:).md)
  Delivers an inbound message containing arbitrary data from your protocol to the application.
- [func nw_framer_deliver_input_no_copy(nw_framer_t, Int, nw_framer_message_t, Bool) -> Bool](nw_framer_deliver_input_no_copy(_:_:_:_:).md)
  Delivers an inbound message containing a specific number of next received bytes.
- [func nw_framer_pass_through_input(nw_framer_t)](nw_framer_pass_through_input(_:).md)
  Indicates that your protocol no longer needs to handle input data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_framer_set_input_handler(_:_:))*