# NSGridRow

**Framework**: AppKit  
**Kind**: class

A row within a grid view.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
class NSGridRow
```

## Topics

### Getting the Row Details
- [var numberOfCells: Int](nsgridrow/numberofcells.md)
- [var isHidden: Bool](nsgridrow/ishidden.md)
### Formatting the Row
- [var topPadding: CGFloat](nsgridrow/toppadding.md)
- [var bottomPadding: CGFloat](nsgridrow/bottompadding.md)
- [var height: CGFloat](nsgridrow/height.md)
- [var rowAlignment: NSGridRow.Alignment](nsgridrow/rowalignment.md)
- [var yPlacement: NSGridCell.Placement](nsgridrow/yplacement.md)
- [NSGridRow.Alignment](nsgridrow/alignment.md)
### Getting the Grid View
- [var gridView: NSGridView?](nsgridrow/gridview.md)
### Getting Cells
- [func cell(at: Int) -> NSGridCell](nsgridrow/cell(at:).md)
### Merging Cells in the Row
- [func mergeCells(in: NSRange)](nsgridrow/mergecells(in:).md)

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

## See Also

- [class NSGridColumn](nsgridcolumn.md)
  A column within a grid view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridrow)*