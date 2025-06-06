# init(_:)

**Framework**: Create ML  
**Kind**: init

Creates a new column from a given sequence of machine learning data values.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init<S>(_ source: S) where S : Sequence, S.Element == MLDataValue
```

#### Discussion

Use this initializer to create a column from a sequence of data values.

```swift
let dataValueOf2 = MLDataValue.int(2)
let dataValueOf3 = MLDataValue.int(3)
let dataValueOf5 = MLDataValue.int(5)
let dataValueOf7 = MLDataValue.int(7)
let dataValueOf11 = MLDataValue.int(11)

let sequence = [dataValueOf2,
                dataValueOf3,
                dataValueOf5,
                dataValueOf7,
                dataValueOf11
]

let sequenceColumn = MLUntypedColumn(sequence)
print(sequenceColumn)
/*
Prints...
 ValueType: Int
 Values:        [2, 3, 5, 7, 11]
 */
```

## Parameters

- `source`: A sequence of data value daelements for the new column.

## See Also

- [init<T>(repeating: T, count: Int)](mluntypedcolumn/init(repeating:count:)-7ttf1.md)
  Creates a new column with a repeating value.
- [init(repeating: MLDataValue, count: Int)](mluntypedcolumn/init(repeating:count:)-q8yk.md)
  Creates a new column with a repeating value.
- [init(Range<Int>)](mluntypedcolumn/init(_:)-33tcv.md)
  Creates a new column of integers from a given range.
- [init(ClosedRange<Int>)](mluntypedcolumn/init(_:)-9no5.md)
  Creates a new column of integers from a given closed range.
- [init<S>(S)](mluntypedcolumn/init(_:)-ag8f.md)
  Creates a new column from a given sequence of elements that can be converted to machine learning data values.
- [init()](mluntypedcolumn/init.md)
  Creates an empty, invalid column used to remove an existing column from a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/init(_:)-5by2g)*