# FormattingOptions

**Framework**: TabularData  
**Kind**: struct

A set of parameters that indicate how to present the contents of data frame or column types to a printable string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct FormattingOptions
```

## Topics

### Creating the Options Object
- [init()](formattingoptions/init.md)
  Creates a formatting options instance with default parameters.
- [init(locale: Locale)](formattingoptions/init(locale:).md)
  Creates a formatting options instance with a locale.
- [init(maximumLineWidth: Int, maximumCellWidth: Int, maximumRowCount: Int, includesColumnTypes: Bool)](formattingoptions/init(maximumlinewidth:maximumcellwidth:maximumrowcount:includescolumntypes:).md)
  Creates a formatting options instance.
### Getting the Properties
- [var dateFormatStyle: Date.FormatStyle](formattingoptions/dateformatstyle.md)
  The date format style.
- [var floatingPointFormatStyle: FloatingPointFormatStyle<Double>](formattingoptions/floatingpointformatstyle.md)
  The floating point format style.
- [var includesColumnTypes: Bool](formattingoptions/includescolumntypes.md)
  A Boolean value that indicates whether the description includes the column types.
- [var integerFormatStyle: IntegerFormatStyle<Int>](formattingoptions/integerformatstyle.md)
  The integer format style.
- [var locale: Locale](formattingoptions/locale.md)
  The locale.
- [var maximumCellWidth: Int](formattingoptions/maximumcellwidth.md)
  The largest number of characters a description can generate per cell.
- [var maximumLineWidth: Int](formattingoptions/maximumlinewidth.md)
  The largest number of characters a description can generate per line.
- [var maximumRowCount: Int](formattingoptions/maximumrowcount.md)
  The largest number of rows a description can generate.
### Instance Properties
- [var includesRowAndColumnCounts: Bool](formattingoptions/includesrowandcolumncounts.md)
  A Boolean value that indicates whether the description includes the number of rows and columns.
- [var includesRowIndices: Bool](formattingoptions/includesrowindices.md)
  A Boolean value that indicates whether the description includes the row indices.

## See Also

- [enum Order](order.md)
  A type that represents a sort ordering.
- [struct ColumnID](columnid.md)
  A column identifier that stores a column’s name and the type of its elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/formattingoptions)*