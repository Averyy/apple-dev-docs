# columnAlignments

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The alignments for the columns in a table.

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
@property (readonly, nullable) NSArray<NSNumber *> * columnAlignments;
```

## Discussion

If the intent is not a table, the value of this property is `nil`.

## See Also

### Getting table information
- [row](./row.md)
  The row number to which this cell belongs.
- [column](./column.md)
  The column number to which the cell belongs.
- [columnCount](./columncount.md)
  The number of columns in a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspresentationintent/columnalignments)*