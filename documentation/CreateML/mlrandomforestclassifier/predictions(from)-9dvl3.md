# predictions(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Classifies the provided data into the target categories.

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

A column of labels predicted by the classifier.

## Parameters

- `data`: The data you want the model to classify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestclassifier/predictions(from:)-9dvl3)*