# NSGridCell

**Framework**: AppKit  
**Kind**: class

An individual content area within a grid view, typically at the intersection of a row and a column.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
class NSGridCell
```

#### Overview

Use a grid cell to specify the content view to display and to position the content view within the cell’s area.

## Topics

### Getting the Cell Containers
- [var column: NSGridColumn?](nsgridcell/column.md)
- [var row: NSGridRow?](nsgridcell/row.md)
- [var contentView: NSView?](nsgridcell/contentview.md)
- [class var emptyContentView: NSView](nsgridcell/emptycontentview.md)
### Formatting the Cell
- [var customPlacementConstraints: [NSLayoutConstraint]](nsgridcell/customplacementconstraints.md)
- [var rowAlignment: NSGridRow.Alignment](nsgridcell/rowalignment.md)
- [var xPlacement: NSGridCell.Placement](nsgridcell/xplacement.md)
- [var yPlacement: NSGridCell.Placement](nsgridcell/yplacement.md)
- [NSGridCell.Placement](nsgridcell/placement.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridcell)*