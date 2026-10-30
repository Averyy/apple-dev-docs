# hasVerticalRuler

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the scroll view keeps a vertical ruler object.

**Availability**:
- macOS

## Declaration

```swift
var hasVerticalRuler: Bool { get set }
```

```objc
@property BOOL hasVerticalRuler;
```

## Discussion

When the value of this method is [`true`](../../Swift/true.md), the scroll view allocates a vertical ruler the first time it’s needed.

Display of rulers is controlled using the [`rulersVisible`](./rulersvisible.md) property.

## See Also

### Managing rulers
- [class var rulerViewClass: AnyClass!](./rulerviewclass.md)
  Returns the default class to be used for ruler objects in NSScrollViews.
- [var hasHorizontalRuler: Bool](./hashorizontalruler.md)
  A Boolean that indicates whether the scroll view keeps a horizontal ruler object.
- [var horizontalRulerView: NSRulerView?](./horizontalrulerview.md)
  The scroll view’s horizontal ruler view.
- [var verticalRulerView: NSRulerView?](./verticalrulerview.md)
  The scroll view’s vertical ruler view.
- [var rulersVisible: Bool](./rulersvisible.md)
  A Boolean that indicates whether the scroll view displays its rulers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/hasverticalruler)*