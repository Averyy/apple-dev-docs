# map(to:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Creates a new column by converting this column to the given type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func map<T>(to type: T.Type) -> MLDataColumn<T> where T : MLDataValueConvertible
```

Available when `Element` conforms to `MLDataValueConvertible`.

#### Return Value

A new column.

#### Discussion

This method is functionally equivalent to the initializers of [`MLDataColumn`](../mldatacolumn.md) that have one parameter `column`, such as [`init(column:)`](./init%28column%29-86ge9.md).

## Parameters

- `type`: A type of [`MLDataColumn`](../mldatacolumn.md) to convert the contents of the column to, using [`MLDataValueConvertible`](../mldatavalueconvertible.md).

## See Also

### Creating a data column by converting another column
- [init(column:)](./init%28column%29.md)
  Creates a new column of machine learning sequences from a given column whose elements can be converted to sequences.
- [init<T>(column: MLDataColumn<T>)](./init%28column%29-5rg9u.md)
  Creates a new column of integers from a given column whose elements can be converted to integers.
- [init<T>(column: MLDataColumn<T>)](./init%28column%29-2rxtu.md)
  Creates a new column of arrays of integers from a given column whose elements can be converted to an array of integers.
- [init<T>(column: MLDataColumn<T>)](./init%28column%29-86ge9.md)
  Creates a new column of doubles from a given column whose elements can be converted to doubles.
- [init<T>(column: MLDataColumn<T>)](./init%28column%29-23pmx.md)
  Creates a new column of arrays of doubles from a given column whose elements can be converted to an array of doubles.
- [init<T>(column: MLDataColumn<T>)](./init%28column%29-ztkv.md)
  Creates a new column of strings from a given column whose elements can be converted to strings.
- [init<T>(column: MLDataColumn<T>)](./init%28column%29-8uzuq.md)
  Creates a new column of arrays of strings from a given column whose elements can be converted to an array of strings.
- [init<T>(column: MLDataColumn<T>)](./init%28column%29-855l9.md)
  Creates a new column of machine learning sequences from a given column whose elements can be converted to sequences.
- [init<T>(column: MLDataColumn<T>)](./init%28column%29-s8g5.md)
  Creates a new column of machine learning dictionaries from a given column whose elements can be converted to dictionaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/map(to:))*