# setIsPaneSplitter:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the type of splitter.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: This functionality is no longer relevant and there is no alternative method.

## Declaration

```objc
- (void) setIsPaneSplitter:(BOOL) flag;
```

## Parameters

- `flag`: [`true`](../../Swift/true.md) if the receiver’s splitter is a bar that goes across the split view. [`false`](../../Swift/false.md) if the splitter is a thumb on the regular background pattern.

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
- [- isPaneSplitter](./ispanesplitter.md)
  The type of pane splitter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/setispanesplitter:)*