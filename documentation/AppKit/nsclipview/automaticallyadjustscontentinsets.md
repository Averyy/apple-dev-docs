# automaticallyAdjustsContentInsets

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the clip view automatically accounts for other scroll view subviews.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var automaticallyAdjustsContentInsets: Bool { get set }
```

```objc
@property BOOL automaticallyAdjustsContentInsets;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), and the clip view is used as the [`contentView`](../nsscrollview/contentview.md) of an [`NSScrollView`](../nsscrollview.md), the clip view automatically accounts for other scroll view subviews, such as rulers and headers. The default value is [`true`](../../Swift/true.md).

## See Also

### Accessing the Content Insets
- [var contentInsets: NSEdgeInsets](./contentinsets.md)
  The distance that the content view is inset from the enclosing scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/automaticallyadjustscontentinsets)*