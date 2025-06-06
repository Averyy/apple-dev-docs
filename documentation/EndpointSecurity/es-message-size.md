# es_message_size(_:)

**Framework**: Endpoint Security  
**Kind**: func

Calculates the size of a message structure.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 10.15+

## Declaration

```swift
func es_message_size(_ msg: UnsafePointer<es_message_t>) -> Int
```

#### Return Value

The calculated size of the message.

## Parameters

- `msg`: The message to calculate the size of.

## See Also

- [func es_copy_message(UnsafePointer<es_message_t>) -> UnsafeMutablePointer<es_message_t>?](es_copy_message(_:).md)
  Copies a message, by allocating new memory.
- [func es_free_message(UnsafeMutablePointer<es_message_t>)](es_free_message(_:).md)
  Frees the memory allocated for the given message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_message_size(_:))*