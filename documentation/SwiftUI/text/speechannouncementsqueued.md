# speechAnnouncementsQueued(_:)

**Framework**: SwiftUI  
**Kind**: method

Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.

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
func speechAnnouncementsQueued(_ value: Bool = true) -> Text
```

#### Discussion

Use this modifier when you want affect the order in which the accessibility system delivers spoken text. Announcements can occur automatically when the label or value of an accessibility element changes.

## Parameters

- `value`: A Boolean value that determines if VoiceOver speaks   changes to text immediately or enqueues them behind existing speech.   Defaults to  .

## See Also

- [func speechAdjustedPitch(Double) -> Text](text/speechadjustedpitch(_:).md)
  Raises or lowers the pitch of spoken text.
- [func speechAlwaysIncludesPunctuation(Bool) -> Text](text/speechalwaysincludespunctuation(_:).md)
  Sets whether VoiceOver should always speak all punctuation in the text view.
- [func speechSpellsOutCharacters(Bool) -> Text](text/speechspellsoutcharacters(_:).md)
  Sets whether VoiceOver should speak the contents of the text view character by character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/speechannouncementsqueued(_:))*