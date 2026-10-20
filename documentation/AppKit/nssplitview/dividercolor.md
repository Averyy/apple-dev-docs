# dividerColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The color of the dividers that the split view draws between subviews.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@NSCopying
var dividerColor: NSColor { get }
```

```objc
@property (copy, readonly) NSColor * dividerColor;
```

#### Discussion

The default implementation of this method returns [`clear`](../nscolor/clear.md) when the split view’s [`dividerStyle`](./dividerstyle-swift.property.md) is [`NSSplitView.DividerStyle.thick`](./dividerstyle-swift.enum/thick.md), or when [`dividerStyle`](./dividerstyle-swift.property.md) is [`NSSplitView.DividerStyle.paneSplitter`](./dividerstyle-swift.enum/panesplitter.md) and the split view is in a textured window. The system draws all other thin dividers with a color that provides appropriate contrast between two white panes.

You can subclass [`NSSplitView`](../nssplitview.md) and override this method to change the color of dividers.

## See Also

### Configuring and Drawing Dividers
- [var dividerStyle: NSSplitView.DividerStyle](./dividerstyle-swift.property.md)
  The style of divider between views.
- [NSSplitView.DividerStyle](./dividerstyle-swift.enum.md)
  Constants that specify the style of the split view’s dividers.
- [var dividerThickness: CGFloat](./dividerthickness.md)
  The thickness of the dividers for the split view.
- [func drawDivider(in: NSRect)](./drawdivider%28in%29.md)
  Draws a divider between two of the split view’s subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/dividercolor)*