# DataFrame

**Framework**: TabularData  
**Kind**: struct

A collection that arranges data in rows and columns.

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
@dynamicMemberLookup
struct DataFrame
```

## Topics

### Creating a Data Frame
- [init()](dataframe/init.md)
  Creates an empty data frame with no rows or columns.
- [init<S>(columns: S)](dataframe/init(columns:).md)
  Creates a new data frame from a sequence of columns.
- [init(dictionaryLiteral: (String, [Any?])...)](dataframe/init(dictionaryliteral:).md)
  Creates a data frame from a dictionary literal.
### Creating a Data Frame from Other Data Frames
- [init(DataFrame.Slice)](dataframe/init(_:).md)
  Creates a new data frame with a slice of rows from another data frame.
- [DataFrame.Slice](dataframe/slice.md)
  A set of a data frame’s rows you create by using a method from a data frame instance or another data frame slice.
### Creating a Data Frame from a JSON File
- [init(contentsOfJSONFile: URL, columns: [String]?, types: [String : JSONType], options: JSONReadingOptions) throws](dataframe/init(contentsofjsonfile:columns:types:options:).md)
  Creates a data frame by reading a JSON file.
- [init(jsonData: Data, columns: [String]?, types: [String : JSONType], options: JSONReadingOptions) throws](dataframe/init(jsondata:columns:types:options:).md)
  Creates a data frame by converting JSON data.
- [enum JSONType](jsontype.md)
  Represents the value types in a JSON file.
- [struct JSONReadingOptions](jsonreadingoptions.md)
  A set of JSON file-reading options.
### Creating a Data Frame from a CSV
- [init(contentsOfCSVFile: URL, columns: [String]?, rows: Range<Int>?, types: [String : CSVType], options: CSVReadingOptions) throws](dataframe/init(contentsofcsvfile:columns:rows:types:options:).md)
  Creates a data frame from a CSV file.
- [init(csvData: Data, columns: [String]?, rows: Range<Int>?, types: [String : CSVType], options: CSVReadingOptions) throws](dataframe/init(csvdata:columns:rows:types:options:).md)
  Creates a data frame from CSV data.
- [enum CSVType](csvtype.md)
  Represents the value types in a CSV file.
- [struct CSVReadingOptions](csvreadingoptions.md)
  A set of CSV file-reading options.
### Creating a Data Frame from Turi Create Types
- [init(contentsOfSFrameDirectory: URL, columns: [String]?, rows: Range<Int>?) throws](dataframe/init(contentsofsframedirectory:columns:rows:).md)
  Creates a data frame from a Turi Create scalable data frame.
- [struct ShapedData](shapeddata.md)
  A collection type that represents multidimensional data in a data frame element.
### Inspecting a Data Frame
- [var isEmpty: Bool](dataframe/isempty.md)
  A Boolean that indicates whether the data frame type is empty.
- [var shape: (rows: Int, columns: Int)](dataframe/shape.md)
  The number of rows and columns in the data frame.
- [var columns: [AnyColumn]](dataframe/columns.md)
  The entire data frame as a collection of columns.
- [var rows: DataFrame.Rows](dataframe/rows-swift.property.md)
  The entire data frame as a collection of rows.
- [DataFrame.Rows](dataframe/rows-swift.struct.md)
  A collection of rows in a data frame.
- [var base: DataFrame](dataframe/base.md)
  The underlying data frame.
- [func containsColumn<T>(String, T.Type) -> Bool](dataframe/containscolumn(_:_:).md)
  Returns a Boolean value indicating whether the data frame contains a column.
### Sorting a Data Frame
- [func sort(on: String, order: Order)](dataframe/sort(on:order:)-4vns7.md)
  Arranges the rows of a data frame according to a column that you select by its name.
- [func sort<T>(on: String, T.Type, order: Order)](dataframe/sort(on:_:order:)-78avw.md)
  Arranges the rows of a data frame according to a column that you select by its name and type.
- [func sort<T>(on: String, T.Type, by: (T, T) throws -> Bool) rethrows](dataframe/sort(on:_:by:).md)
  Arranges the rows of a data frame according to a column that you select by its name and type, with a predicate.
- [func sort<T>(on: ColumnID<T>, by: (T, T) throws -> Bool) rethrows](dataframe/sort(on:by:).md)
  Arranges the rows of a data frame according to a column that you select by its column identifier, with a predicate.
- [func sort<T>(on: ColumnID<T>, order: Order)](dataframe/sort(on:order:)-5ep7w.md)
  Arranges the rows of a data frame according to a column that you select by its column identifier.
- [func sort<T0, T1>(on: ColumnID<T0>, ColumnID<T1>, order: Order)](dataframe/sort(on:_:order:)-8wrkl.md)
  Arranges the rows of a data frame according to two columns that you select by their column identifiers.
- [func sort<T0, T1, T2>(on: ColumnID<T0>, ColumnID<T1>, ColumnID<T2>, order: Order)](dataframe/sort(on:_:_:order:).md)
  Arranges the rows of a data frame according to three columns that you select by their column identifiers.
### Summarizing a Data Frame
- [func summary() -> DataFrame](dataframe/summary.md)
  Generates a data frame that summarizes the columns of the data frame.
- [func summary(of: String...) -> DataFrame](dataframe/summary(of:).md)
  Generates a data frame that summarizes the columns you select by name.
- [func summary(ofColumns: Int...) -> DataFrame](dataframe/summary(ofcolumns:).md)
  Generates a data frame that summarizes the columns you select by index.
- [enum SummaryColumnIDs](summarycolumnids.md)
  The summary data frame column identifiers.
### Saving a Data Frame to a CSV Format
- [func writeCSV(to: URL, options: CSVWritingOptions) throws](dataframe/writecsv(to:options:).md)
  Creates a CSV file with the contents of the data frame type.
- [func csvRepresentation(options: CSVWritingOptions) throws -> Data](dataframe/csvrepresentation(options:).md)
  Generates a CSV data instance of the data frame type.
- [struct CSVWritingOptions](csvwritingoptions.md)
  A set of CSV file-writing options.
### Describing a Data Frame
- [var description: String](dataframe/description.md)
  A text representation of the data frame.
- [var debugDescription: String](dataframe/debugdescription.md)
  A text representation of the data frame suitable for debugging.
- [func description(options: FormattingOptions) -> String](dataframe/description(options:).md)
  Generates a text representation of the data frame type.
- [var customMirror: Mirror](dataframe/custommirror.md)
  A mirror that reflects the data frame.
### Comparing Data Frames
- [static func == (DataFrame, DataFrame) -> Bool](dataframe/==(_:_:).md)
  Returns a Boolean that indicates whether the data frames are equal.
- [static func != (Self, Self) -> Bool](dataframe/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Hashing a Data Frame
- [func hash(into: inout Hasher)](dataframe/hash(into:).md)
  Hashes the essential components of the data frame by feeding them into a hasher.
- [var hashValue: Int](dataframe/hashvalue.md)
  The hash value.
### Initializers
- [init<S, Feature, Annotation>(S, featuresColumnID: ColumnID<Feature>, annotationsColumnID: ColumnID<Annotation>) throws](dataframe/init(_:featurescolumnid:annotationscolumnid:).md)
  Creates a data frame from a sequence of annotated features.
- [init<each T>(contentsOfCSVFile: URL, columns: repeat ColumnID<each T>, rows: Range<Int>?, options: CSVReadingOptions) throws](dataframe/init(contentsofcsvfile:columns:rows:options:).md)
  Creates a data frame from a CSV file.
- [init<each T>(csvData: Data, columns: repeat ColumnID<each T>, rows: Range<Int>?, options: CSVReadingOptions) throws](dataframe/init(csvdata:columns:rows:options:).md)
  Creates a data frame from CSV data.
### Instance Methods
- [func containsColumn<T>(ColumnID<T>) -> Bool](dataframe/containscolumn(_:)-6nqfs.md)
  Returns a Boolean value indicating whether the data frame contains a column matching a column ID.
- [func containsColumn(String) -> Bool](dataframe/containscolumn(_:)-8spst.md)
  Returns a Boolean value indicating whether the data frame contains a column.
- [func loadRangedAnnotations<Annotation>(parameters: DataFrameTemporalAnnotationParameters<Annotation>, continueOnFailure: Bool) throws -> [AnnotatedFeature<TemporalFileSegment, Annotation>]](dataframe/loadrangedannotations(parameters:continueonfailure:).md)
  Loads training examples from a data frame containing annotations.
- [func selecting(ColumnSelection) -> DataFrame](dataframe/selecting(_:).md)
  Generates a data frame that includes only the column selection.
### Type Aliases
- [DataFrame.ColumnType](dataframe/columntype.md)
  A type that conforms to the type-erased column protocol.
### Default Implementations
- [CustomDebugStringConvertible Implementations](dataframe/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](dataframe/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](dataframe/customstringconvertible-implementations.md)
- [DataFrameProtocol Implementations](dataframe/dataframeprotocol-implementations.md)
- [Equatable Implementations](dataframe/equatable-implementations.md)
- [ExpressibleByDictionaryLiteral Implementations](dataframe/expressiblebydictionaryliteral-implementations.md)
- [Hashable Implementations](dataframe/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataFrameProtocol](dataframeprotocol.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByDictionaryLiteral](../Swift/ExpressibleByDictionaryLiteral.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [protocol DataFrameProtocol](dataframeprotocol.md)
  A type that represents a data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe)*