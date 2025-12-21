# printingItems

**Framework**: UIKit  
**Kind**: property

An array of ready-to-print objects.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var printingItems: [Any]? { get set }
```

#### Discussion

The array must contain [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL), [`NSData`](https://developer.apple.com/documentation/Foundation/NSData), [`UIImage`](uiimage.md), or [`ALAsset`](https://developer.apple.com/documentation/AssetsLibrary/ALAsset) objects in any combination. Objects of the first two types must reference or contain image data or PDF data. `NSURL` objects must use the `file:` or `assets-library:` scheme or any scheme that can return an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object with a registered protocol. Image data (including that encapsulated by [`UIImage`](uiimage.md) and [`ALAsset`](https://developer.apple.com/documentation/AssetsLibrary/ALAsset) objects) must be in a format supported by the Image I/O framework; see [`UIImage`](uiimage.md) for more information. An [`ALAsset`](https://developer.apple.com/documentation/AssetsLibrary/ALAsset) object must be of type [`ALAssetTypePhoto`](https://developer.apple.com/documentation/AssetsLibrary/ALAssetTypePhoto). Items are printed in array-index order. The array is released at the end of the print job. The default value is `nil`.

If you set this property, `UIPrintInteractionController` sets the [`printingItem`](uiprintinteractioncontroller/printingitem.md), [`printPageRenderer`](uiprintinteractioncontroller/printpagerenderer.md), and [`printFormatter`](uiprintinteractioncontroller/printformatter.md) properties to `nil`. (Only one of these properties can be set for a print job.)

If this property is set, the printing options do not include the control for selecting a page range, even if the [`showsPageRange`](uiprintinteractioncontroller/showspagerange.md) property is set to [`true`](https://developer.apple.com/documentation/Swift/true). If you want page-range selection, you should use the [`printingItem`](uiprintinteractioncontroller/printingitem.md) property instead.

## See Also

- [var printingItem: Any?](uiprintinteractioncontroller/printingitem.md)
  A single ready-to-print object.
- [var printPageRenderer: UIPrintPageRenderer?](uiprintinteractioncontroller/printpagerenderer.md)
  An object that draws pages of printable content when UIKit requests it.
- [var printFormatter: UIPrintFormatter?](uiprintinteractioncontroller/printformatter.md)
  An object that lays out the content of pages according to the kind of content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/printingitems)*