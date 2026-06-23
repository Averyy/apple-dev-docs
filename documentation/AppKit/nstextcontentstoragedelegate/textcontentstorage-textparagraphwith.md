# textContentStorage(_:textParagraphWith:)

**Framework**: AppKit  
**Kind**: method

Returns a custom `NSTextParagraph` for the specified range in the content storage’s attributed string.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func textContentStorage(_ textContentStorage: NSTextContentStorage, textParagraphWith range: NSRange) -> NSTextParagraph?
```

#### Return Value

A new [`NSTextParagraph`](nstextparagraph.md), or `nil`.

#### Discussion

When non-nil, `textContentStorage` uses the text paragraph instead of creating the standard [`NSTextParagraph`](nstextparagraph.md) with the attributed substring in range. The attributed string for a custom text paragraph must have `range.length`.

Returns a custom paragraph for a range that you provide from the object’s attributed string.

#### Discussion

When non-`nil`, `textContentStorage` uses the text paragraph instead of creating the standard [`NSTextParagraph`](nstextparagraph.md) with the attributed substring in range. The attributed string for a custom text paragraph must have a length of `range.length`.

## Parameters

- `textContentStorage`: The object’s content manager.
- `range`: The [`NSRange`](https://developer.apple.com/documentation/Foundation/NSRange-c.struct) that describes the extent of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentstoragedelegate/textcontentstorage(_:textparagraphwith:))*