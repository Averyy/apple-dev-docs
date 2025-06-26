# TelephonyConversationManager

**Framework**: LiveCommunicationKit  
**Kind**: class

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final class TelephonyConversationManager
```

## Topics

### Initializers
- [init()](telephonyconversationmanager/init.md)
### Instance Properties
- [var cellularServices: [CellularService]](telephonyconversationmanager/cellularservices.md)
  The list of accounts which an application can use to dial. Your application is able to dial a conversation without any Accounts available in TelephonyManager No accounts will be available to an application if it is not the default dialing application
### Instance Methods
- [func startCellularConversation(StartCellularConversationAction) async throws](telephonyconversationmanager/startcellularconversation(_:).md)
  Dials a conversation using the provided dial request

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/telephonyconversationmanager)*