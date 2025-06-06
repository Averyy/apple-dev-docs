# printingItem

**Framework**: UIKit  
**Kind**: property

A single ready-to-print object.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var printingItem: Any? { get set }
```

#### Discussion

The object must be an instance of the [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL), [`NSData`](https://developer.apple.com/documentation/Foundation/NSData), or [`UIImage`](uiimage.md) class. An object of the first two types must reference or contain image data or PDF data. `NSURL` objects must use the `file:` or any scheme that can return an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object with a registered protocol. Image data (including that encapsulated by [`UIImage`](uiimage.md)) must be in a format supported by the Image I/O framework; see [`UIImage`](uiimage.md) for more information. The object is released at the end of the print job. The default value is `nil`.

If you set this property, `UIPrintInteractionController` sets the [`printingItems`](uiprintinteractioncontroller/printingitems.md), [`printPageRenderer`](uiprintinteractioncontroller/printpagerenderer.md), and [`printFormatter`](uiprintinteractioncontroller/printformatter.md) properties to `nil`. (You can only set one of these properties for a print job).

If this property is set and the [`showsPageRange`](uiprintinteractioncontroller/showspagerange.md) property is set to [`true`](https://developer.apple.com/documentation/swift/true)—and the printing item is a PDF document of more than one page—the printing options include the control for selecting a page range.

## See Also

- [var printingItems: [Any]?](uiprintinteractioncontroller/printingitems.md)
  An array of ready-to-print objects.
- [var printPageRenderer: UIPrintPageRenderer?](uiprintinteractioncontroller/printpagerenderer.md)
  An object that draws pages of printable content when UIKit requests it.
- [var printFormatter: UIPrintFormatter?](uiprintinteractioncontroller/printformatter.md)
  An object that lays out the content of pages according to the kind of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printingitem)*