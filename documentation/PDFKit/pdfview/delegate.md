# delegate

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

Returns the view’s delegate.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any PDFViewDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<PDFViewDelegate> delegate;
```

## See Also

### Setting the Delegate
- [protocol PDFViewDelegate](../pdfviewdelegate.md)
  The delegate for the `PDFView` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/delegate)*