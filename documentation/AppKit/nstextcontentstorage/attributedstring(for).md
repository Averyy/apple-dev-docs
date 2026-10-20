# attributedString(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a new attributed string for the text element.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func attributedString(for textElement: NSTextElement) -> NSAttributedString?
```

```objc
- (NSAttributedString *) attributedStringForTextElement:(NSTextElement *) textElement;
```

#### Return Value

An [`NSAttributedString`](../../Foundation/nsattributedstring.md), or `nil`.

#### Discussion

Returns `nil` if the method can’t map `textElement` to an [`NSAttributedString`](../../Foundation/nsattributedstring.md).

## Parameters

- `textElement`: The [`NSTextElement`](../nstextelement.md) to map into an attributed string.

## See Also

### Managing text elements
- [func textElement(for: NSAttributedString) -> NSTextElement?](./textelement%28for%29.md)
  Returns the text element corresponding to object’s attributed string.
- [var includesTextListMarkers: Bool](./includestextlistmarkers.md)
  When `true`, `NSTextContentStorage` assumes the paragraph with `NSTextList` includes the text list marker string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentstorage/attributedstring(for:))*