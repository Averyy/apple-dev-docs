# textElement(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the text element corresponding to object’s attributed string.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func textElement(for attributedString: NSAttributedString) -> NSTextElement?
```

```objc
- (NSTextElement *) textElementForAttributedString:(NSAttributedString *) attributedString;
```

## Return Value

An [`NSTextElement`](../nstextelement.md), or `nil`.

## Discussion

Returns `nil` when `attributedString` contains attributes not mappable to [`NSTextElement`](../nstextelement.md).

## Parameters

- `attributedString`: The attributed string to map into an [`NSTextElement`](../nstextelement.md).

## See Also

### Managing text elements
- [func attributedString(for: NSTextElement) -> NSAttributedString?](./attributedstring%28for%29.md)
  Returns a new attributed string for the text element.
- [var includesTextListMarkers: Bool](./includestextlistmarkers.md)
  When `true`, `NSTextContentStorage` assumes the paragraph with `NSTextList` includes the text list marker string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentstorage/textelement(for:))*