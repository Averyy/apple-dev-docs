# CSVType

**Framework**: TabularData  
**Kind**: enum

Represents the value types in a CSV file.

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
enum CSVType
```

## Topics

### Operators
- [static func == (CSVType, CSVType) -> Bool](csvtype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [CSVType.boolean](csvtype/boolean.md)
  A Boolean type.
- [CSVType.data](csvtype/data.md)
  A binary data type.
- [CSVType.date](csvtype/date.md)
  A date type.
- [CSVType.double](csvtype/double.md)
  A double-precision floating-point type.
- [CSVType.float](csvtype/float.md)
  A single-precision floating-point type.
- [CSVType.integer](csvtype/integer.md)
  An integer type.
- [CSVType.string](csvtype/string.md)
  A string type.
### Instance Properties
- [var hashValue: Int](csvtype/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](csvtype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](csvtype/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(contentsOfCSVFile: URL, columns: [String]?, rows: Range<Int>?, types: [String : CSVType], options: CSVReadingOptions) throws](dataframe/init(contentsofcsvfile:columns:rows:types:options:).md)
  Creates a data frame from a CSV file.
- [init(csvData: Data, columns: [String]?, rows: Range<Int>?, types: [String : CSVType], options: CSVReadingOptions) throws](dataframe/init(csvdata:columns:rows:types:options:).md)
  Creates a data frame from CSV data.
- [struct CSVReadingOptions](csvreadingoptions.md)
  A set of CSV file-reading options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvtype)*