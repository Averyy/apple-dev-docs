# fillMissing(with:)

**Framework**: Create ML  
**Kind**: method

Creates a modified copy of the column such that every missing element is replaced with the given value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func fillMissing(with value: MLDataValue) -> MLUntypedColumn
```

#### Return Value

A new `MLDataColumn` column.

## Parameters

- `value`: A value to replace every undefined element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn/fillmissing(with:))*