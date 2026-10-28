# printPageRenderer

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An object that draws pages of printable content when UIKit requests it.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var printPageRenderer: UIPrintPageRenderer? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIPrintPageRenderer * printPageRenderer;
```

## Discussion

The object assigned to this property must be an instance of a custom subclass of [`UIPrintPageRenderer`](../uiprintpagerenderer.md). The `UIPrintInteractionController` class retains the page-renderer object and releases it at the end of the print job. The default value is `nil`.

If you set this property, `UIPrintInteractionController` sets the [`printingItems`](./printingitems.md), [`printingItem`](./printingitem.md), [`printFormatter`](./printformatter.md) properties to `nil`. (Only one of these properties can be set for a print job.)

If this property is set and the [`showsPageRange`](./showspagerange.md) property is set to [`true`](../../Swift/true.md)—and the rendered content is greater than one page—the printing options include the control for selecting a page range.

## See Also

### Providing the source of printable content
- [var printingItem: Any?](./printingitem.md)
  A single ready-to-print object.
- [var printingItems: [Any]?](./printingitems.md)
  An array of ready-to-print objects.
- [var printFormatter: UIPrintFormatter?](./printformatter.md)
  An object that lays out the content of pages according to the kind of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printpagerenderer)*