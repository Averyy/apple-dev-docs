# rotation

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Sets the rotation angle for the page in degrees.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var rotation: Int { get set }
```

```objc
@property (nonatomic) NSInteger rotation;
```

#### Discussion

The rotation must be a positive or negative multiple of 90 (negative angles are converted to their positive equivalents; for example, -90 is changed to 270); otherwise this method throws an exception.

## See Also

### Getting Information About a Page
- [var document: PDFDocument?](./document.md)
  Returns the `PDFDocument` object with which the page is associated.
- [var label: String?](./label.md)
  Returns the label for the page.
- [func bounds(for: PDFDisplayBox) -> CGRect](./bounds%28for%29.md)
  Returns the bounds for the specified PDF display box.
- [func setBounds(CGRect, for: PDFDisplayBox)](./setbounds%28_,for%29.md)
  Sets the bounds for the specified box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/rotation)*