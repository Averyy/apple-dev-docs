# rulersVisible

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the scroll view displays its rulers.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var rulersVisible: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the scroll view displays its rulers (creating them if needed). When the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), the scroll view doesn’t display its rulers.

## See Also

- [class var rulerViewClass: AnyClass!](nsscrollview/rulerviewclass.md)
  Returns the default class to be used for ruler objects in NSScrollViews.
- [var hasHorizontalRuler: Bool](nsscrollview/hashorizontalruler.md)
  A Boolean that indicates whether the scroll view keeps a horizontal ruler object.
- [var horizontalRulerView: NSRulerView?](nsscrollview/horizontalrulerview.md)
  The scroll view’s horizontal ruler view.
- [var hasVerticalRuler: Bool](nsscrollview/hasverticalruler.md)
  A Boolean that indicates whether the scroll view keeps a vertical ruler object.
- [var verticalRulerView: NSRulerView?](nsscrollview/verticalrulerview.md)
  The scroll view’s vertical ruler view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/rulersvisible)*