# PDFDestination

**Framework**: PDFKit  
**Kind**: class

A `PDFDestination` object describes a point on a PDF page.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PDFDestination
```

#### Overview

In typical usage, you do not initialize `PDFDestination` objects but rather get them as either attributes of [`PDFAnnotationLink`](pdfannotationlink.md) or [`PDFOutline`](pdfoutline.md) objects, or in response to the `PDFView` method [`currentDestination`](pdfview/currentdestination.md).

## Topics

### Initializing a Destination
- [init(page: PDFPage, at: CGPoint)](pdfdestination/init(page:at:).md)
  Initializes the destination.
### Getting Pages and Points
- [var page: PDFPage?](pdfdestination/page.md)
  Returns the page that the destination refers to.
- [var point: CGPoint](pdfdestination/point.md)
  Returns the point, in page space, that the destination refers to.
- [let kPDFDestinationUnspecifiedValue: CGFloat](kpdfdestinationunspecifiedvalue.md)
### Getting a Relative Location
- [func compare(PDFDestination) -> ComparisonResult](pdfdestination/compare(_:).md)
  Returns a comparison result that indicates the location of the destination in the document, relative to the current position.
### Instance Properties
- [var zoom: CGFloat](pdfdestination/zoom.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var page: PDFPage?](pdfannotation/page.md)
  Returns the page that the annotation is associated with.
- [var modificationDate: Date?](pdfannotation/modificationdate.md)
  Returns the modification date of the annotation.
- [var userName: String?](pdfannotation/username.md)
  Returns the name of the user who created the annotation.
- [var type: String?](pdfannotation/type.md)
  Returns the type of the annotation.
- [var action: PDFAction?](pdfannotation/action.md)
  An object that represents an action for a PDF element, such as a link annotation.
- [class PDFAction](pdfaction.md)
  An action that is performed when, for example, a PDF annotation is activated or an outline item is clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdestination)*