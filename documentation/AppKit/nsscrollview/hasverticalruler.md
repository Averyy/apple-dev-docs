# hasVerticalRuler

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the scroll view keeps a vertical ruler object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var hasVerticalRuler: Bool { get set }
```

#### Discussion

When the value of this method is [`true`](https://developer.apple.com/documentation/swift/true), the scroll view allocates a vertical ruler the first time it’s needed.

Display of rulers is controlled using the [`rulersVisible`](nsscrollview/rulersvisible.md) property.

## See Also

- [class var rulerViewClass: AnyClass!](nsscrollview/rulerviewclass.md)
  Returns the default class to be used for ruler objects in NSScrollViews.
- [var hasHorizontalRuler: Bool](nsscrollview/hashorizontalruler.md)
  A Boolean that indicates whether the scroll view keeps a horizontal ruler object.
- [var horizontalRulerView: NSRulerView?](nsscrollview/horizontalrulerview.md)
  The scroll view’s horizontal ruler view.
- [var verticalRulerView: NSRulerView?](nsscrollview/verticalrulerview.md)
  The scroll view’s vertical ruler view.
- [var rulersVisible: Bool](nsscrollview/rulersvisible.md)
  A Boolean that indicates whether the scroll view displays its rulers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/hasverticalruler)*