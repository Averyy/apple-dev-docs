# PDFAreaOfInterest

**Framework**: PDFKit  
**Kind**: struct  
**Role**: Structure

The mouse position over PDF view areas.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct PDFAreaOfInterest
```

```c
enum PDFAreaOfInterest : NSInteger;
```

## Overview

These constants are components of a bit field and may be combined arbitrarily.

## Topics

### Constants
- [static var pageArea: PDFAreaOfInterest](./pdfareaofinterest/pagearea.md)
  The mouse is over a page.
- [static var textArea: PDFAreaOfInterest](./pdfareaofinterest/textarea.md)
  The mouse is over text.
- [static var annotationArea: PDFAreaOfInterest](./pdfareaofinterest/annotationarea.md)
  The mouse is over an annotation.
- [static var linkArea: PDFAreaOfInterest](./pdfareaofinterest/linkarea.md)
  The mouse is over a link.
- [static var controlArea: PDFAreaOfInterest](./pdfareaofinterest/controlarea.md)
  The mouse is over a control.
- [static var textFieldArea: PDFAreaOfInterest](./pdfareaofinterest/textfieldarea.md)
  The mouse is over a text field.
- [static var iconArea: PDFAreaOfInterest](./pdfareaofinterest/iconarea.md)
  The mouse is over an icon.
- [static var popupArea: PDFAreaOfInterest](./pdfareaofinterest/popuparea.md)
  The mouse is over a popup menu.
- [static var imageArea: PDFAreaOfInterest](./pdfareaofinterest/imagearea.md)
  The mouse is over an image.
- [kPDFNoArea](./pdfareaofinterest/kpdfnoarea.md)
  The mouse is over an undefined area.
### Initializers
- [init(rawValue: Int)](./pdfareaofinterest/init%28rawvalue%29.md)
### Type Properties
- [static var anyArea: PDFAreaOfInterest](./pdfareaofinterest/anyarea.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Working with Mouse Position and Events
- [func areaOfInterest(forMouse: UIEvent) -> PDFAreaOfInterest](./pdfview/areaofinterest%28formouse%29.md)
  Returns the type of area the mouse cursor is over.
- [func areaOfInterest(for: CGPoint) -> PDFAreaOfInterest](./pdfview/areaofinterest%28for%29.md)
  Returns the type of area for a specific cursor location point.
- [func setCursorFor(PDFAreaOfInterest)](./pdfview/setcursorfor%28_%29.md)
  Sets the type of mouse cursor according to the type of area the mouse cursor is over.
- [func perform(PDFAction)](./pdfview/perform%28_%29.md)
  Performs the specified action.
- [Drag Operations](./drag-operations.md)
  Define drag operations allowed for a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfareaofinterest)*