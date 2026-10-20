# init(repeating:count:)

**Framework**: Create ML  
**Kind**: init

Creates a new column with a repeating element.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(repeating repeatedValue: Element, count: Int)
```

#### Discussion

Use this initializer to create a column of repeating elements with any type that conforms to [`MLDataValueConvertible`](mldatavalueconvertible.md), including integers, doubles, strings, arrays, and dictionaries.

```swift
let three5s = MLDataColumn(repeating: 5, count: 3)
print(three5s) // Prints [5, 5, 5]
```

## Parameters

- `repeatedValue`: An initial value for every element in the new column.
- `count`: A number of elements to create for the new column.

## See Also

- [init<S>(S)](mldatacolumn/init(_:).md)
  Creates a new column from a given sequence of elements.
- [init()](mldatacolumn/init.md)
  Constructs an invalid Column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/init(repeating:count:))*