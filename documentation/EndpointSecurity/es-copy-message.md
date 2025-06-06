# es_copy_message(_:)

**Framework**: Endpoint Security  
**Kind**: func

Copies a message, by allocating new memory.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func es_copy_message(_ msg: UnsafePointer<es_message_t>) -> UnsafeMutablePointer<es_message_t>?
```

#### Return Value

A pointer to a copy of the original message.

#### Discussion

After calling this function, the caller owns this memory and must eventually free it with [`es_free_message(_:)`](es_free_message(_:).md) to avoid leaking memory.

## Parameters

- `msg`: The message to copy.

## See Also

- [func es_message_size(UnsafePointer<es_message_t>) -> Int](es_message_size(_:).md)
  Calculates the size of a message structure.
- [func es_free_message(UnsafeMutablePointer<es_message_t>)](es_free_message(_:).md)
  Frees the memory allocated for the given message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_copy_message(_:))*