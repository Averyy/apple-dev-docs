# es_release_message(_:)

**Framework**: Endpoint Security  
**Kind**: func

Releases a previously-retained message.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func es_release_message(_ msg: UnsafePointer<es_message_t>)
```

## Parameters

- `msg`: The message to release.

## See Also

- [func es_retain_message(UnsafePointer<es_message_t>)](es_retain_message(_:).md)
  Retains the given message, extending its lifetime until released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_release_message(_:))*