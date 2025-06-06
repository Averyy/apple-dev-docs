# speechAdjustedPitch(_:)

**Framework**: SwiftUI  
**Kind**: method

Raises or lowers the pitch of spoken text.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func speechAdjustedPitch(_ value: Double) -> Text
```

#### Discussion

Use this modifier when you want to change the pitch of spoken text. The value indicates how much higher or lower to change the pitch.

## Parameters

- `value`: The amount to raise or lower the pitch.   Values between   and   result in a lower pitch while   values between   and   result in a higher pitch.   The method clamps values to the range   to  .

## See Also

- [func speechAlwaysIncludesPunctuation(Bool) -> Text](text/speechalwaysincludespunctuation(_:).md)
  Sets whether VoiceOver should always speak all punctuation in the text view.
- [func speechAnnouncementsQueued(Bool) -> Text](text/speechannouncementsqueued(_:).md)
  Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [func speechSpellsOutCharacters(Bool) -> Text](text/speechspellsoutcharacters(_:).md)
  Sets whether VoiceOver should speak the contents of the text view character by character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/speechadjustedpitch(_:))*