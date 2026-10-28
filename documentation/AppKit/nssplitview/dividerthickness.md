# dividerThickness

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The thickness of the dividers for the split view.

**Availability**:
- macOS

## Declaration

```swift
var dividerThickness: CGFloat { get }
```

```objc
@property (readonly) CGFloat dividerThickness;
```

## Discussion

You can subclass [`NSSplitView`](../nssplitview.md) and override this method to change the thickness of a split view’s dividers.

## See Also

### Configuring and Drawing Dividers
- [var dividerStyle: NSSplitView.DividerStyle](./dividerstyle-swift.property.md)
  The style of divider between views.
- [NSSplitView.DividerStyle](./dividerstyle-swift.enum.md)
  Constants that specify the style of the split view’s dividers.
- [var dividerColor: NSColor](./dividercolor.md)
  The color of the dividers that the split view draws between subviews.
- [func drawDivider(in: NSRect)](./drawdivider%28in%29.md)
  Draws a divider between two of the split view’s subviews.
- [- isPaneSplitter](./ispanesplitter.md)
  The type of pane splitter.
- [- setIsPaneSplitter:](./setispanesplitter_.md)
  Sets the type of splitter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/dividerthickness)*