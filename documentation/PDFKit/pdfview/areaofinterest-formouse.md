# areaOfInterest(forMouse:)

**Framework**: PDFKit  
**Kind**: method

Returns the type of area the mouse cursor is over.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func areaOfInterest(forMouse event: UIEvent) -> PDFAreaOfInterest
```

#### Discussion

The `PDFAreaOfInterest` enumeration defines the various area types. This method is for custom subclasses of the `PDFView` class. Use it if you override the `NSResponder` class’s [`mouseMoved(with:)`](https://developer.apple.com/documentation/AppKit/NSResponder/mouseMoved(with:)) method or related methods.

Refer to `Constants` for the various values of the area-of-interest constants. Each of these constants contributes to the value of the `PDFAreaOfInterest` bit field.

## See Also

- [func areaOfInterest(for: CGPoint) -> PDFAreaOfInterest](pdfview/areaofinterest(for:).md)
  Returns the type of area for a specific cursor location point.
- [struct PDFAreaOfInterest](pdfareaofinterest.md)
  The mouse position over PDF view areas.
- [func setCursorFor(PDFAreaOfInterest)](pdfview/setcursorfor(_:).md)
  Sets the type of mouse cursor according to the type of area the mouse cursor is over.
- [func perform(PDFAction)](pdfview/perform(_:).md)
  Performs the specified action.
- [Drag Operations](drag-operations.md)
  Define drag operations allowed for a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/areaofinterest(formouse:))*