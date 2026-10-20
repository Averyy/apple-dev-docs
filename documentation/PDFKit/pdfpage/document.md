# document

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns the `PDFDocument` object with which the page is associated.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
weak var document: PDFDocument? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) PDFDocument * document;
```

## See Also

### Getting Information About a Page
- [var label: String?](./label.md)
  Returns the label for the page.
- [func bounds(for: PDFDisplayBox) -> CGRect](./bounds%28for%29.md)
  Returns the bounds for the specified PDF display box.
- [func setBounds(CGRect, for: PDFDisplayBox)](./setbounds%28_,for%29.md)
  Sets the bounds for the specified box.
- [var rotation: Int](./rotation.md)
  Sets the rotation angle for the page in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/document)*