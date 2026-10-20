# init(repeating:count:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

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
init<T>(repeating repeatedValue: T, count: Int) where T : MLDataValueConvertible
```

**Other overloads**:

```swift
init(repeating repeatedValue: MLDataValue, count: Int)
```

#### Discussion

Use this initializer to create a column of repeating elements with any type that conforms to [`MLDataValueConvertible`](../mldatavalueconvertible.md), including integers, doubles, strings, arrays, and dictionaries.

```swift
let three5s = MLUntypedColumn(repeating: 5, count: 3)
print(three5s)
/* Prints...
 ValueType: Int
 Values:        [5, 5, 5]
 */
```

## Parameters

- `repeatedValue`: An initial value for every element in the new column.
- `count`: The number of elements in the new column.

## See Also

### Creating an untyped column
- [init(repeating:count:)](./init%28repeating,count%29.md)
  Creates a new column with a repeating value.
- [init(repeating: MLDataValue, count: Int)](./init%28repeating,count%29-q8yk.md)
  Creates a new column with a repeating value.
- [init(_:)](./init%28_%29.md)
  Creates a new column of integers from a given closed range.
- [init(Range<Int>)](./init%28_%29-33tcv.md)
  Creates a new column of integers from a given range.
- [init(ClosedRange<Int>)](./init%28_%29-9no5.md)
  Creates a new column of integers from a given closed range.
- [init<S>(S)](./init%28_%29-ag8f.md)
  Creates a new column from a given sequence of elements that can be converted to machine learning data values.
- [init<S>(S)](./init%28_%29-5by2g.md)
  Creates a new column from a given sequence of machine learning data values.
- [init()](./init%28%29.md)
  Creates an empty, invalid column used to remove an existing column from a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/init(repeating:count:)-7ttf1)*