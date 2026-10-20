# string

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns an `NSString` object representing the text on the page.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var string: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * string;
```

## See Also

### Working with Textual Content
- [var numberOfCharacters: Int](./numberofcharacters.md)
  Returns the number of characters on the page, including whitespace characters.
- [var attributedString: NSAttributedString?](./attributedstring.md)
  Returns an `NSAttributedString` object representing the text on the page.
- [func characterBounds(at: Int) -> CGRect](./characterbounds%28at%29.md)
  Returns the bounds, in page space, of the character at the specified index.
- [func characterIndex(at: CGPoint) -> Int](./characterindex%28at%29.md)
  Returns the character index value for the specified point in page space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/string)*