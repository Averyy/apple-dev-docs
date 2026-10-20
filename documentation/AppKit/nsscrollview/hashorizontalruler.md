# hasHorizontalRuler

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the scroll view keeps a horizontal ruler object.

**Availability**:
- macOS

## Declaration

```swift
var hasHorizontalRuler: Bool { get set }
```

```objc
@property BOOL hasHorizontalRuler;
```

#### Discussion

When the value of this method is [`true`](../../Swift/true.md), the scroll view allocates a horizontal ruler the first time it’s needed.

Display of rulers is controlled using the [`rulersVisible`](./rulersvisible.md) property.

## See Also

### Managing Rulers
- [class var rulerViewClass: AnyClass!](./rulerviewclass.md)
  Returns the default class to be used for ruler objects in NSScrollViews.
- [var horizontalRulerView: NSRulerView?](./horizontalrulerview.md)
  The scroll view’s horizontal ruler view.
- [var hasVerticalRuler: Bool](./hasverticalruler.md)
  A Boolean that indicates whether the scroll view keeps a vertical ruler object.
- [var verticalRulerView: NSRulerView?](./verticalrulerview.md)
  The scroll view’s vertical ruler view.
- [var rulersVisible: Bool](./rulersvisible.md)
  A Boolean that indicates whether the scroll view displays its rulers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/hashorizontalruler)*