# speechAlwaysIncludesPunctuation(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets whether VoiceOver should always speak all punctuation in the text view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func speechAlwaysIncludesPunctuation(_ value: Bool = true) -> some View
```

#### Discussion

Use this modifier to control whether the system speaks punctuation characters in the text. You might use this for code or other text where the punctuation is relevant, or where you want VoiceOver to speak a verbatim transcription of the text you provide. For example, given the text:

```swift
Text("All the world's a stage, " +
     "And all the men and women merely players;")
     .speechAlwaysIncludesPunctuation()
```

VoiceOver would speak “All the world apostrophe s a stage comma and all the men and women merely players semicolon”.

By default, VoiceOver voices punctuation based on surrounding context.

## Parameters

- `value`: A Boolean value that you set to   if   VoiceOver should speak all punctuation in the text. Defaults to  .

## See Also

- [func speechAdjustedPitch(Double) -> some View](familyactivitypicker/speechadjustedpitch(_:).md)
  Raises or lowers the pitch of spoken text.
- [func speechAnnouncementsQueued(Bool) -> some View](familyactivitypicker/speechannouncementsqueued(_:).md)
  Controls whether to queue pending announcements behind existing speech rather than interrupting speech in progress.
- [func speechSpellsOutCharacters(Bool) -> some View](familyactivitypicker/speechspellsoutcharacters(_:).md)
  Sets whether VoiceOver should speak the contents of the text view character by character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/speechalwaysincludespunctuation(_:))*