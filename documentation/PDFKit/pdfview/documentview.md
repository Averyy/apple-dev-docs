# documentView

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

The innermost view used by `PDFView` or by your `PDFView` subclass.

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
var documentView: UIView? { get }
```

*macOS*

```swift
var documentView: NSView? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly, nullable) UIView * documentView;
```

*macOS*

```objc
@property (nonatomic, readonly, nullable) NSView * documentView;
```

## Discussion

The innermost view is the one displaying the visible document pages. This method is useful when converting coordinates from one view to another.

## See Also

### Specializing the View
- [func layoutDocumentView()](./layoutdocumentview%28%29.md)
  Performs layout of the inner views.
- [Draw Operations](../draw-operations.md)
  Draw in a PDF page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/documentview)*