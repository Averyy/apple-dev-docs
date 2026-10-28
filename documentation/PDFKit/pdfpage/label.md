# label

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns the label for the page.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * label;
```

## Discussion

Typically, the label is “1” for the first page, “2” for the second page, and so on, but nonnumerical labels are also possible (such as “xxi”, “4-1” and so on).

## See Also

### Getting Information About a Page
- [var document: PDFDocument?](./document.md)
  Returns the `PDFDocument` object with which the page is associated.
- [func bounds(for: PDFDisplayBox) -> CGRect](./bounds%28for%29.md)
  Returns the bounds for the specified PDF display box.
- [func setBounds(CGRect, for: PDFDisplayBox)](./setbounds%28_,for%29.md)
  Sets the bounds for the specified box.
- [var rotation: Int](./rotation.md)
  Sets the rotation angle for the page in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfpage/label)*