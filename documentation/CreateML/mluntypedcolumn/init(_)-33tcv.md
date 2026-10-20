# init(_:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

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

**Other overloads**:

```swift
init(_ range: ClosedRange<Int>)
```

```swift
init<S>(_ source: S) where S : Sequence, S.Element : MLDataValueConvertible
```

```swift
init<S>(_ source: S) where S : Sequence, S.Element == MLDataValue
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

### Creating an untyped column
- [init(repeating:count:)](./init%28repeating,count%29.md)
  Creates a new column with a repeating value.
- [init<T>(repeating: T, count: Int)](./init%28repeating,count%29-7ttf1.md)
  Creates a new column with a repeating value.
- [init(repeating: MLDataValue, count: Int)](./init%28repeating,count%29-q8yk.md)
  Creates a new column with a repeating value.
- [init(_:)](./init%28_%29.md)
  Creates a new column of integers from a given closed range.
- [init(ClosedRange<Int>)](./init%28_%29-9no5.md)
  Creates a new column of integers from a given closed range.
- [init<S>(S)](./init%28_%29-ag8f.md)
  Creates a new column from a given sequence of elements that can be converted to machine learning data values.
- [init<S>(S)](./init%28_%29-5by2g.md)
  Creates a new column from a given sequence of machine learning data values.
- [init()](./init%28%29.md)
  Creates an empty, invalid column used to remove an existing column from a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/init(_:)-33tcv)*