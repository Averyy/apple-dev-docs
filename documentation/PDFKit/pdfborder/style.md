# style

**Framework**: PDFKit  
**Kind**: property

Sets the border style.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var style: PDFBorderStyle { get set }
```

#### Discussion

Refer to `Constants` for the available border styles.

## See Also

- [enum PDFBorderStyle](pdfborderstyle.md)
  PDF Kit annotation borders may have the following styles.
- [var lineWidth: CGFloat](pdfborder/linewidth.md)
  Sets the line width (in points) for the border.
- [var dashPattern: [Any]?](pdfborder/dashpattern.md)
  Gets the dash pattern for the border as an array of NSNumber objects.
- [var borderKeyValues: [AnyHashable : Any]](pdfborder/borderkeyvalues.md)
  A dictionary that contains a deep copy of all border properties.
- [struct PDFBorderKey](pdfborderkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfborder/style)*