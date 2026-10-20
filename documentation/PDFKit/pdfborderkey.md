# PDFBorderKey

**Framework**: PDFKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
struct PDFBorderKey
```

```c
typedef NSString * const PDFBorderKey;
```

## Topics

### Initializers
- [init(rawValue: String)](./pdfborderkey/init%28rawvalue%29.md)
### Type Properties
- [static let dashPattern: PDFBorderKey](./pdfborderkey/dashpattern.md)
- [static let lineWidth: PDFBorderKey](./pdfborderkey/linewidth.md)
- [static let style: PDFBorderKey](./pdfborderkey/style.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Working with Border Styles and Characteristics
- [var style: PDFBorderStyle](./pdfborder/style.md)
  Sets the border style.
- [enum PDFBorderStyle](./pdfborderstyle.md)
  PDF Kit annotation borders may have the following styles.
- [var lineWidth: CGFloat](./pdfborder/linewidth.md)
  Sets the line width (in points) for the border.
- [var dashPattern: [Any]?](./pdfborder/dashpattern.md)
  Gets the dash pattern for the border as an array of NSNumber objects.
- [var borderKeyValues: [AnyHashable : Any]](./pdfborder/borderkeyvalues.md)
  A dictionary that contains a deep copy of all border properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfborderkey)*