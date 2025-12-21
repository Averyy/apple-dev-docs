# init(column:)

**Framework**: Create ML  
**Kind**: init

Creates a new column of machine learning sequences from a given column whose elements can be converted to sequences.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init<T>(column: MLDataColumn<T>) where T : MLDataValueConvertible
```

#### Discussion

Use this initializer to create a column of sequences from another column. Start by creating a column that is convertible to a column of sequences.

```swift
let intSequenceString = "[1, 2, 3]"
let intSequenceString2 = "[4, 5, 6]"
let stringsColumn = MLDataColumn([intSequenceString, intSequenceString2])

print(stringsColumn) // Prints "[1, 2, 3]", "[4, 5, 6]"]
```

Then use [`init(column:)`](mldatacolumn/init(column:)-855l9.md) to convert the column to a column of sequences.

```swift
let sequenceColumn = MLDataColumn<MLDataValue.SequenceType>(column: stringsColumn)
print(sequenceColumn) // Prints [[DataValue(1), DataValue(2), DataValue(3)],
                      // [DataValue(4), DataValue(5), DataValue(6)]]
```

## Parameters

- `column`: An   of elements convertible to  .

## See Also

- [func map<T>(to: T.Type) -> MLDataColumn<T>](mldatacolumn/map(to:).md)
  Creates a new column by converting this column to the given type.
- [init<T>(column: MLDataColumn<T>)](mldatacolumn/init(column:)-5rg9u.md)
  Creates a new column of integers from a given column whose elements can be converted to integers.
- [init<T>(column: MLDataColumn<T>)](mldatacolumn/init(column:)-2rxtu.md)
  Creates a new column of arrays of integers from a given column whose elements can be converted to an array of integers.
- [init<T>(column: MLDataColumn<T>)](mldatacolumn/init(column:)-86ge9.md)
  Creates a new column of doubles from a given column whose elements can be converted to doubles.
- [init<T>(column: MLDataColumn<T>)](mldatacolumn/init(column:)-23pmx.md)
  Creates a new column of arrays of doubles from a given column whose elements can be converted to an array of doubles.
- [init<T>(column: MLDataColumn<T>)](mldatacolumn/init(column:)-ztkv.md)
  Creates a new column of strings from a given column whose elements can be converted to strings.
- [init<T>(column: MLDataColumn<T>)](mldatacolumn/init(column:)-8uzuq.md)
  Creates a new column of arrays of strings from a given column whose elements can be converted to an array of strings.
- [init<T>(column: MLDataColumn<T>)](mldatacolumn/init(column:)-855l9.md)
  Creates a new column of machine learning sequences from a given column whose elements can be converted to sequences.
- [init<T>(column: MLDataColumn<T>)](mldatacolumn/init(column:)-s8g5.md)
  Creates a new column of machine learning dictionaries from a given column whose elements can be converted to dictionaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/init(column:))*