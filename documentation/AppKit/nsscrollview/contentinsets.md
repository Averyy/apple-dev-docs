# contentInsets

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The distance that the scroll view’s subviews are inset from the enclosing scroll view during tiling.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var contentInsets: NSEdgeInsets { get set }
```

```objc
@property NSEdgeInsets contentInsets;
```

#### Discussion

When the value of this property is equal to `NSEdgeInsetsZero`, traditional tiling is performed. Rulers, headers, and other subviews are tiled with the [`contentView`](./contentview.md) frame filling the remaining space. When the value of this property is not equal to `NSEdgeInsetsZero`, the rulers, headers, and other subviews are inset as specified. The [`contentView`](./contentview.md) is placed underneath these sibling views and is only inset by the scroll view border and non-overlay scrollers.

See [`NSEdgeInsets`](../../Foundation/nsedgeinsets.md) for possible values.

When the value of the [`automaticallyAdjustsContentInsets`](./automaticallyadjustscontentinsets.md) property is [`true`](../../Swift/true.md), any value of this property is overridden during tiling.

## See Also

### Managing Insets
- [var automaticallyAdjustsContentInsets: Bool](./automaticallyadjustscontentinsets.md)
  A Boolean that indicates whether the scroll view automatically adjusts its content insets.
- [var scrollerInsets: NSEdgeInsets](./scrollerinsets.md)
  The distance the scrollers are inset from the edge of the scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/contentinsets)*