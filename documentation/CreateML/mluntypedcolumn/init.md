# init()

**Framework**: Create ML  
**Kind**: init

Creates an empty, invalid column used to remove an existing column from a data table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init()
```

#### Return Value

An empty, invalid column.

#### Discussion

Use this initializer to create an empty column that, when assigned to the name of an existing column within a data table, will remove that column from the table.

For example, to remove a column from a data table, first start with a variable data table.

```swift
let data: [String: MLDataValueConvertible] = [
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Temperature": [91.3, 85.8, 79.5, 83.4, 72.2]
]

var table = try MLDataTable(dictionary: data)

print(table)
/* Prints...
 Columns:
 Day    string
 Temperature    float
 Rows: 5
 Data:
 +----------------+----------------+
 | Day            | Temperature    |
 +----------------+----------------+
 | Monday         | 91.3           |
 | Tuesday        | 85.8           |
 | Wednesday      | 79.5           |
 | Thursday       | 83.4           |
 | Friday         | 72.2           |
 +----------------+----------------+
 [5 rows x 2 columns]
 */
```

Then use [`init()`](mluntypedcolumn/init().md) to create an empty column.

```swift
let emptyColumn = MLUntypedColumn()
```

Finally, use [`subscript(_:)`](mluntypedcolumn/subscript(_:)-9hr32.md) to remove the existing column from the data table by setting the empty column to the name of that existing column.

```swift
// Remove the "Temperature" column from the data table
table["Temperature"] = emptyColumn

print(table)
/* Prints...
 Columns:
 Day    string
 Rows: 5
 Data:
 +----------------+
 | Day            |
 +----------------+
 | Monday         |
 | Tuesday        |
 | Wednesday      |
 | Thursday       |
 | Friday         |
 +----------------+
 [5 rows x 1 columns]
 */
```

## See Also

- [init(repeating:count:)](mluntypedcolumn/init(repeating:count:).md)
  Creates a new column with a repeating value.
- [init<T>(repeating: T, count: Int)](mluntypedcolumn/init(repeating:count:)-7ttf1.md)
  Creates a new column with a repeating value.
- [init(repeating: MLDataValue, count: Int)](mluntypedcolumn/init(repeating:count:)-q8yk.md)
  Creates a new column with a repeating value.
- [init(_:)](mluntypedcolumn/init(_:).md)
  Creates a new column of integers from a given closed range.
- [init(Range<Int>)](mluntypedcolumn/init(_:)-33tcv.md)
  Creates a new column of integers from a given range.
- [init(ClosedRange<Int>)](mluntypedcolumn/init(_:)-9no5.md)
  Creates a new column of integers from a given closed range.
- [init<S>(S)](mluntypedcolumn/init(_:)-ag8f.md)
  Creates a new column from a given sequence of elements that can be converted to machine learning data values.
- [init<S>(S)](mluntypedcolumn/init(_:)-5by2g.md)
  Creates a new column from a given sequence of machine learning data values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/init())*