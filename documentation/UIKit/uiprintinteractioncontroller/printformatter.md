# printFormatter

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An object that lays out the content of pages according to the kind of content.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var printFormatter: UIPrintFormatter? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIPrintFormatter * printFormatter;
```

## Discussion

Assign to this property an instance of one of the concrete subclasses of [`UIPrintFormatter`](../uiprintformatter.md): [`UISimpleTextPrintFormatter`](../uisimpletextprintformatter.md), [`UIMarkupTextPrintFormatter`](../uimarkuptextprintformatter.md), and [`UIViewPrintFormatter`](../uiviewprintformatter.md). This object is released at the end of the print job.

If you set this property, `UIPrintInteractionController` sets the [`printingItems`](./printingitems.md), [`printingItem`](./printingitem.md), and [`printPageRenderer`](./printpagerenderer.md) properties to `nil`. (Only one of these properties can be set for a print job.)

If this property is set and the [`showsPageRange`](./showspagerange.md) property is set to [`true`](../../Swift/true.md)—and if the formatter represents content of more than one page—the printing options include the control for selecting a page range.

## See Also

### Providing the source of printable content
- [var printingItem: Any?](./printingitem.md)
  A single ready-to-print object.
- [var printingItems: [Any]?](./printingitems.md)
  An array of ready-to-print objects.
- [var printPageRenderer: UIPrintPageRenderer?](./printpagerenderer.md)
  An object that draws pages of printable content when UIKit requests it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printformatter)*