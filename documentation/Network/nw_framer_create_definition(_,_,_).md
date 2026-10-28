# nw_framer_create_definition(_:_:_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Initializes a new protocol definition based on your protocol implementation.

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
func nw_framer_create_definition(_ identifier: UnsafePointer<CChar>, _ flags: UInt32, _ start_handler: @escaping nw_framer_start_handler_t) -> nw_protocol_definition_t
```

```c
nw_protocol_definition_tnw_framer_create_definition(const char *identifier, uint32_t flags, nw_framer_start_handler_t start_handler);
```

## Discussion

Each time you initialize a protocol definition with your custom start handler, a new definition is created that will not be considered equal to other definitions. If you need to associate messages with a protocol you have added to a connection’s protocol stack, make sure to use the same definition.

## See Also

### Adding Framers to Connections
- [typealias nw_framer_start_handler_t](./nw_framer_start_handler_t.md)
  A handler that represents the entry point into your custom protocol.
- [typealias nw_framer_t](./nw_framer_t.md)
  An object that represents a single instance of your custom protocol running in a connection.
- [struct nw_framer_start_result_t](./nw_framer_start_result_t.md)
  Results that you send to indicate the disposition of your protocol after the start handler is invoked.
- [var NW_FRAMER_CREATE_FLAGS_DEFAULT: Int32](./nw_framer_create_flags_default.md)
  A constant flag value that indicates that the default framer protocol behavior should be used.
- [func nw_framer_create_options(nw_protocol_definition_t) -> nw_protocol_options_t](./nw_framer_create_options%28_%29.md)
  Initializes a set of protocol options with a custom framer definition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_framer_create_definition(_:_:_:))*