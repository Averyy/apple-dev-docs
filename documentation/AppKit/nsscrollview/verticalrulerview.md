# verticalRulerView

**Framework**: AppKit  
**Kind**: property

The scroll view’s vertical ruler view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var verticalRulerView: NSRulerView? { get set }
```

#### Discussion

The value of this property is `nil` when the scroll view has no vertical ruler view.

If the scroll view is set to display a vertical ruler view and doesn’t yet have one, this property creates an instance of the ruler view class set using the class method `setRulerViewClass(_:)`. You can use this property to override the default ruler class set using the class method `setRulerViewClass(_:)`.

Display of rulers is controlled using the [`rulersVisible`](nsscrollview/rulersvisible.md) property.

## See Also

- [class var rulerViewClass: AnyClass!](nsscrollview/rulerviewclass.md)
  Returns the default class to be used for ruler objects in NSScrollViews.
- [var hasHorizontalRuler: Bool](nsscrollview/hashorizontalruler.md)
  A Boolean that indicates whether the scroll view keeps a horizontal ruler object.
- [var horizontalRulerView: NSRulerView?](nsscrollview/horizontalrulerview.md)
  The scroll view’s horizontal ruler view.
- [var hasVerticalRuler: Bool](nsscrollview/hasverticalruler.md)
  A Boolean that indicates whether the scroll view keeps a vertical ruler object.
- [var rulersVisible: Bool](nsscrollview/rulersvisible.md)
  A Boolean that indicates whether the scroll view displays its rulers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/verticalrulerview)*