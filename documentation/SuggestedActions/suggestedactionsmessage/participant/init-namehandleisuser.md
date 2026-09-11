# init(name:handle:isUser:)

**Framework**: Suggested Actions  
**Kind**: init

Creates a participant in a conversation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(name: String, handle: String, isUser: Bool)
```

## Parameters

- `name`: The participant’s display name, for example, Juan Chavez.
- `handle`: A unique identifier for the participant, like an email address or phone number.
- `isUser`: A Boolean value that indicates whether the participant is the user of this device. Set `isUser` to `true` for the participant whose identity matches the user signed in to your app on this device, and `false` for every other participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/suggestedactions/suggestedactionsmessage/participant/init(name:handle:isuser:))*