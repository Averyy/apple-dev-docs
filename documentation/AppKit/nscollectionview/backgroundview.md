# backgroundView

**Framework**: AppKit  
**Kind**: property

The background view placed behind all items and supplementary views.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var backgroundView: NSView? { get set }
```

#### Discussion

The view you assign to this property is positioned underneath all other content and sized automatically to match the enclosing clip view’s frame. The view itself does not scroll with the rest of the collection view content. The view’s layer redraw policy is also changed to [`NSView.LayerContentsRedrawPolicy.never`](nsview/layercontentsredrawpolicy-swift.enum/never.md).

In macOS 10.12 and later, a collection view that sets both [`backgroundView`](nscollectionview/backgroundview.md) and [`backgroundColors`](nscollectionview/backgroundcolors.md) shows `backgroundColors[0]` through all areas that are not opaquely covered by the [`backgroundView`](nscollectionview/backgroundview.md).

## See Also

- [var delegate: (any NSCollectionViewDelegate)?](nscollectionview/delegate.md)
  The collection view’s delegate object.
- [protocol NSCollectionViewDelegate](nscollectionviewdelegate.md)
  A set of methods that you use to manage the behavior of a collection view.
- [var content: [Any]](nscollectionview/content.md)
  An array that provides data for the collection view.
- [var backgroundColors: [NSColor]!](nscollectionview/backgroundcolors.md)
  An array containing the collection view’s background colors.
- [var backgroundViewScrollsWithContent: Bool](nscollectionview/backgroundviewscrollswithcontent.md)
  A Boolean value that indicates whether the collection view’s background view scrolls with the items and other content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/backgroundview)*