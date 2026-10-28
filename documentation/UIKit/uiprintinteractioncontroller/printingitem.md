# printingItem

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A single ready-to-print object.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var printingItem: Any? { get set }
```

```objc
@property (nonatomic, copy, nullable) id printingItem;
```

## Discussion

The object must be an instance of the [`NSURL`](../../Foundation/nsurl.md), [`NSData`](../../Foundation/nsdata.md), or [`UIImage`](../uiimage.md) class. An object of the first two types must reference or contain image data or PDF data. `NSURL` objects must use the `file:` or any scheme that can return an [`NSData`](../../Foundation/nsdata.md) object with a registered protocol. Image data (including that encapsulated by [`UIImage`](../uiimage.md)) must be in a format supported by the Image I/O framework; see [`UIImage`](../uiimage.md) for more information. The object is released at the end of the print job. The default value is `nil`.

If you set this property, `UIPrintInteractionController` sets the [`printingItems`](./printingitems.md), [`printPageRenderer`](./printpagerenderer.md), and [`printFormatter`](./printformatter.md) properties to `nil`. (You can only set one of these properties for a print job).

If this property is set and the [`showsPageRange`](./showspagerange.md) property is set to [`true`](../../Swift/true.md)—and the printing item is a PDF document of more than one page—the printing options include the control for selecting a page range.

## See Also

### Providing the source of printable content
- [var printingItems: [Any]?](./printingitems.md)
  An array of ready-to-print objects.
- [var printPageRenderer: UIPrintPageRenderer?](./printpagerenderer.md)
  An object that draws pages of printable content when UIKit requests it.
- [var printFormatter: UIPrintFormatter?](./printformatter.md)
  An object that lays out the content of pages according to the kind of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printingitem)*