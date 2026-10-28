# mouseUpAction

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

The action to perform when a user releases the mouse button within an annotation.

**Availability**:
- macOS 10.5+ - Deprecated in 10.13

## Declaration

```swift
var mouseUpAction: PDFAction? { get set }
```

```objc
@property (nonatomic, strong, nullable) PDFAction * mouseUpAction;
```

## Discussion

The mouse-up action is optional.

## Parameters

- `action`: The PDF action to perform when a user releases the mouse button within an annotation.

## See Also

### Deprecated Properties
- [var toolTip: String?](./tooltip.md)
  Returns text for display as a help tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/mouseupaction)*