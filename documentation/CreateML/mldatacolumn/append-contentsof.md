# append(contentsOf:)

**Framework**: Create ML  
**Kind**: method

Appends the elements of the given column to the end of this column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
mutating func append(contentsOf newColumn: MLDataColumn<Element>)
```

#### Discussion

> **Note**: The type of `newColumn` must be the same type or convertible to the same type as the column. See [`MLDataValueConvertible`](mldatavalueconvertible.md).

The type of `newColumn` must be the same type or convertible to the same type as the column. See [`MLDataValueConvertible`](mldatavalueconvertible.md).

## Parameters

- `newColumn`: A column to append.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/append(contentsof:))*