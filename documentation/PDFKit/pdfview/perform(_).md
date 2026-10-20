# perform(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Performs the specified action.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func perform(_ action: PDFAction)
```

```objc
- (void) performAction:(PDFAction *) action;
```

## See Also

### Working with Mouse Position and Events
- [func areaOfInterest(forMouse: UIEvent) -> PDFAreaOfInterest](./areaofinterest%28formouse%29.md)
  Returns the type of area the mouse cursor is over.
- [func areaOfInterest(for: CGPoint) -> PDFAreaOfInterest](./areaofinterest%28for%29.md)
  Returns the type of area for a specific cursor location point.
- [struct PDFAreaOfInterest](../pdfareaofinterest.md)
  The mouse position over PDF view areas.
- [func setCursorFor(PDFAreaOfInterest)](./setcursorfor%28_%29.md)
  Sets the type of mouse cursor according to the type of area the mouse cursor is over.
- [Drag Operations](../drag-operations.md)
  Define drag operations allowed for a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/perform(_:))*