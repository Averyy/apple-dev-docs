# NSTableView.ColumnAutoresizingStyle.lastColumnOnlyAutoresizingStyle

**Framework**: AppKit  
**Kind**: case

Autoresize only the last table column.

**Availability**:
- macOS ?+

## Declaration

```swift
case lastColumnOnlyAutoresizingStyle
```

#### Discussion

When that table column can no longer be resized, stop autoresizing.  Normally you should use one of the sequential autoresizing modes instead.

## See Also

- [NSTableView.ColumnAutoresizingStyle.noColumnAutoresizing](nstableview/columnautoresizingstyle-swift.enum/nocolumnautoresizing.md)
  Disable table column autoresizing.
- [NSTableView.ColumnAutoresizingStyle.uniformColumnAutoresizingStyle](nstableview/columnautoresizingstyle-swift.enum/uniformcolumnautoresizingstyle.md)
  Autoresize all columns by distributing space equally, simultaneously.
- [NSTableView.ColumnAutoresizingStyle.sequentialColumnAutoresizingStyle](nstableview/columnautoresizingstyle-swift.enum/sequentialcolumnautoresizingstyle.md)
  Autoresize each table column sequentially, from the last auto-resizable column to the first auto-resizable column; proceed to the next column when the current column has reached its minimum or maximum size.
- [NSTableView.ColumnAutoresizingStyle.reverseSequentialColumnAutoresizingStyle](nstableview/columnautoresizingstyle-swift.enum/reversesequentialcolumnautoresizingstyle.md)
  Autoresize each table column sequentially, from the first auto-resizable column to the last auto-resizable column; proceed to the next column when the current column has reached its minimum or maximum size.
- [NSTableView.ColumnAutoresizingStyle.firstColumnOnlyAutoresizingStyle](nstableview/columnautoresizingstyle-swift.enum/firstcolumnonlyautoresizingstyle.md)
  Autoresize only the first table column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/columnautoresizingstyle-swift.enum/lastcolumnonlyautoresizingstyle)*