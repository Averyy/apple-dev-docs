# init(conversationUUID:timeoutDate:)

**Framework**: LiveCommunicationKit  
**Kind**: init

Creates a conversation action.

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

- `conversationUUID`: The unique identifier of the action’s associated conversation.
- `timeoutDate`: The point in time that marks when the action can’t be completed anymore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationaction/init(conversationuuid:timeoutdate:))*