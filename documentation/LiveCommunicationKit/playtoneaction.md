# PlayToneAction

**Framework**: LiveCommunicationKit  
**Kind**: class

Plays a sequence of tones to indicate local or remote member keypad entry.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
final class PlayToneAction
```

## Topics

### Initializers
- [init(conversationUUID: UUID, digits: String, tone: PlayToneAction.Tone)](playtoneaction/init(conversationuuid:digits:tone:).md)
  Creates a new `PlayToneAction`.
### Instance Properties
- [let digits: String](playtoneaction/digits.md)
  The digits tapped by the user into the in-call keypad or included in the dial string.
- [let tone: PlayToneAction.Tone](playtoneaction/tone-swift.property.md)
  The tone to play.
### Enumerations
- [PlayToneAction.Tone](playtoneaction/tone-swift.enum.md)
  The types of tones that may be played.

## Relationships

### Inherits From
- [ConversationAction](conversationaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/playtoneaction)*