# speechSpellsOutCharacters(_:)

**Framework**: PermissionKit  
**Kind**: method

Sets whether VoiceOver should speak the contents of the text view character by character.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 26.0+ (Beta)
- watchOS 8.0+

## Declaration

```swift
nonisolated
func speechSpellsOutCharacters(_ value: Bool = true) -> some View
```

#### Discussion

Use this modifier when you want VoiceOver to speak text as individual letters, character by character. This is important for text that is not meant to be spoken together, like:

- An acronym that isn’t a word, like APPL, spoken as “A-P-P-L”.
- A number representing a series of digits, like 25, spoken as “two-five” rather than “twenty-five”.

## Parameters

- `value`: A Boolean value that when   indicates   VoiceOver should speak text as individual characters. Defaults   to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/speechspellsoutcharacters(_:))*