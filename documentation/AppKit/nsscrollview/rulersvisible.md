# rulersVisible

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the scroll view displays its rulers.

**Availability**:
- macOS

## Declaration

```swift
var rulersVisible: Bool { get set }
```

```objc
@property BOOL rulersVisible;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the scroll view displays its rulers (creating them if needed). When the value of this property is [`false`](../../Swift/false.md), the scroll view doesn’t display its rulers.

## See Also

### Managing Rulers
- [class var rulerViewClass: AnyClass!](./rulerviewclass.md)
  Returns the default class to be used for ruler objects in NSScrollViews.
- [var hasHorizontalRuler: Bool](./hashorizontalruler.md)
  A Boolean that indicates whether the scroll view keeps a horizontal ruler object.
- [var horizontalRulerView: NSRulerView?](./horizontalrulerview.md)
  The scroll view’s horizontal ruler view.
- [var hasVerticalRuler: Bool](./hasverticalruler.md)
  A Boolean that indicates whether the scroll view keeps a vertical ruler object.
- [var verticalRulerView: NSRulerView?](./verticalrulerview.md)
  The scroll view’s vertical ruler view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/rulersvisible)*