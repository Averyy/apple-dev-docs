# columnCount

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The number of columns in a table.

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
@property (readonly) NSInteger columnCount;
```

## Discussion

If the intent is not a table, the value of this property is `0`.

## See Also

### Getting table information
- [row](./row.md)
  The row number to which this cell belongs.
- [column](./column.md)
  The column number to which the cell belongs.
- [columnAlignments](./columnalignments.md)
  The alignments for the columns in a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspresentationintent/columncount)*