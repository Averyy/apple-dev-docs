# selectionForLine(at:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the whole line of text that includes the specified point.

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
func selectionForLine(at point: CGPoint) -> PDFSelection?
```

*macOS*

```swift
func selectionForLine(at point: NSPoint) -> PDFSelection?
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (PDFSelection *) selectionForLineAtPoint:(CGPoint) point;
```

*macOS*

```objc
- (PDFSelection *) selectionForLineAtPoint:(NSPoint) point;
```

## Discussion

Returns `NULL` if no line of text contains `point`.

Use this method to respond to a triple-click.

## See Also

### Working with Selections
- [func selection(for: CGRect) -> PDFSelection?](./selection%28for%29-2ckpi.md)
  Returns the text enclosed within the specified rectangle, expressed in page (user) coordinates.
- [func selectionForWord(at: CGPoint) -> PDFSelection?](./selectionforword%28at%29.md)
  Returns the whole word that includes the specified point.
- [func selection(from: CGPoint, to: CGPoint) -> PDFSelection?](./selection%28from,to%29.md)
  Returns the text between the two specified points in page space.
- [func selection(for: NSRange) -> PDFSelection?](./selection%28for%29-20y9d.md)
  Returns the text contained within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/selectionforline(at:))*