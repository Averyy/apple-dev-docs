# TransportMessage

**Framework**: Accessory Transport Extension  
**Kind**: struct

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
struct TransportMessage
```

## Topics

### Initializers
- [init(sessionID: UUID, data: Data)](transportmessage/init(sessionid:data:).md)
  Create a new message for a session.
### Instance Properties
- [let data: Data](transportmessage/data.md)
- [let sessionID: UUID](transportmessage/sessionid.md)
### Type Aliases
- [TransportMessage.Completion](transportmessage/completion.md)
### Enumerations
- [TransportMessage.Result](transportmessage/result.md)
  Result of message transmission.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/transportmessage)*