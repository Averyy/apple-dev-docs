# nw_framer_message_t

**Framework**: Network  
**Kind**: typealias  
**Role**: Type Alias

A message for a custom protocol, in which you can store arbitrary key-value pairs.

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
typealias nw_framer_message_t = nw_protocol_metadata_t
```

```c
typedef nw_protocol_metadata_t nw_framer_message_t;
```

## See Also

### Customizing Framer Messages
- [func nw_protocol_metadata_is_framer_message(nw_protocol_metadata_t) -> Bool](./nw_protocol_metadata_is_framer_message%28_%29.md)
  Checks if a metadata object represents a custom framer protocol message.
- [func nw_framer_protocol_create_message(nw_protocol_definition_t) -> nw_framer_message_t](./nw_framer_protocol_create_message%28_%29.md)
  Initializes an empty message for a custom framer definition.
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

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_framer_message_t)*