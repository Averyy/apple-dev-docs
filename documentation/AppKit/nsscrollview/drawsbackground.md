# drawsBackground

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the scroll view draws its background.

**Availability**:
- macOS

## Declaration

```swift
var drawsBackground: Bool { get set }
```

```objc
@property BOOL drawsBackground;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the scroll view cell fills the background with its background color.

If the scroll view encloses an `NSClipView`, setting this property to [`false`](../../Swift/false.md) also sets the `NSClipView` property [`copiesOnScroll`](../nsclipview/copiesonscroll.md) to [`false`](../../Swift/false.md). The side effect of setting `drawsBackground` directly on the `NSClipView` instead is the appearance of “trails” (vestiges of previous drawing) in the document view as it is scrolled.

## See Also

### Related Documentation
- [var drawsBackground: Bool](../nsclipview/drawsbackground.md)
  A Boolean value that indicates if the clip view draws its background color.
- [var copiesOnScroll: Bool](../nsclipview/copiesonscroll.md)
  A Boolean value that indicates if the clip view copies rendered images while scrolling.
### Managing Graphics Attributes
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The color of the content view’s background.
- [var borderType: NSBorderType](./bordertype.md)
  A value that specifies the appearance of the scroll view’s border.
- [var documentCursor: NSCursor?](./documentcursor.md)
  The content view’s document cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/drawsbackground)*