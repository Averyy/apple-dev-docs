# attributedString(for:)

**Framework**: AppKit  
**Kind**: method

Returns a new attributed string for the text element.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func attributedString(for textElement: NSTextElement) -> NSAttributedString?
```

#### Return Value

An [`NSAttributedString`](https://developer.apple.com/documentation/foundation/nsattributedstring), or `nil`.

#### Discussion

Returns `nil` if the method can’t map `textElement` to an [`NSAttributedString`](https://developer.apple.com/documentation/foundation/nsattributedstring).

## Parameters

- `textElement`: The [`NSTextElement`](nstextelement.md) to map into an attributed string.

## See Also

- [func textElement(for: NSAttributedString) -> NSTextElement?](nstextcontentstorage/textelement(for:).md)
  Returns the text element corresponding to object’s attributed string.
- [var includesTextListMarkers: Bool](nstextcontentstorage/includestextlistmarkers.md)
  When `true`, `NSTextContentStorage` assumes the paragraph with `NSTextList` includes the text list marker string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentstorage/attributedstring(for:))*