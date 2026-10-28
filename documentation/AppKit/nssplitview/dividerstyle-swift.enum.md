# NSSplitView.DividerStyle

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the style of the split view’s dividers.

**Availability**:
- macOS 10.5+

## Declaration

```swift
enum DividerStyle
```

```c
enum NSSplitViewDividerStyle : NSInteger;
```

## Overview

These constants specify the possible divider styles that [`NSSplitView`](../nssplitview.md) uses.

## Topics

### Constants
- [NSSplitView.DividerStyle.thick](./dividerstyle-swift.enum/thick.md)
  A thick style divider displays between subviews.
- [NSSplitView.DividerStyle.thin](./dividerstyle-swift.enum/thin.md)
  A thin style divider displays between subviews.
- [NSSplitView.DividerStyle.paneSplitter](./dividerstyle-swift.enum/panesplitter.md)
  A thick style divider with a 3D appearance displays between subviews.
### Initializers
- [init?(rawValue: Int)](./dividerstyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring and Drawing Dividers
- [var dividerStyle: NSSplitView.DividerStyle](./dividerstyle-swift.property.md)
  The style of divider between views.
- [var dividerColor: NSColor](./dividercolor.md)
  The color of the dividers that the split view draws between subviews.
- [var dividerThickness: CGFloat](./dividerthickness.md)
  The thickness of the dividers for the split view.
- [func drawDivider(in: NSRect)](./drawdivider%28in%29.md)
  Draws a divider between two of the split view’s subviews.
- [- isPaneSplitter](./ispanesplitter.md)
  The type of pane splitter.
- [- setIsPaneSplitter:](./setispanesplitter_.md)
  Sets the type of splitter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/dividerstyle-swift.enum)*