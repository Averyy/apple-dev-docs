# es_message_size(_:)

**Framework**: Endpoint Security  
**Kind**: func  
**Role**: Function

Calculates the size of a message structure.

**Availability**:
- iOS 18.0+ - Deprecated in 18.0
- iPadOS 18.0+ - Deprecated in 18.0
- Mac Catalyst 18.0+ - Deprecated in 18.0
- macOS 10.15+ - Deprecated in 11.0

> **Deprecated**: Use [`es_retain_message(_:)`](./es_retain_message%28_%29.md) to retain a message. Don’t use [`es_message_size(_:)`](./es_message_size%28_%29.md) in conjunction with attempting to copy a message; doing so will result in use-after-free bugs.

## Declaration

```swift
func es_message_size(_ msg: UnsafePointer<es_message_t>) -> Int
```

```c
extern size_t es_message_size(const es_message_t *msg);
```

## Return Value

The calculated size of the message.

## Parameters

- `msg`: The message to calculate the size of.

## See Also

### Deprecated Functions
- [func es_copy_message(UnsafePointer<es_message_t>) -> UnsafeMutablePointer<es_message_t>?](./es_copy_message%28_%29.md)
  Copies a message, by allocating new memory.
- [func es_free_message(UnsafeMutablePointer<es_message_t>)](./es_free_message%28_%29.md)
  Frees the memory allocated for the given message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_message_size(_:))*