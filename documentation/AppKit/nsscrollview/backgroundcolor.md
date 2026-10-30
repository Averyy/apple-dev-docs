# backgroundColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The color of the content view’s background.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var backgroundColor: NSColor { get set }
```

```objc
@property (copy) NSColor * backgroundColor;
```

## Discussion

This color is used to paint areas inside the content view that aren’t covered by the document view.

## See Also

### Related Documentation
- [var backgroundColor: NSColor](../nsclipview/backgroundcolor.md)
  The color of the clip view’s background.
### Managing graphics attributes
- [var drawsBackground: Bool](./drawsbackground.md)
  A Boolean that indicates whether the scroll view draws its background.
- [var borderType: NSBorderType](./bordertype.md)
  A value that specifies the appearance of the scroll view’s border.
- [var documentCursor: NSCursor?](./documentcursor.md)
  The content view’s document cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/backgroundcolor)*