# printFormatter

**Framework**: UIKit  
**Kind**: property

An object that lays out the content of pages according to the kind of content.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var printFormatter: UIPrintFormatter? { get set }
```

#### Discussion

Assign to this property an instance of one of the concrete subclasses of [`UIPrintFormatter`](uiprintformatter.md): [`UISimpleTextPrintFormatter`](uisimpletextprintformatter.md), [`UIMarkupTextPrintFormatter`](uimarkuptextprintformatter.md), and [`UIViewPrintFormatter`](uiviewprintformatter.md). This object is released at the end of the print job.

If you set this property, `UIPrintInteractionController` sets the [`printingItems`](uiprintinteractioncontroller/printingitems.md), [`printingItem`](uiprintinteractioncontroller/printingitem.md), and [`printPageRenderer`](uiprintinteractioncontroller/printpagerenderer.md) properties to `nil`. (Only one of these properties can be set for a print job.)

If this property is set and the [`showsPageRange`](uiprintinteractioncontroller/showspagerange.md) property is set to [`true`](https://developer.apple.com/documentation/swift/true)—and if the formatter represents content of more than one page—the printing options include the control for selecting a page range.

## See Also

- [var printingItem: Any?](uiprintinteractioncontroller/printingitem.md)
  A single ready-to-print object.
- [var printingItems: [Any]?](uiprintinteractioncontroller/printingitems.md)
  An array of ready-to-print objects.
- [var printPageRenderer: UIPrintPageRenderer?](uiprintinteractioncontroller/printpagerenderer.md)
  An object that draws pages of printable content when UIKit requests it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printformatter)*