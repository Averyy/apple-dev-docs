# init(column:)

**Framework**: Create ML  
**Kind**: init

Creates a new column of machine learning dictionaries from a given column whose elements can be converted to dictionaries.

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

Use this initializer to create a column of dictionaries from another column. Start by creating a column that is convertible to a column of dictionaries.

```swift
let intDictionaryString = "{1:\"one\", 2:\"two\", 3:\"three\"}"
let intDictionaryString2 = "{4:\"four\", 5:\"five\", 6:\"six\"}"
let stringsColumn = MLDataColumn([intDictionaryString, intDictionaryString2])

print(stringsColumn) // Prints ["{1:"one", 2:"two", 3:"three"}", "{4:"four", 5:"five", 6:"six"}"]
```

Then use [`init(column:)`](mldatacolumn/init(column:)-s8g5.md) to convert the column to a column of dictionaries.

```swift
let dictionaryColumn = MLDataColumn<MLDataValue.DictionaryType>(column: stringsColumn)
print(dictionaryColumn) // Prints [[1: one, 2: two, 3: three], [5: five, 4: four, 6: six]]
```

## Parameters

- `column`: An   of elements convertible to  .

## See Also

- [func map<T>(to: T.Type) -> MLDataColumn<T>](mldatacolumn/map(to:).md)
  Creates a new column by converting this column to the given type.
- [init(column:)](mldatacolumn/init(column:).md)
  Creates a new column of machine learning sequences from a given column whose elements can be converted to sequences.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/init(column:)-s8g5)*