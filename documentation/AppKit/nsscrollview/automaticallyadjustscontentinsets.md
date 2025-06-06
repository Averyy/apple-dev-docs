# automaticallyAdjustsContentInsets

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the scroll view automatically adjusts its content insets.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var automaticallyAdjustsContentInsets: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the scroll view automatically sets its [`contentInsets`](nsscrollview/contentinsets.md) property to account for any overlapping title or tool bar. To overlap with the title or tool bar, the window style mask must include `NSFullSizeContentViewWindowMask` and the title bar must not be transparent.

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var contentInsets: NSEdgeInsets](nsscrollview/contentinsets.md)
  The distance that the scroll view’s subviews are inset from the enclosing scroll view during tiling.
- [var scrollerInsets: NSEdgeInsets](nsscrollview/scrollerinsets.md)
  The distance the scrollers are inset from the edge of the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/automaticallyadjustscontentinsets)*