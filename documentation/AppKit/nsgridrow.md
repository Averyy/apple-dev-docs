# NSGridRow

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A row within a grid view.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
class NSGridRow
```

```objc
@interface NSGridRow : NSObject
```

## Topics

### Getting the Row Details
- [var numberOfCells: Int](./nsgridrow/numberofcells.md)
- [var isHidden: Bool](./nsgridrow/ishidden.md)
### Formatting the Row
- [var topPadding: CGFloat](./nsgridrow/toppadding.md)
- [var bottomPadding: CGFloat](./nsgridrow/bottompadding.md)
- [var height: CGFloat](./nsgridrow/height.md)
- [var rowAlignment: NSGridRow.Alignment](./nsgridrow/rowalignment.md)
- [var yPlacement: NSGridCell.Placement](./nsgridrow/yplacement.md)
- [NSGridRow.Alignment](./nsgridrow/alignment.md)
### Getting the Grid View
- [var gridView: NSGridView?](./nsgridrow/gridview.md)
### Getting Cells
- [func cell(at: Int) -> NSGridCell](./nsgridrow/cell%28at%29.md)
### Merging Cells in the Row
- [func mergeCells(in: NSRange)](./nsgridrow/mergecells%28in%29.md)
### Initializers
- [init?(coder: NSCoder)](./nsgridrow/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Rows and Columns
- [class NSGridColumn](./nsgridcolumn.md)
  A column within a grid view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridrow)*