# characterBounds(at:)

**Framework**: PDFKit  
**Kind**: method

Returns the bounds, in page space, of the character at the specified index.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func characterBounds(at index: Int) -> NSRect
```

#### Discussion

In the unlikely event that there is more than one character at the specified index point, only the bounds of the first character is returned.

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page. Note that the bounds returned are not guaranteed to have integer coordinates.

## See Also

- [var numberOfCharacters: Int](pdfpage/numberofcharacters.md)
  Returns the number of characters on the page, including whitespace characters.
- [var string: String?](pdfpage/string.md)
  Returns an `NSString` object representing the text on the page.
- [var attributedString: NSAttributedString?](pdfpage/attributedstring.md)
  Returns an `NSAttributedString` object representing the text on the page.
- [func characterIndex(at: CGPoint) -> Int](pdfpage/characterindex(at:).md)
  Returns the character index value for the specified point in page space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/characterbounds(at:))*