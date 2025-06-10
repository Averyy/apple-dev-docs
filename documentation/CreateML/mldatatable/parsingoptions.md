# MLDataTable.ParsingOptions

**Framework**: Create ML  
**Kind**: struct

The options for parsing a comma-separated values (CSV) file into a data table for a machine learning model.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct ParsingOptions
```

#### Overview

Use `ParsingOptions` only when importing a CSV file with [`init(contentsOf:options:)`](mldatatable/init(contentsof:options:).md), especially if your CSV file has special formatting or your data table only needs to import specific rows or columns.

## Topics

### Creating the CSV parsing options
- [init(containsHeader: Bool, delimiter: String, comment: String, escape: String, doubleQuote: Bool, quote: String, skipInitialSpaces: Bool, missingValues: [String], lineTerminator: String, selectColumns: [String]?, maxRows: Int?, skipRows: Int)](mldatatable/parsingoptions/init(containsheader:delimiter:comment:escape:doublequote:quote:skipinitialspaces:missingvalues:lineterminator:selectcolumns:maxrows:skiprows:).md)
  Creates CSV parsing options.
### Specifying the CSV file format
- [var containsHeader: Bool](mldatatable/parsingoptions/containsheader.md)
  A Boolean value indicating whether an input CSV file contains a header.
- [var delimiter: String](mldatatable/parsingoptions/delimiter.md)
  The character that separates the data fields in a CSV file.
- [var lineTerminator: String](mldatatable/parsingoptions/lineterminator.md)
  The character that represents the end of a line in a CSV file.
### Handling special characters
- [var escape: String](mldatatable/parsingoptions/escape.md)
  The character that marks a C escape sequence in a CSV file.
- [var quote: String](mldatatable/parsingoptions/quote.md)
  The character that represents a quote (`"`) in a CSV file.
- [var doubleQuote: Bool](mldatatable/parsingoptions/doublequote.md)
  A Boolean value indicating whether two consecutive quotes (`""`) represent a single quote (`"`) in a CSV file.
### Ignoring CSV components
- [var skipRows: Int](mldatatable/parsingoptions/skiprows.md)
  The number of starting rows to skip from the start of a CSV file.
- [var skipInitialSpaces: Bool](mldatatable/parsingoptions/skipinitialspaces.md)
  A Boolean value indicating whether to ignore leading spaces of a data field.
- [var comment: String](mldatatable/parsingoptions/comment.md)
  The character that marks the beginning of a comment, or text to ignore, in a CSV file.
### Limiting rows and columns
- [var maxRows: Int?](mldatatable/parsingoptions/maxrows.md)
  The maximum number of rows to import form a CSV file; otherwise `nil` to import all rows.
- [var selectColumns: [String]?](mldatatable/parsingoptions/selectcolumns.md)
  The list of column names to import from a CSV file; otherwise `nil` to import all columns.
### Representing missing values
- [var missingValues: [String]](mldatatable/parsingoptions/missingvalues.md)
  A list of strings that represent missing values in a CSV file.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/parsingoptions)*