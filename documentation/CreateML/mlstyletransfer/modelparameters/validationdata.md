# MLStyleTransfer.ModelParameters.ValidationData

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

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
- [MLStyleTransfer.ModelParameters.ValidationData.content(_:)](./validationdata/content%28_%29.md)
  The location of a validation image you use to validate the model.
- [MLStyleTransfer.ModelParameters.ValidationData.none](./validationdata/none.md)
  An empty validation dataset you use to skip model validation.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Describing parameters
- [MLStyleTransfer.ModelParameters.ModelAlgorithmType](./modelalgorithmtype.md)
  The style transfer training algorithm options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/modelparameters/validationdata)*