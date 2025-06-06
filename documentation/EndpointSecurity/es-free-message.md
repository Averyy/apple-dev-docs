# es_free_message(_:)

**Framework**: Endpoint Security  
**Kind**: func

Frees the memory allocated for the given message.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func es_free_message(_ msg: UnsafeMutablePointer<es_message_t>)
```

#### Discussion

Only free messages you explicitly copied with [`es_copy_message(_:)`](es_copy_message(_:).md).

> ⚠️ **Warning**:  Freeing a message from inside a handler block will cause your app to crash.

 Freeing a message from inside a handler block will cause your app to crash.

## Parameters

- `msg`: The message to free.

## See Also

- [func es_copy_message(UnsafePointer<es_message_t>) -> UnsafeMutablePointer<es_message_t>?](es_copy_message(_:).md)
  Copies a message, by allocating new memory.
- [func es_message_size(UnsafePointer<es_message_t>) -> Int](es_message_size(_:).md)
  Calculates the size of a message structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_free_message(_:))*