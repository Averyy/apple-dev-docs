# attributedSourceText

**Framework**: Translation  
**Kind**: property

The original translated text, including style formatting and links.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)

## Declaration

```swift
let attributedSourceText: AttributedString?
```

#### Discussion

When translating attributed strings using any translation method, the framework makes a best effort to preserve both visual formatting and defined attributes. This enables use cases like timestamp synchronization for captions or lyrics. For examples of translating text with preserved attributes, see [`attributedSourceText`](translationsession/request/attributedsourcetext.md).

## See Also

- [let sourceText: String](translationsession/response/sourcetext.md)
  The original text to translate from.
- [let targetText: String](translationsession/response/targettext.md)
  The translated text.
- [let attributedTargetText: AttributedString?](translationsession/response/attributedtargettext.md)
  The translated formatted text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/response/attributedsourcetext)*