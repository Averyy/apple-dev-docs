# characterIndex(at:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the character index value for the specified point in page space.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func characterIndex(at point: CGPoint) -> Int
```

*macOS*

```swift
func characterIndex(at point: NSPoint) -> Int
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (NSInteger) characterIndexAtPoint:(CGPoint) point;
```

*macOS*

```objc
- (NSInteger) characterIndexAtPoint:(NSPoint) point;
```

#### Discussion

If there is no character at the specified point, the method returns `-1`.

Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

### Working with Textual Content
- [var numberOfCharacters: Int](./numberofcharacters.md)
  Returns the number of characters on the page, including whitespace characters.
- [var string: String?](./string.md)
  Returns an `NSString` object representing the text on the page.
- [var attributedString: NSAttributedString?](./attributedstring.md)
  Returns an `NSAttributedString` object representing the text on the page.
- [func characterBounds(at: Int) -> CGRect](./characterbounds%28at%29.md)
  Returns the bounds, in page space, of the character at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/characterindex(at:))*