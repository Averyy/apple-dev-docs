# isPaneSplitter

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The type of pane splitter.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: This functionality is no longer relevant and there is no alternative method.

## Declaration

```objc
- (BOOL) isPaneSplitter;
```

#### Return Value

[`true`](../../Swift/true.md) if the split view’s splitter is a bar that goes across the split view; [`false`](../../Swift/false.md) if the splitter is a thumb on the regular background pattern.

## See Also

### Configuring and Drawing Dividers
- [var dividerStyle: NSSplitView.DividerStyle](./dividerstyle-swift.property.md)
  The style of divider between views.
- [NSSplitView.DividerStyle](./dividerstyle-swift.enum.md)
  Constants that specify the style of the split view’s dividers.
- [var dividerColor: NSColor](./dividercolor.md)
  The color of the dividers that the split view draws between subviews.
- [var dividerThickness: CGFloat](./dividerthickness.md)
  The thickness of the dividers for the split view.
- [func drawDivider(in: NSRect)](./drawdivider%28in%29.md)
  Draws a divider between two of the split view’s subviews.
- [- setIsPaneSplitter:](./setispanesplitter_.md)
  Sets the type of splitter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/ispanesplitter)*