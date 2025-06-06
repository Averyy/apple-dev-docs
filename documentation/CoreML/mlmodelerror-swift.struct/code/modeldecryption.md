# MLModelError.Code.modelDecryption

**Framework**: Core ML  
**Kind**: case

An error code for problems related to decrypting models.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
case modelDecryption
```

#### Discussion

Core ML typically throws (Swift) or returns (Objective-C) this error when the framework can’t decrypt a model.

## See Also

- [MLModelError.Code.featureType](mlmodelerror-swift.struct/code/featuretype.md)
  An error code for problems related to model features.
- [MLModelError.Code.parameters](mlmodelerror-swift.struct/code/parameters.md)
  An error code for problems related to model parameters.
- [MLModelError.Code.modelCollection](mlmodelerror-swift.struct/code/modelcollection.md)
  An error code for problems related to retrieving a model collection from the deployment system.
- [MLModelError.Code.modelDecryptionKeyFetch](mlmodelerror-swift.struct/code/modeldecryptionkeyfetch.md)
  An error code for problems related to retrieving a model’s decryption key.
- [MLModelError.Code.update](mlmodelerror-swift.struct/code/update.md)
  An error code for problems related to on-device model updates.
- [MLModelError.Code.customLayer](mlmodelerror-swift.struct/code/customlayer.md)
  An error code for problems related to custom layers.
- [MLModelError.Code.customModel](mlmodelerror-swift.struct/code/custommodel.md)
  An error code for problems related to custom models.
- [MLModelError.Code.io](mlmodelerror-swift.struct/code/io.md)
  An error code for problems related to the system’s input or output.
- [MLModelError.Code.predictionCancelled](mlmodelerror-swift.struct/code/predictioncancelled.md)
  An error code for problems related to canceling the prediction before it completes.
- [MLModelError.Code.generic](mlmodelerror-swift.struct/code/generic.md)
  An error code for runtime issues that don’t apply to the other error codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelerror-swift.struct/code/modeldecryption)*