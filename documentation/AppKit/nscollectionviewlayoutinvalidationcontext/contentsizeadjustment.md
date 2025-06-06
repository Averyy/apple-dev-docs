# contentSizeAdjustment

**Framework**: AppKit  
**Kind**: property

The delta value to add to the collection view’s content size.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var contentSizeAdjustment: NSSize { get set }
```

#### Discussion

Use this property to update the size of the collection view’s content area, as computed by the associated layout object. The default value of this property is [`NSZeroSize`](https://developer.apple.com/documentation/Foundation/NSZeroSize). Changing the value causes the collection view to add the specified height and width values to its content size. Thus, positive values grow the content area and negative values shrink it. You might add space around the content area to provide a visual buffer for your collection view content.

## See Also

- [var contentOffsetAdjustment: NSPoint](nscollectionviewlayoutinvalidationcontext/contentoffsetadjustment.md)
  The delta value to add to the collection view’s content offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutinvalidationcontext/contentsizeadjustment)*