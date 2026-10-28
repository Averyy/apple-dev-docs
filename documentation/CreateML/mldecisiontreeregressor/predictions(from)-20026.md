# predictions(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Predicts the target value from the provided data.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 13.0
- visionOS 1.0+

> **Deprecated**: Use DataFrame instead of MLDataTable.

## Declaration

```swift
func predictions(from data: MLDataTable) throws -> MLUntypedColumn
```

**Other overloads**:

```swift
func predictions(from data: DataFrame) throws -> AnyColumn
```

## Return Value

A column of values predicted by the regressor.

## Parameters

- `data`: The data you want the model to make predictions from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeregressor/predictions(from:)-20026)*