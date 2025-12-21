# init(_:)

**Framework**: Create ML  
**Kind**: init

Creates a new column of integers from a given range.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(_ range: Range<Int>)
```

#### Discussion

Use this initializer to create a column of incrementing values from a range.

```swift
let rangeColumn = MLUntypedColumn(3..<7)

print(rangeColumn)
/* Prints...
 ValueType: Int
 Values:        [3, 4, 5, 6]
 */
```

## Parameters

- `range`: A range of integer elements for the new column.

## See Also

- [init(repeating:count:)](mluntypedcolumn/init(repeating:count:).md)
  Creates a new column with a repeating value.
- [init<T>(repeating: T, count: Int)](mluntypedcolumn/init(repeating:count:)-7ttf1.md)
  Creates a new column with a repeating value.
- [init(repeating: MLDataValue, count: Int)](mluntypedcolumn/init(repeating:count:)-q8yk.md)
  Creates a new column with a repeating value.
- [init(_:)](mluntypedcolumn/init(_:).md)
  Creates a new column of integers from a given closed range.
- [init(ClosedRange<Int>)](mluntypedcolumn/init(_:)-9no5.md)
  Creates a new column of integers from a given closed range.
- [init<S>(S)](mluntypedcolumn/init(_:)-ag8f.md)
  Creates a new column from a given sequence of elements that can be converted to machine learning data values.
- [init<S>(S)](mluntypedcolumn/init(_:)-5by2g.md)
  Creates a new column from a given sequence of machine learning data values.
- [init()](mluntypedcolumn/init.md)
  Creates an empty, invalid column used to remove an existing column from a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/init(_:)-33tcv)*