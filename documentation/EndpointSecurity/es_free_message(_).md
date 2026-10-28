# es_free_message(_:)

**Framework**: Endpoint Security  
**Kind**: func  
**Role**: Function

Frees the memory allocated for the given message.

**Availability**:
- macOS 10.15+ - Deprecated in 11.0

> **Deprecated**: Use [`es_release_message(_:)`](./es_release_message%28_%29.md) to release a message.

## Declaration

```swift
func es_free_message(_ msg: UnsafeMutablePointer<es_message_t>)
```

```c
extern void es_free_message(es_message_t *msg);
```

## Discussion

Only free messages you explicitly copied with [`es_copy_message(_:)`](./es_copy_message%28_%29.md).

> ⚠️ **Warning**:  Freeing a message from inside a handler block will cause your app to crash.

## Parameters

- `msg`: The message to free.

## See Also

### Deprecated Functions
- [func es_copy_message(UnsafePointer<es_message_t>) -> UnsafeMutablePointer<es_message_t>?](./es_copy_message%28_%29.md)
  Copies a message, by allocating new memory.
- [func es_message_size(UnsafePointer<es_message_t>) -> Int](./es_message_size%28_%29.md)
  Calculates the size of a message structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_free_message(_:))*