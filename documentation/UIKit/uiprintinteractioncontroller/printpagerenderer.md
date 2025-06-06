# printPageRenderer

**Framework**: UIKit  
**Kind**: property

An object that draws pages of printable content when UIKit requests it.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var printPageRenderer: UIPrintPageRenderer? { get set }
```

#### Discussion

The object assigned to this property must be an instance of a custom subclass of [`UIPrintPageRenderer`](uiprintpagerenderer.md). The `UIPrintInteractionController` class retains the page-renderer object and releases it at the end of the print job. The default value is `nil`.

If you set this property, `UIPrintInteractionController` sets the [`printingItems`](uiprintinteractioncontroller/printingitems.md), [`printingItem`](uiprintinteractioncontroller/printingitem.md), [`printFormatter`](uiprintinteractioncontroller/printformatter.md) properties to `nil`. (Only one of these properties can be set for a print job.)

If this property is set and the [`showsPageRange`](uiprintinteractioncontroller/showspagerange.md) property is set to [`true`](https://developer.apple.com/documentation/swift/true)—and the rendered content is greater than one page—the printing options include the control for selecting a page range.

## See Also

- [var printingItem: Any?](uiprintinteractioncontroller/printingitem.md)
  A single ready-to-print object.
- [var printingItems: [Any]?](uiprintinteractioncontroller/printingitems.md)
  An array of ready-to-print objects.
- [var printFormatter: UIPrintFormatter?](uiprintinteractioncontroller/printformatter.md)
  An object that lays out the content of pages according to the kind of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printpagerenderer)*