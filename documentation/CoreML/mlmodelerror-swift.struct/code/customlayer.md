# MLModelError.Code.customLayer

**Framework**: Core ML  
**Kind**: case

An error code for problems related to custom layers.

**Availability**:
- iOS 11.2+
- iPadOS 11.2+
- Mac Catalyst 13.1+
- macOS 10.13.2+
- tvOS 11.2+
- visionOS 1.0+
- watchOS 4.2+

## Declaration

```swift
case customLayer
```

#### Discussion

Core ML typically throws (Swift) or returns (Objective-C) this error when the custom layer has a programming mistake. For example, a model’s prediction method fails with this error code if Core ML can’t find the custom layer’s implementation.

## See Also

- [MLModelError.Code.featureType](mlmodelerror-swift.struct/code/featuretype.md)
  An error code for problems related to model features.
- [MLModelError.Code.parameters](mlmodelerror-swift.struct/code/parameters.md)
  An error code for problems related to model parameters.
- [MLModelError.Code.modelCollection](mlmodelerror-swift.struct/code/modelcollection.md)
  An error code for problems related to retrieving a model collection from the deployment system.
- [MLModelError.Code.modelDecryptionKeyFetch](mlmodelerror-swift.struct/code/modeldecryptionkeyfetch.md)
  An error code for problems related to retrieving a model’s decryption key.
- [MLModelError.Code.modelDecryption](mlmodelerror-swift.struct/code/modeldecryption.md)
  An error code for problems related to decrypting models.
- [MLModelError.Code.update](mlmodelerror-swift.struct/code/update.md)
  An error code for problems related to on-device model updates.
- [MLModelError.Code.customModel](mlmodelerror-swift.struct/code/custommodel.md)
  An error code for problems related to custom models.
- [MLModelError.Code.io](mlmodelerror-swift.struct/code/io.md)
  An error code for problems related to the system’s input or output.
- [MLModelError.Code.predictionCancelled](mlmodelerror-swift.struct/code/predictioncancelled.md)
  An error code for problems related to canceling the prediction before it completes.
- [MLModelError.Code.generic](mlmodelerror-swift.struct/code/generic.md)
  An error code for runtime issues that don’t apply to the other error codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelerror-swift.struct/code/customlayer)*