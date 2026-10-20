# areaOfInterest(for:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the type of area for a specific cursor location point.

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
func areaOfInterest(for cursorLocation: CGPoint) -> PDFAreaOfInterest
```

*macOS*

```swift
func areaOfInterest(for cursorLocation: NSPoint) -> PDFAreaOfInterest
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (PDFAreaOfInterest) areaOfInterestForPoint:(CGPoint) cursorLocation;
```

*macOS*

```objc
- (PDFAreaOfInterest) areaOfInterestForPoint:(NSPoint) cursorLocation;
```

## See Also

### Working with Mouse Position and Events
- [func areaOfInterest(forMouse: UIEvent) -> PDFAreaOfInterest](./areaofinterest%28formouse%29.md)
  Returns the type of area the mouse cursor is over.
- [struct PDFAreaOfInterest](../pdfareaofinterest.md)
  The mouse position over PDF view areas.
- [func setCursorFor(PDFAreaOfInterest)](./setcursorfor%28_%29.md)
  Sets the type of mouse cursor according to the type of area the mouse cursor is over.
- [func perform(PDFAction)](./perform%28_%29.md)
  Performs the specified action.
- [Drag Operations](../drag-operations.md)
  Define drag operations allowed for a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/areaofinterest(for:))*