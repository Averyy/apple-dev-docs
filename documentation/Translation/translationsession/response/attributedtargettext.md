# attributedTargetText

**Framework**: Translation  
**Kind**: property

The translated formatted text.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+

## Declaration

```swift
let attributedTargetText: AttributedString?
```

#### Discussion

This property contains the translated text with formatting and defined attributes preserved and aligned from the source text.

The framework makes a best effort to preserve attributes like accessibility instructions and time ranges, aligning them to the corresponding words in the target language.

> **Note**: The framework preserves but doesn’t modify attributes. To use the correct language after translation, update any attributes that need to reflect the target language, such as the language modifier for VoiceOver.

For examples of translating attributed source text, see [`attributedSourceText`](translationsession/request/attributedsourcetext.md).

## See Also

- [let sourceText: String](translationsession/response/sourcetext.md)
  The original text to translate from.
- [let targetText: String](translationsession/response/targettext.md)
  The translated text.
- [let attributedSourceText: AttributedString?](translationsession/response/attributedsourcetext.md)
  The original translated text, including style formatting and links.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/response/attributedtargettext)*