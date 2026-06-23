# includesTextListMarkers

**Framework**: AppKit  
**Kind**: property

When `true`, `NSTextContentStorage` assumes the paragraph with `NSTextList` includes the text list marker string.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var includesTextListMarkers: Bool { get set }
```

#### Discussion

Utilizes `NSTextList.includesTextListMarkers` as the default value.

## See Also

- [func textElement(for: NSAttributedString) -> NSTextElement?](nstextcontentstorage/textelement(for:).md)
  Returns the text element corresponding to object’s attributed string.
- [func attributedString(for: NSTextElement) -> NSAttributedString?](nstextcontentstorage/attributedstring(for:).md)
  Returns a new attributed string for the text element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentstorage/includestextlistmarkers)*