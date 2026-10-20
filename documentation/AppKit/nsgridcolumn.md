# NSGridColumn

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A column within a grid view.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
class NSGridColumn
```

```objc
@interface NSGridColumn : NSObject
```

## Topics

### Instance Properties
- [var gridView: NSGridView?](./nsgridcolumn/gridview.md)
- [var isHidden: Bool](./nsgridcolumn/ishidden.md)
- [var leadingPadding: CGFloat](./nsgridcolumn/leadingpadding.md)
- [var numberOfCells: Int](./nsgridcolumn/numberofcells.md)
- [var trailingPadding: CGFloat](./nsgridcolumn/trailingpadding.md)
- [var width: CGFloat](./nsgridcolumn/width.md)
- [var xPlacement: NSGridCell.Placement](./nsgridcolumn/xplacement.md)
### Instance Methods
- [func cell(at: Int) -> NSGridCell](./nsgridcolumn/cell%28at%29.md)
- [func mergeCells(in: NSRange)](./nsgridcolumn/mergecells%28in%29.md)
### Initializers
- [init?(coder: NSCoder)](./nsgridcolumn/init%28coder%29.md)

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
- [class NSGridRow](./nsgridrow.md)
  A row within a grid view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridcolumn)*