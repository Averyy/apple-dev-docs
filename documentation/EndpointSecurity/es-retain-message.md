# es_retain_message(_:)

**Framework**: Endpoint Security  
**Kind**: func

Retains the given message, extending its lifetime until released.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func es_retain_message(_ msg: UnsafePointer<es_message_t>)
```

#### Discussion

If you asynchronously process the message provided to the event-handler block of [`es_new_client(_:_:)`](es_new_client(_:_:).md), you must retain the message.

## Parameters

- `msg`: The message to retain.

## See Also

- [func es_release_message(UnsafePointer<es_message_t>)](es_release_message(_:).md)
  Releases a previously-retained message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_retain_message(_:))*