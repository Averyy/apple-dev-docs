# speechSpellsOutCharacters(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets whether VoiceOver should speak the contents of the text view character by character.

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
func speechSpellsOutCharacters(_ value: Bool = true) -> Text
```

#### Discussion

Use this modifier when you want VoiceOver to speak text as individual letters, character by character. This is important for text that is not meant to be spoken together, like:

- An acronym that isn’t a word, like APPL, spoken as “A-P-P-L”.
- A number representing a series of digits, like 25, spoken as “two-five” rather than “twenty-five”.

## Parameters

- `value`: A Boolean value that when   indicates   VoiceOver should speak text as individual characters. Defaults   to  .

## See Also

- [func speechAdjustedPitch(Double) -> Text](text/speechadjustedpitch(_:).md)
  Raises or lowers the pitch of spoken text.
- [func speechAlwaysIncludesPunctuation(Bool) -> Text](text/speechalwaysincludespunctuation(_:).md)
  Sets whether VoiceOver should always speak all punctuation in the text view.
- [func speechAnnouncementsQueued(Bool) -> Text](text/speechannouncementsqueued(_:).md)
  Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/speechspellsoutcharacters(_:))*