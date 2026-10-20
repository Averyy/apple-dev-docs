# drawsBackground

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the clip view draws its background color.

**Availability**:
- macOS

## Declaration

```swift
var drawsBackground: Bool { get set }
```

```objc
@property BOOL drawsBackground;
```

#### Discussion

If your [`NSClipView`](../nsclipview.md) is enclosed in an [`NSScrollView`](../nsscrollview.md), you should set the [`drawsBackground`](./drawsbackground.md) property on the [`NSScrollView`](../nsscrollview.md). Setting this property to [`false`](../../Swift/false.md) on an [`NSScrollView`](../nsscrollview.md) has the added effect of setting the [`NSClipView`](../nsclipview.md) property [`copiesOnScroll`](./copiesonscroll.md) to [`false`](../../Swift/false.md). The side effect of setting the [`drawsBackground`](./drawsbackground.md) property on the [`NSClipView`](../nsclipview.md) is the appearance of “trails” (vestiges of previous drawing) in the document view as it is scrolled.

## See Also

### Working with Background Color
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The color of the clip view’s background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/drawsbackground)*