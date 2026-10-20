# init(_:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a new column from a given sequence of elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init<S>(_ source: S) where Element == S.Element, S : Sequence
```

#### Discussion

Use this initializer to create a column from a sequence of any type that conforms to [`MLDataValueConvertible`](../mldatavalueconvertible.md).

```swift
let sequenceColumn = MLDataColumn([2, 3, 5, 7, 11])
print(sequenceColumn) // Prints [2, 3, 5, 7, 11]
```

## Parameters

- `source`: A sequence of elements for the new column.

## See Also

### Creating a data column
- [init(repeating:count:)](./init%28repeating,count%29.md)
  Creates a new column with a repeating element.
- [init()](./init%28%29.md)
  Constructs an invalid Column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/init(_:))*