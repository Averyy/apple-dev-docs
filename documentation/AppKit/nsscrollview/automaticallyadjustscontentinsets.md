# automaticallyAdjustsContentInsets

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the scroll view automatically adjusts its content insets.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var automaticallyAdjustsContentInsets: Bool { get set }
```

```objc
@property BOOL automaticallyAdjustsContentInsets;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the scroll view automatically sets its [`contentInsets`](./contentinsets.md) property to account for any overlapping title or tool bar. To overlap with the title or tool bar, the window style mask must include `NSFullSizeContentViewWindowMask` and the title bar must not be transparent.

The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Managing Insets
- [var contentInsets: NSEdgeInsets](./contentinsets.md)
  The distance that the scroll view’s subviews are inset from the enclosing scroll view during tiling.
- [var scrollerInsets: NSEdgeInsets](./scrollerinsets.md)
  The distance the scrollers are inset from the edge of the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/automaticallyadjustscontentinsets)*