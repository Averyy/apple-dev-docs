# NSGridColumn

**Framework**: AppKit  
**Kind**: class

A column within a grid view.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
class NSGridColumn
```

## Topics

### Instance Properties
- [var gridView: NSGridView?](nsgridcolumn/gridview.md)
- [var isHidden: Bool](nsgridcolumn/ishidden.md)
- [var leadingPadding: CGFloat](nsgridcolumn/leadingpadding.md)
- [var numberOfCells: Int](nsgridcolumn/numberofcells.md)
- [var trailingPadding: CGFloat](nsgridcolumn/trailingpadding.md)
- [var width: CGFloat](nsgridcolumn/width.md)
- [var xPlacement: NSGridCell.Placement](nsgridcolumn/xplacement.md)
### Instance Methods
- [func cell(at: Int) -> NSGridCell](nsgridcolumn/cell(at:).md)
- [func mergeCells(in: NSRange)](nsgridcolumn/mergecells(in:).md)
### Initializers
- [init?(coder: NSCoder)](nsgridcolumn/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)

## See Also

- [class NSGridRow](nsgridrow.md)
  A row within a grid view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridcolumn)*