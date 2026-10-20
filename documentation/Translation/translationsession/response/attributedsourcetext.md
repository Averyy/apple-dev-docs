# attributedSourceText

**Framework**: Translation  
**Kind**: property  
**Role**: Instance Property

The original translated text, including style formatting and links.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+

## Declaration

```swift
let attributedSourceText: AttributedString?
```

#### Discussion

When translating attributed strings using any translation method, the framework makes a best effort to preserve both visual formatting and defined attributes. This enables use cases like timestamp synchronization for captions or lyrics. For examples of translating text with preserved attributes, see [`attributedSourceText`](../request/attributedsourcetext.md).

## See Also

### Getting translation results
- [let sourceText: String](./sourcetext.md)
  The original text to translate from.
- [let targetText: String](./targettext.md)
  The translated text.
- [let attributedTargetText: AttributedString?](./attributedtargettext.md)
  The translated formatted text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/response/attributedsourcetext)*