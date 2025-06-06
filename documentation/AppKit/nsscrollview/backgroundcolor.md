# backgroundColor

**Framework**: AppKit  
**Kind**: property

The color of the content view’s background.

**Availability**:
- macOS ?+

## Declaration

```swift
@NSCopying
@MainActor var backgroundColor: NSColor { get set }
```

#### Discussion

This color is used to paint areas inside the content view that aren’t covered by the document view.

## See Also

- [var backgroundColor: NSColor](nsclipview/backgroundcolor.md)
  The color of the clip view’s background.
- [var drawsBackground: Bool](nsscrollview/drawsbackground.md)
  A Boolean that indicates whether the scroll view draws its background.
- [var borderType: NSBorderType](nsscrollview/bordertype.md)
  A value that specifies the appearance of the scroll view’s border.
- [var documentCursor: NSCursor?](nsscrollview/documentcursor.md)
  The content view’s document cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/backgroundcolor)*