# backgroundColor

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

The view’s background color.

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
var backgroundColor: UIColor { get set }
```

*macOS*

```swift
var backgroundColor: NSColor { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, strong) UIColor * backgroundColor;
```

*macOS*

```objc
@property (nonatomic, strong) NSColor * backgroundColor;
```

#### Discussion

A view’s background is the area displayed to either side of a PDF document’s pages. The background also appears between pages when page breaks are enabled. The default color is a 50% gray.

## See Also

### Setting Background Color
- [func takeBackgroundColorFrom(Any)](./takebackgroundcolorfrom%28_%29.md)
  Sets the view’s background color to the specified color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/backgroundcolor)*