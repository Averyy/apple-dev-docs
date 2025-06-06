# drawsBackground

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates if the clip view draws its background color.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var drawsBackground: Bool { get set }
```

#### Discussion

If your [`NSClipView`](nsclipview.md) is enclosed in an [`NSScrollView`](nsscrollview.md), you should set the [`drawsBackground`](nsclipview/drawsbackground.md) property on the [`NSScrollView`](nsscrollview.md). Setting this property to [`false`](https://developer.apple.com/documentation/swift/false) on an [`NSScrollView`](nsscrollview.md) has the added effect of setting the [`NSClipView`](nsclipview.md) property [`copiesOnScroll`](nsclipview/copiesonscroll.md) to [`false`](https://developer.apple.com/documentation/swift/false). The side effect of setting the [`drawsBackground`](nsclipview/drawsbackground.md) property on the [`NSClipView`](nsclipview.md) is the appearance of “trails” (vestiges of previous drawing) in the document view as it is scrolled.

## See Also

- [var backgroundColor: NSColor](nsclipview/backgroundcolor.md)
  The color of the clip view’s background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/drawsbackground)*