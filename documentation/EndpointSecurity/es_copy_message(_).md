# es_copy_message(_:)

**Framework**: Endpoint Security  
**Kind**: func  
**Role**: Function

Copies a message, by allocating new memory.

**Availability**:
- macOS 10.15+ - Deprecated in 11.0

> **Deprecated**: Use [`es_retain_message(_:)`](./es_retain_message%28_%29.md) to retain a message.

## Declaration

```swift
func es_copy_message(_ msg: UnsafePointer<es_message_t>) -> UnsafeMutablePointer<es_message_t>?
```

```c
extern es_message_t *es_copy_message(const es_message_t *msg);
```

## Return Value

A pointer to a copy of the original message.

## Discussion

After calling this function, the caller owns this memory and must eventually free it with [`es_free_message(_:)`](./es_free_message%28_%29.md) to avoid leaking memory.

## Parameters

- `msg`: The message to copy.

## See Also

### Deprecated Functions
- [func es_message_size(UnsafePointer<es_message_t>) -> Int](./es_message_size%28_%29.md)
  Calculates the size of a message structure.
- [func es_free_message(UnsafeMutablePointer<es_message_t>)](./es_free_message%28_%29.md)
  Frees the memory allocated for the given message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_copy_message(_:))*