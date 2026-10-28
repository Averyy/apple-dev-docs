# go(to:on:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Navigates to the specified rectangle on the specified page.

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
func go(to rect: CGRect, on page: PDFPage)
```

*macOS*

```swift
func go(to rect: NSRect, on page: PDFPage)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (void) goToRect:(CGRect) rect onPage:(PDFPage *) page;
```

*macOS*

```objc
- (void) goToRect:(NSRect) rect onPage:(PDFPage *) page;
```

## Discussion

If the specified rectangle is already visible, this method does nothing. This allows you to scroll the `PDFView` object to a specific [`PDFAnnotation`](../pdfannotation.md) or [`PDFSelection`](../pdfselection.md) object, because both of these objects have bounds methods that return an annotation or selection position in page space.

Note that `rect` is specified in page-space coordinates. Page space is a 72 dpi coordinate system with the origin at the lower-left corner of the current page.

## See Also

### Using Seek in a Document
- [func go(to: PDFPage)](./go%28to%29-6x8y2.md)
  Scrolls to the specified page.
- [func go(to: PDFDestination)](./go%28to%29-5lh5d.md)
  Navigates to the specified destination.
- [func go(to: PDFSelection)](./go%28to%29-3t5go.md)
  Scrolls to the first character of the specified selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/go(to:on:))*