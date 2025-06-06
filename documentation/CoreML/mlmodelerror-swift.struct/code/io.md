# MLModelError.Code.io

**Framework**: Core ML  
**Kind**: case

An error code for problems related to the system’s input or output.

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
case io
```

#### Discussion

Core ML typically throws (Swift) or returns (Objective-C) this error when the file system encounters an error.

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
- [MLModelError.Code.customLayer](mlmodelerror-swift.struct/code/customlayer.md)
  An error code for problems related to custom layers.
- [MLModelError.Code.customModel](mlmodelerror-swift.struct/code/custommodel.md)
  An error code for problems related to custom models.
- [MLModelError.Code.predictionCancelled](mlmodelerror-swift.struct/code/predictioncancelled.md)
  An error code for problems related to canceling the prediction before it completes.
- [MLModelError.Code.generic](mlmodelerror-swift.struct/code/generic.md)
  An error code for runtime issues that don’t apply to the other error codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelerror-swift.struct/code/io)*