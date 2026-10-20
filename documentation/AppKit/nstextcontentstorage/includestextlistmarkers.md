# includesTextListMarkers

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

When `true`, `NSTextContentStorage` assumes the paragraph with `NSTextList` includes the text list marker string.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var includesTextListMarkers: Bool { get set }
```

```objc
@property BOOL includesTextListMarkers;
```

#### Discussion

Utilizes `NSTextList.includesTextListMarkers` as the default value.

## See Also

### Managing text elements
- [func textElement(for: NSAttributedString) -> NSTextElement?](./textelement%28for%29.md)
  Returns the text element corresponding to object’s attributed string.
- [func attributedString(for: NSTextElement) -> NSAttributedString?](./attributedstring%28for%29.md)
  Returns a new attributed string for the text element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentstorage/includestextlistmarkers)*