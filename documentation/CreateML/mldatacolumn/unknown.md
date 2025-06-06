# ||(_:_:)

**Framework**: Create ML  
**Kind**: op

Creates a column of Booleans by performing a logical OR operation on each element in the first column with the corresponding element in the second column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func || (a: MLDataColumn<Bool>, b: MLDataColumn<Bool>) -> MLDataColumn<Bool>
```

#### Return Value

A new column of Booleans if the columns are the same size; otherwise an invalid column.

## Parameters

- `a`: A column of Booleans.
- `b`: A column of Booleans.

## See Also

- [static func && (MLDataColumn<Bool>, MLDataColumn<Bool>) -> MLDataColumn<Bool>](mldatacolumn/&&(_:_:).md)
  Creates a column of Booleans by performing a logical AND operation on each element in the first column with the corresponding element in the second column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/__(_:_:))*