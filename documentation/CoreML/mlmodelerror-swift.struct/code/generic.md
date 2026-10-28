# MLModelError.Code.generic

**Framework**: Core ML  
**Kind**: case  
**Role**: Case

An error code for runtime issues that don’t apply to the other error codes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case generic
```

```c
MLModelErrorGeneric
```

## Discussion

Core ML typically throws (Swift) or returns (Objective-C) this error when it encounters an internal problem.

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
- [MLModelError.Code.update](./update.md)
  An error code for problems related to on-device model updates.
- [MLModelError.Code.customLayer](./customlayer.md)
  An error code for problems related to custom layers.
- [MLModelError.Code.customModel](./custommodel.md)
  An error code for problems related to custom models.
- [MLModelError.Code.io](./io.md)
  An error code for problems related to the system’s input or output.
- [MLModelError.Code.predictionCancelled](./predictioncancelled.md)
  An error code for problems related to canceling the prediction before it completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelerror-swift.struct/code/generic)*