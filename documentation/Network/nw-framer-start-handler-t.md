# nw_framer_start_handler_t

**Framework**: Network  
**Kind**: typealias

A handler that represents the entry point into your custom protocol.

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
typealias nw_framer_start_handler_t = (nw_framer_t) -> nw_framer_start_result_t
```

#### Return Value

Return a start result indicating if the connection should become ready immediately, or wait for you protocol to perform a handshake.

#### Discussion

Within your start handler, you should register all other callbacks for your custom protocol, particularly [`nw_framer_set_output_handler(_:_:)`](nw_framer_set_output_handler(_:_:).md) and [`nw_framer_set_input_handler(_:_:)`](nw_framer_set_input_handler(_:_:).md).

Any state that you need to be associated with your protocol as customizable options can be captured within the start block.

## See Also

- [func nw_framer_create_definition(UnsafePointer<CChar>, UInt32, nw_framer_start_handler_t) -> nw_protocol_definition_t](nw_framer_create_definition(_:_:_:).md)
  Initializes a new protocol definition based on your protocol implementation.
- [typealias nw_framer_t](nw_framer_t.md)
  An object that represents a single instance of your custom protocol running in a connection.
- [struct nw_framer_start_result_t](nw_framer_start_result_t.md)
  Results that you send to indicate the disposition of your protocol after the start handler is invoked.
- [var NW_FRAMER_CREATE_FLAGS_DEFAULT: Int32](nw_framer_create_flags_default.md)
  A constant flag value that indicates that the default framer protocol behavior should be used.
- [func nw_framer_create_options(nw_protocol_definition_t) -> nw_protocol_options_t](nw_framer_create_options(_:).md)
  Initializes a set of protocol options with a custom framer definition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_framer_start_handler_t)*