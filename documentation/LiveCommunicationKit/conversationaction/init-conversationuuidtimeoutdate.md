# init(conversationUUID:timeoutDate:)

**Framework**: LiveCommunicationKit  
**Kind**: init

Initializes a new conversation action.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
convenience init(conversationUUID: UUID, timeoutDate: Date = Date(timeIntervalSinceNow: 30))
```

## Parameters

- `timeoutDate`: The   after which the action cannot be completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationaction/init(conversationuuid:timeoutdate:))*