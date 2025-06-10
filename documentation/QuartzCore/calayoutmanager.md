# CALayoutManager

**Framework**: Core Animation  
**Kind**: protocol

Methods that allow an object to manage the layout of a layer and its sublayers.

**Availability**:
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
protocol CALayoutManager : NSObjectProtocol
```

## Topics

### Managing Layout
- [func invalidateLayout(of: CALayer)](calayoutmanager/invalidatelayout(of:).md)
  Invalidates the layout of a layer so it knows to refresh its content on the next frame.
- [func layoutSublayers(of: CALayer)](calayoutmanager/layoutsublayers(of:).md)
  Override to customize layout of sublayers whenever the layer needs redrawing.
- [func preferredSize(of: CALayer) -> CGSize](calayoutmanager/preferredsize(of:).md)
  Override to customize layer size.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [CAConstraintLayoutManager](caconstraintlayoutmanager.md)

## See Also

- [class CALayer](calayer.md)
  An object that manages image-based content and allows you to perform animations on that content.
- [protocol CALayerDelegate](calayerdelegate.md)
  Methods your app can implement to respond to layer-related events.
- [class CAConstraint](caconstraint.md)
  A representation of a single layout constraint between two layers.
- [class CAConstraintLayoutManager](caconstraintlayoutmanager.md)
  An object that provides a constraint-based layout manager.
- [protocol CAAction](caaction.md)
  An interface that allows instances to respond to actions triggered by a Core Animation layer change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayoutmanager)*