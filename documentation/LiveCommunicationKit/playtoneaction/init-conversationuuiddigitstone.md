# init(conversationUUID:digits:tone:)

**Framework**: LiveCommunicationKit  
**Kind**: init

Creates an action that plays a sequence of tones that indicate an interaction with the keypad.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
init(conversationUUID: UUID, digits: String, tone: PlayToneAction.Tone)
```

## Parameters

- `conversationUUID`: The unique identifier of the conversation to which this action will be applied.
- `digits`: The digits tapped by the user into the keypad or included in the dial string.
- `tone`: The tone to play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/playtoneaction/init(conversationuuid:digits:tone:))*