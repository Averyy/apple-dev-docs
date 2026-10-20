# PDFBorderStyle

**Framework**: PDFKit  
**Kind**: enum  
**Role**: Enumeration

PDF Kit annotation borders may have the following styles.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum PDFBorderStyle
```

```c
enum PDFBorderStyle : NSInteger;
```

## Topics

### Constants
- [PDFBorderStyle.solid](./pdfborderstyle/solid.md)
  Solid border.
- [PDFBorderStyle.dashed](./pdfborderstyle/dashed.md)
  Dashed border.
- [PDFBorderStyle.beveled](./pdfborderstyle/beveled.md)
  Beveled border.
- [PDFBorderStyle.inset](./pdfborderstyle/inset.md)
  Inset border.
- [PDFBorderStyle.underline](./pdfborderstyle/underline.md)
  Underline border.
### Initializers
- [init?(rawValue: Int)](./pdfborderstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Working with Border Styles and Characteristics
- [var style: PDFBorderStyle](./pdfborder/style.md)
  Sets the border style.
- [var lineWidth: CGFloat](./pdfborder/linewidth.md)
  Sets the line width (in points) for the border.
- [var dashPattern: [Any]?](./pdfborder/dashpattern.md)
  Gets the dash pattern for the border as an array of NSNumber objects.
- [var borderKeyValues: [AnyHashable : Any]](./pdfborder/borderkeyvalues.md)
  A dictionary that contains a deep copy of all border properties.
- [struct PDFBorderKey](./pdfborderkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfborderstyle)*