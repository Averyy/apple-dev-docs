# speechAlwaysIncludesPunctuation(_:)

**Framework**: Journaling Suggestions  
**Kind**: method

Sets whether VoiceOver should always speak all punctuation in the text view.

**Availability**:
- iOS 15.0+
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

```None
Text("All the world's a stage, " +
     "And all the men and women merely players;")
     .speechAlwaysIncludesPunctuation()
```

VoiceOver would speak “All the world apostrophe s a stage comma and all the men and women merely players semicolon”.

By default, VoiceOver voices punctuation based on surrounding context.

## Parameters

- `value`: A Boolean value that you set to   if   VoiceOver should speak all punctuation in the text. Defaults to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/speechalwaysincludespunctuation(_:))*