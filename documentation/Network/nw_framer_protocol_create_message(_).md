# nw_framer_protocol_create_message(_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Initializes an empty message for a custom framer definition.

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
func nw_framer_protocol_create_message(_ definition: nw_protocol_definition_t) -> nw_framer_message_t
```

```c
nw_framer_message_tnw_framer_protocol_create_message(nw_protocol_definition_t definition);
```

## See Also

### Customizing Framer Messages
- [typealias nw_framer_message_t](./nw_framer_message_t.md)
  A message for a custom protocol, in which you can store arbitrary key-value pairs.
- [func nw_protocol_metadata_is_framer_message(nw_protocol_metadata_t) -> Bool](./nw_protocol_metadata_is_framer_message%28_%29.md)
  Checks if a metadata object represents a custom framer protocol message.
- [func nw_framer_message_create(nw_framer_t) -> nw_framer_message_t](./nw_framer_message_create%28_%29.md)
  Initializes an empty message from within a framer implementation.
- [func nw_framer_message_set_value(nw_framer_message_t, UnsafePointer<CChar>, UnsafeMutableRawPointer?, nw_framer_message_dispose_value_t?)](./nw_framer_message_set_value%28_,_,_,_%29.md)
  Sets a value to be stored in a framer message, with a completion to call to disposed the stored value when the message is released.
- [typealias nw_framer_message_dispose_value_t](./nw_framer_message_dispose_value_t.md)
  A handler that’s invoked when your custom value needs to be released due to a message being released or the value being replaced.
- [func nw_framer_message_set_object_value(nw_framer_message_t, UnsafePointer<CChar>, Any?)](./nw_framer_message_set_object_value%28_,_,_%29.md)
  Sets an NSObject value to be stored in a framer message.
- [func nw_framer_message_access_value(nw_framer_message_t, UnsafePointer<CChar>, (UnsafeRawPointer?) -> Bool) -> Bool](./nw_framer_message_access_value%28_,_,_%29.md)
  Accesses a custom value stored in a framer message.
- [func nw_framer_message_copy_object_value(nw_framer_message_t, UnsafePointer<CChar>) -> Any?](./nw_framer_message_copy_object_value%28_,_%29.md)
  Accesses an NSObject value stored in a framer message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_framer_protocol_create_message(_:))*