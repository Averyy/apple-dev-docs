# dashPattern

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Gets the dash pattern for the border as an array of NSNumber objects.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var dashPattern: [Any]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray * dashPattern;
```

#### Discussion

Refer to the description for `NSBezierPath` for more information.

## See Also

### Working with Border Styles and Characteristics
- [var style: PDFBorderStyle](./style.md)
  Sets the border style.
- [enum PDFBorderStyle](../pdfborderstyle.md)
  PDF Kit annotation borders may have the following styles.
- [var lineWidth: CGFloat](./linewidth.md)
  Sets the line width (in points) for the border.
- [var borderKeyValues: [AnyHashable : Any]](./borderkeyvalues.md)
  A dictionary that contains a deep copy of all border properties.
- [struct PDFBorderKey](../pdfborderkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfborder/dashpattern)*