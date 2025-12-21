# cellularServices

**Framework**: LiveCommunicationKit  
**Kind**: property

A read-only list of cellular service accounts that you can use to initiate a cellular conversation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final var cellularServices: [CellularService] { get }
```

#### Discussion

To have access to cellular services, your app needs to be the default calling app. If your app doesn’t have permission to access to accounts, it can still initiate conversations using [`TelephonyConversationManager`](telephonyconversationmanager.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/telephonyconversationmanager/cellularservices)*