# MLModelError.Code.update

**Framework**: Core ML  
**Kind**: case  
**Role**: Case

An error code for problems related to on-device model updates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case update
```

```c
MLModelErrorUpdate
```

#### Discussion

Core ML typically throws (Swift) or returns (Objective-C) this error when the update process encounters a problem at runtime, such as an [`MLMultiArray`](../../mlmultiarray.md) input with an incorrect shape.

## See Also

### Error codes
- [MLModelError.Code.featureType](./featuretype.md)
  An error code for problems related to model features.
- [MLModelError.Code.parameters](./parameters.md)
  An error code for problems related to model parameters.
- [MLModelError.Code.modelCollection](./modelcollection.md)
  An error code for problems related to retrieving a model collection from the deployment system.
- [MLModelError.Code.modelDecryptionKeyFetch](./modeldecryptionkeyfetch.md)
  An error code for problems related to retrieving a model’s decryption key.
- [MLModelError.Code.modelDecryption](./modeldecryption.md)
  An error code for problems related to decrypting models.
- [MLModelError.Code.customLayer](./customlayer.md)
  An error code for problems related to custom layers.
- [MLModelError.Code.customModel](./custommodel.md)
  An error code for problems related to custom models.
- [MLModelError.Code.io](./io.md)
  An error code for problems related to the system’s input or output.
- [MLModelError.Code.predictionCancelled](./predictioncancelled.md)
  An error code for problems related to canceling the prediction before it completes.
- [MLModelError.Code.generic](./generic.md)
  An error code for runtime issues that don’t apply to the other error codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelerror-swift.struct/code/update)*