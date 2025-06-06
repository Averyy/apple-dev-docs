# MLStyleTransfer.ModelParameters.ValidationData

**Framework**: Create ML  
**Kind**: enum

The source of a validation dataset for a style transfer model.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum ValidationData
```

## Topics

### Designating validation data
- [MLStyleTransfer.ModelParameters.ValidationData.content(_:)](mlstyletransfer/modelparameters/validationdata/content(_:).md)
  The location of a validation image you use to validate the model.
- [MLStyleTransfer.ModelParameters.ValidationData.none](mlstyletransfer/modelparameters/validationdata/none.md)
  An empty validation dataset you use to skip model validation.
### Comparing validation data
- [static func == (MLStyleTransfer.ModelParameters.ValidationData, MLStyleTransfer.ModelParameters.ValidationData) -> Bool](mlstyletransfer/modelparameters/validationdata/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](mlstyletransfer/modelparameters/validationdata/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Default Implementations
- [Equatable Implementations](mlstyletransfer/modelparameters/validationdata/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [MLStyleTransfer.ModelParameters.ModelAlgorithmType](mlstyletransfer/modelparameters/modelalgorithmtype.md)
  The style transfer training algorithm options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/modelparameters/validationdata)*