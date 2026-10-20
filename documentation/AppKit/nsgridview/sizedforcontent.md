# sizedForContent

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The default value for row and column sizes.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class let sizedForContent: CGFloat
```

```c
extern const CGFloat NSGridViewSizeForContent;
```

#### Discussion

This constant indicates that a row or column should automatically fit the content views.

## See Also

### Managing Grid Spacing and Alignment
- [var columnSpacing: CGFloat](./columnspacing.md)
  The column spacing for the grid view.
- [var rowSpacing: CGFloat](./rowspacing.md)
  The row spacing for the grid view.
- [var rowAlignment: NSGridRow.Alignment](./rowalignment.md)
  The row alignment for the grid view.
- [var xPlacement: NSGridCell.Placement](./xplacement.md)
  The placement of the cell within the grid column.
- [var yPlacement: NSGridCell.Placement](./yplacement.md)
  The placement of the cell within the grid row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/sizedforcontent)*