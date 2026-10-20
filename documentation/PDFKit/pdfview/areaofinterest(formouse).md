# areaOfInterest(forMouse:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Returns the type of area the mouse cursor is over.

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
func areaOfInterest(forMouse event: UIEvent) -> PDFAreaOfInterest
```

*macOS*

```swift
func areaOfInterest(forMouse event: NSEvent) -> PDFAreaOfInterest
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (PDFAreaOfInterest) areaOfInterestForMouse:(UIEvent *) event;
```

*macOS*

```objc
- (PDFAreaOfInterest) areaOfInterestForMouse:(NSEvent *) event;
```

#### Discussion

The `PDFAreaOfInterest` enumeration defines the various area types. This method is for custom subclasses of the `PDFView` class. Use it if you override the `NSResponder` class’s [`mouseMoved(with:)`](../../AppKit/nsresponder/mousemoved%28with%29.md) method or related methods.

Refer to `Constants` for the various values of the area-of-interest constants. Each of these constants contributes to the value of the `PDFAreaOfInterest` bit field.

## See Also

### Working with Mouse Position and Events
- [func areaOfInterest(for: CGPoint) -> PDFAreaOfInterest](./areaofinterest%28for%29.md)
  Returns the type of area for a specific cursor location point.
- [struct PDFAreaOfInterest](../pdfareaofinterest.md)
  The mouse position over PDF view areas.
- [func setCursorFor(PDFAreaOfInterest)](./setcursorfor%28_%29.md)
  Sets the type of mouse cursor according to the type of area the mouse cursor is over.
- [func perform(PDFAction)](./perform%28_%29.md)
  Performs the specified action.
- [Drag Operations](../drag-operations.md)
  Define drag operations allowed for a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview/areaofinterest(formouse:))*