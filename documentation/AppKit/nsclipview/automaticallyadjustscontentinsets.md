# automaticallyAdjustsContentInsets

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates if the clip view automatically accounts for other scroll view subviews.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var automaticallyAdjustsContentInsets: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), and the clip view is used as the [`contentView`](nsscrollview/contentview.md) of an [`NSScrollView`](nsscrollview.md), the clip view automatically accounts for other scroll view subviews, such as rulers and headers. The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var contentInsets: NSEdgeInsets](nsclipview/contentinsets.md)
  The distance that the content view is inset from the enclosing scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/automaticallyadjustscontentinsets)*