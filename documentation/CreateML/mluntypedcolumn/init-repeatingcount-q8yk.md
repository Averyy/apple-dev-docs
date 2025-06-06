# init(repeating:count:)

**Framework**: Create ML  
**Kind**: init

Creates a new column with a repeating value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(repeating repeatedValue: MLDataValue, count: Int)
```

#### Discussion

Use this initializer to create a column of repeating elements of a data value.

```swift
let dataValueOf5 = MLDataValue.int(5)
let three5s = MLUntypedColumn(repeating: dataValueOf5, count: 3)
print(three5s)
/*
Prints...
 ValueType: Int
 Values:        [5, 5, 5]
 */
```

## Parameters

- `repeatedValue`: An initial value for every element in the new column.
- `count`: The number of elements in the new column.

## See Also

- [init<T>(repeating: T, count: Int)](mluntypedcolumn/init(repeating:count:)-7ttf1.md)
  Creates a new column with a repeating value.
- [init(Range<Int>)](mluntypedcolumn/init(_:)-33tcv.md)
  Creates a new column of integers from a given range.
- [init(ClosedRange<Int>)](mluntypedcolumn/init(_:)-9no5.md)
  Creates a new column of integers from a given closed range.
- [init<S>(S)](mluntypedcolumn/init(_:)-ag8f.md)
  Creates a new column from a given sequence of elements that can be converted to machine learning data values.
- [init<S>(S)](mluntypedcolumn/init(_:)-5by2g.md)
  Creates a new column from a given sequence of machine learning data values.
- [init()](mluntypedcolumn/init.md)
  Creates an empty, invalid column used to remove an existing column from a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/init(repeating:count:)-q8yk)*