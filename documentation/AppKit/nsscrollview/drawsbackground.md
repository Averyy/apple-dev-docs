# drawsBackground

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the scroll view draws its background.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var drawsBackground: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the scroll view cell fills the background with its background color.

If the scroll view encloses an `NSClipView`, setting this property to [`false`](https://developer.apple.com/documentation/Swift/false) also sets the `NSClipView` property [`copiesOnScroll`](nsclipview/copiesonscroll.md) to [`false`](https://developer.apple.com/documentation/Swift/false). The side effect of setting `drawsBackground` directly on the `NSClipView` instead is the appearance of “trails” (vestiges of previous drawing) in the document view as it is scrolled.

## See Also

- [var drawsBackground: Bool](nsclipview/drawsbackground.md)
  A Boolean value that indicates if the clip view draws its background color.
- [var copiesOnScroll: Bool](nsclipview/copiesonscroll.md)
  A Boolean value that indicates if the clip view copies rendered images while scrolling.
- [var backgroundColor: NSColor](nsscrollview/backgroundcolor.md)
  The color of the content view’s background.
- [var borderType: NSBorderType](nsscrollview/bordertype.md)
  A value that specifies the appearance of the scroll view’s border.
- [var documentCursor: NSCursor?](nsscrollview/documentcursor.md)
  The content view’s document cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/drawsbackground)*