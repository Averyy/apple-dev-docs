# setCursorFor(_:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Sets the type of mouse cursor according to the type of area the mouse cursor is over.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setCursorFor(_ area: PDFAreaOfInterest)
```

```objc
- (void) setCursorForAreaOfInterest:(PDFAreaOfInterest) area;
```

## Discussion

This method is especially useful for custom subclasses of the `PDFView` class.

## See Also

### Working with Mouse Position and Events
- [func areaOfInterest(forMouse: UIEvent) -> PDFAreaOfInterest](./areaofinterest%28formouse%29.md)
  Returns the type of area the mouse cursor is over.
- [func areaOfInterest(for: CGPoint) -> PDFAreaOfInterest](./areaofinterest%28for%29.md)
  Returns the type of area for a specific cursor location point.
- [struct PDFAreaOfInterest](../pdfareaofinterest.md)
  The mouse position over PDF view areas.
- [func perform(PDFAction)](./perform%28_%29.md)
  Performs the specified action.
- [Drag Operations](../drag-operations.md)
  Define drag operations allowed for a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/setcursorfor(_:))*