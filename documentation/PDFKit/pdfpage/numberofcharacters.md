# numberOfCharacters

**Framework**: PDFKit  
**Kind**: property

Returns the number of characters on the page, including whitespace characters.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var numberOfCharacters: Int { get }
```

## See Also

- [var string: String?](pdfpage/string.md)
  Returns an `NSString` object representing the text on the page.
- [var attributedString: NSAttributedString?](pdfpage/attributedstring.md)
  Returns an `NSAttributedString` object representing the text on the page.
- [func characterBounds(at: Int) -> CGRect](pdfpage/characterbounds(at:).md)
  Returns the bounds, in page space, of the character at the specified index.
- [func characterIndex(at: CGPoint) -> Int](pdfpage/characterindex(at:).md)
  Returns the character index value for the specified point in page space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/numberofcharacters)*