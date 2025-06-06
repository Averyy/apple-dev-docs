# TabularData

**Framework**: TabularData  
**Kind**: module

Import, organize, and prepare a table of data to train a machine learning model.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Topics

### Data Tables
- [struct DataFrame](dataframe.md)
  A collection that arranges data in rows and columns.
- [protocol DataFrameProtocol](dataframeprotocol.md)
  A type that represents a data frame.
### Typed Columns
- [struct Column](column.md)
  A column in a data frame.
- [struct ColumnSlice](columnslice.md)
  A collection that represents a selection of contiguous elements from a typed column.
- [struct FilledColumn](filledcolumn.md)
  A view on a column that replaces missing elements with a default value.
- [struct DiscontiguousColumnSlice](discontiguouscolumnslice.md)
  A collection that represents a selection, potentially with gaps, of elements from a typed column.
- [protocol ColumnProtocol](columnprotocol.md)
  A type that represents a column.
- [protocol OptionalColumnProtocol](optionalcolumnprotocol.md)
  A type that represents a column that has missing values.
### Type-Erased Columns
- [struct AnyColumn](anycolumn.md)
  A type-erased column.
- [struct AnyColumnSlice](anycolumnslice.md)
  A type-erased column slice.
- [protocol AnyColumnProtocol](anycolumnprotocol.md)
  A type that represents a type-erased column.
- [protocol AnyColumnPrototype](anycolumnprototype.md)
  A prototype that creates type-erased columns.
### Statistical Summaries
- [struct NumericSummary](numericsummary.md)
  A summary of a numerical column.
- [struct CategoricalSummary](categoricalsummary.md)
  A categorical summary of a collection’s elements.
- [struct AnyCategoricalSummary](anycategoricalsummary.md)
  A type-erased categorical summary.
### Errors
- [enum JSONReadingError](jsonreadingerror.md)
  A JSON reading error.
- [enum CSVReadingError](csvreadingerror.md)
  A CSV reading error.
- [enum CSVWritingError](csvwritingerror.md)
  A CSV writing error.
- [struct ColumnDecodingError](columndecodingerror.md)
  A column decoding error.
- [struct ColumnEncodingError](columnencodingerror.md)
  A column encoding error.
- [enum SFrameReadingError](sframereadingerror.md)
  An error when reading a Turi Create scalable data frame.
### Supporting Types
- [enum Order](order.md)
  A type that represents a sort ordering.
- [struct ColumnID](columnid.md)
  A column identifier that stores a column’s name and the type of its elements.
- [struct FormattingOptions](formattingoptions.md)
  A set of parameters that indicate how to present the contents of data frame or column types to a printable string.
### Structures
- [struct JSONWritingOptions](jsonwritingoptions.md)
  A set of JSON file-reading options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/TabularData)*