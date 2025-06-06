# dividerColor

**Framework**: AppKit  
**Kind**: property

The color of the dividers that the split view draws between subviews.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@NSCopying
@MainActor var dividerColor: NSColor { get }
```

#### Discussion

The default implementation of this method returns [`clear`](nscolor/clear.md) when the split view’s [`dividerStyle`](nssplitview/dividerstyle-swift.property.md) is [`NSSplitView.DividerStyle.thick`](nssplitview/dividerstyle-swift.enum/thick.md), or when [`dividerStyle`](nssplitview/dividerstyle-swift.property.md) is [`NSSplitView.DividerStyle.paneSplitter`](nssplitview/dividerstyle-swift.enum/panesplitter.md) and the split view is in a textured window. The system draws all other thin dividers with a color that provides appropriate contrast between two white panes.

You can subclass [`NSSplitView`](nssplitview.md) and override this method to change the color of dividers.

## See Also

- [var dividerStyle: NSSplitView.DividerStyle](nssplitview/dividerstyle-swift.property.md)
  The style of divider between views.
- [NSSplitView.DividerStyle](nssplitview/dividerstyle-swift.enum.md)
  Constants that specify the style of the split view’s dividers.
- [var dividerThickness: CGFloat](nssplitview/dividerthickness.md)
  The thickness of the dividers for the split view.
- [func drawDivider(in: NSRect)](nssplitview/drawdivider(in:).md)
  Draws a divider between two of the split view’s subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/dividercolor)*