# column

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The column number to which the cell belongs.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
@property (readonly) NSInteger column;
```

#### Discussion

The value of this property is `0`-based, with the first column at `0`, the second column at `1`, and so on. Header rows are always at row `0`, with subsequent rows starting at `1`. If The intent is not a cell, this value is `0`.

## See Also

### Getting table information
- [row](./row.md)
  The row number to which this cell belongs.
- [columnCount](./columncount.md)
  The number of columns in a table.
- [columnAlignments](./columnalignments.md)
  The alignments for the columns in a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspresentationintent/column)*