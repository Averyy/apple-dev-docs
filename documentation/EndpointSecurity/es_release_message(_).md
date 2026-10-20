# es_release_message(_:)

**Framework**: Endpoint Security  
**Kind**: func  
**Role**: Function

Releases a previously-retained message.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func es_release_message(_ msg: UnsafePointer<es_message_t>)
```

```c
extern void es_release_message(const es_message_t *msg);
```

## Parameters

- `msg`: The message to release.

## See Also

### Retaining and Releasing Messages
- [func es_retain_message(UnsafePointer<es_message_t>)](./es_retain_message%28_%29.md)
  Retains the given message, extending its lifetime until released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_release_message(_:))*