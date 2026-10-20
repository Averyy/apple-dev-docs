# startLineStyle

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

The style of the line annotation’s starting point, such as square or filled arrowhead.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var startLineStyle: PDFLineStyle { get set }
```

```objc
@property (nonatomic) PDFLineStyle startLineStyle;
```

## See Also

### Configuring Line Annotations
- [var startPoint: CGPoint](./startpoint.md)
  The point where a line begins, in annotation-space coordinates.
- [var endPoint: CGPoint](./endpoint.md)
  The point where a line ends, in annotation-space coordinates.
- [var endLineStyle: PDFLineStyle](./endlinestyle.md)
  The style of the line annotation’s ending point, such as square or filled arrowhead.
- [class func lineStyle(fromName: String) -> PDFLineStyle](./linestyle%28fromname%29.md)
  Returns a line style that corresponds to the specified name.
- [class func name(for: PDFLineStyle) -> String](./name%28for%29.md)
  Returns the name of the line style, which matches the definition in the Adobe PDF Specification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/startlinestyle)*