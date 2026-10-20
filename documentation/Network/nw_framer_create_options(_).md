# nw_framer_create_options(_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Initializes a set of protocol options with a custom framer definition.

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
func nw_framer_create_options(_ framer_definition: nw_protocol_definition_t) -> nw_protocol_options_t
```

```c
nw_protocol_options_tnw_framer_create_options(nw_protocol_definition_t framer_definition);
```

## See Also

### Adding Framers to Connections
- [func nw_framer_create_definition(UnsafePointer<CChar>, UInt32, nw_framer_start_handler_t) -> nw_protocol_definition_t](./nw_framer_create_definition%28_,_,_%29.md)
  Initializes a new protocol definition based on your protocol implementation.
- [typealias nw_framer_start_handler_t](./nw_framer_start_handler_t.md)
  A handler that represents the entry point into your custom protocol.
- [typealias nw_framer_t](./nw_framer_t.md)
  An object that represents a single instance of your custom protocol running in a connection.
- [struct nw_framer_start_result_t](./nw_framer_start_result_t.md)
  Results that you send to indicate the disposition of your protocol after the start handler is invoked.
- [var NW_FRAMER_CREATE_FLAGS_DEFAULT: Int32](./nw_framer_create_flags_default.md)
  A constant flag value that indicates that the default framer protocol behavior should be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_framer_create_options(_:))*