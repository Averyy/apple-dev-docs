# NSTableView.ColumnAutoresizingStyle.sequentialColumnAutoresizingStyle

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Autoresize each table column sequentially, from the last auto-resizable column to the first auto-resizable column; proceed to the next column when the current column has reached its minimum or maximum size.

**Availability**:
- macOS

## Declaration

```swift
case sequentialColumnAutoresizingStyle
```

```c
NSTableViewSequentialColumnAutoresizingStyle
```

## See Also

### Constants
- [NSTableView.ColumnAutoresizingStyle.noColumnAutoresizing](./nocolumnautoresizing.md)
  Disable table column autoresizing.
- [NSTableView.ColumnAutoresizingStyle.uniformColumnAutoresizingStyle](./uniformcolumnautoresizingstyle.md)
  Autoresize all columns by distributing space equally, simultaneously.
- [NSTableView.ColumnAutoresizingStyle.reverseSequentialColumnAutoresizingStyle](./reversesequentialcolumnautoresizingstyle.md)
  Autoresize each table column sequentially, from the first auto-resizable column to the last auto-resizable column; proceed to the next column when the current column has reached its minimum or maximum size.
- [NSTableView.ColumnAutoresizingStyle.lastColumnOnlyAutoresizingStyle](./lastcolumnonlyautoresizingstyle.md)
  Autoresize only the last table column.
- [NSTableView.ColumnAutoresizingStyle.firstColumnOnlyAutoresizingStyle](./firstcolumnonlyautoresizingstyle.md)
  Autoresize only the first table column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/columnautoresizingstyle-swift.enum/sequentialcolumnautoresizingstyle)*