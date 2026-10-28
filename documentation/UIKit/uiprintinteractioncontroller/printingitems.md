# printingItems

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of ready-to-print objects.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var printingItems: [Any]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray * printingItems;
```

## Discussion

The array must contain [`NSURL`](../../Foundation/nsurl.md), [`NSData`](../../Foundation/nsdata.md), [`UIImage`](../uiimage.md), or [`ALAsset`](../../AssetsLibrary/alasset.md) objects in any combination. Objects of the first two types must reference or contain image data or PDF data. `NSURL` objects must use the `file:` or `assets-library:` scheme or any scheme that can return an [`NSData`](../../Foundation/nsdata.md) object with a registered protocol. Image data (including that encapsulated by [`UIImage`](../uiimage.md) and [`ALAsset`](../../AssetsLibrary/alasset.md) objects) must be in a format supported by the Image I/O framework; see [`UIImage`](../uiimage.md) for more information. An [`ALAsset`](../../AssetsLibrary/alasset.md) object must be of type [`ALAssetTypePhoto`](../../AssetsLibrary/alassettypephoto.md). Items are printed in array-index order. The array is released at the end of the print job. The default value is `nil`.

If you set this property, `UIPrintInteractionController` sets the [`printingItem`](./printingitem.md), [`printPageRenderer`](./printpagerenderer.md), and [`printFormatter`](./printformatter.md) properties to `nil`. (Only one of these properties can be set for a print job.)

If this property is set, the printing options do not include the control for selecting a page range, even if the [`showsPageRange`](./showspagerange.md) property is set to [`true`](../../Swift/true.md). If you want page-range selection, you should use the [`printingItem`](./printingitem.md) property instead.

## See Also

### Providing the source of printable content
- [var printingItem: Any?](./printingitem.md)
  A single ready-to-print object.
- [var printPageRenderer: UIPrintPageRenderer?](./printpagerenderer.md)
  An object that draws pages of printable content when UIKit requests it.
- [var printFormatter: UIPrintFormatter?](./printformatter.md)
  An object that lays out the content of pages according to the kind of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printingitems)*