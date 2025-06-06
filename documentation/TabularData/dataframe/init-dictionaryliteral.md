# init(dictionaryLiteral:)

**Framework**: TabularData  
**Kind**: init

Creates a data frame from a dictionary literal.

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
init(dictionaryLiteral elements: (String, [Any?])...)
```

#### Discussion

Don’t call this initializer directly. The compiler calls it to create a data frame from a dictionary literal. You create a dictionary literal by enclosing a comma-separated list of key-value pairs in square brackets.

For example, this line creates a data frame with two columns and four rows:

```swift
let dataFrame: DataFrame = ["a": [1, 2, 3, 5], "b": [1.414, 2.718, 3.14, 6.28]]
```

The initializer checks each column’s elements and, if possible, defines the column’s type to one of the following:

- `Bool`
- `Int`
- `Float`
- `Double`
- `Date`
- `String`
- `Data`

Otherwise, the data frame sets a column’s type to `Any`.

> **Note**: Use [`append(column:)`](dataframe/append(column:)-aema.md) to add a column of a specific type.

Use [`append(column:)`](dataframe/append(column:)-aema.md) to add a column of a specific type.

## Parameters

- `elements`: A comma-separated, or variadic, list of tuples.   Each tuple consists of two elements:

## See Also

- [init()](dataframe/init.md)
  Creates an empty data frame with no rows or columns.
- [init<S>(columns: S)](dataframe/init(columns:).md)
  Creates a new data frame from a sequence of columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/init(dictionaryliteral:))*