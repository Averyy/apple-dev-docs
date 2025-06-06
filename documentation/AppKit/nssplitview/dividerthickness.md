# dividerThickness

**Framework**: AppKit  
**Kind**: property

The thickness of the dividers for the split view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var dividerThickness: CGFloat { get }
```

#### Discussion

You can subclass [`NSSplitView`](nssplitview.md) and override this method to change the thickness of a split view’s dividers.

## See Also

- [var dividerStyle: NSSplitView.DividerStyle](nssplitview/dividerstyle-swift.property.md)
  The style of divider between views.
- [NSSplitView.DividerStyle](nssplitview/dividerstyle-swift.enum.md)
  Constants that specify the style of the split view’s dividers.
- [var dividerColor: NSColor](nssplitview/dividercolor.md)
  The color of the dividers that the split view draws between subviews.
- [func drawDivider(in: NSRect)](nssplitview/drawdivider(in:).md)
  Draws a divider between two of the split view’s subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/dividerthickness)*