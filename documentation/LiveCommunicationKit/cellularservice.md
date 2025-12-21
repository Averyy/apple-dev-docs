# CellularService

**Framework**: LiveCommunicationKit  
**Kind**: struct

A structure that represents the cellular service account to use for starting or joining a conversation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct CellularService
```

## Mentions

- [Preparing your app to be the default dialer app](preparing-your-app-to-be-the-default-dialer-app.md)

## Topics

### Attributes
- [let label: String](cellularservice/label.md)
  The label for the service that people view in a communication app.
- [let id: UUID](cellularservice/id.md)
  A unique identifier that identifies the cellular service.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class TelephonyConversationManager](telephonyconversationmanager.md)
  An interface for initiating cellular network conversations.
- [struct StartCellularConversationAction](startcellularconversationaction.md)
  The action that starts a cellular conversation using the default calling app.
- [struct Handle](handle.md)
  A way to reach a participant, such as a phone number or email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/cellularservice)*