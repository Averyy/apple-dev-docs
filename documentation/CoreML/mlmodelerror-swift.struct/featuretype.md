# featureType

**Framework**: Core ML  
**Kind**: property

An error code for problems related to model features.

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
static var featureType: MLModelError.Code { get }
```

#### Discussion

Core ML typically throws this error when an app sends an input feature a value that’s of an incorrect type.

## See Also

- [static var parameters: MLModelError.Code](mlmodelerror-swift.struct/parameters.md)
  An error code for problems related to model parameters.
- [static var modelCollection: MLModelError.Code](mlmodelerror-swift.struct/modelcollection.md)
  An error code for problems related to retrieving a model collection from the deployment system.
- [static var modelDecryptionKeyFetch: MLModelError.Code](mlmodelerror-swift.struct/modeldecryptionkeyfetch.md)
  An error code for problems related to retrieving a model’s decryption key.
- [static var modelDecryption: MLModelError.Code](mlmodelerror-swift.struct/modeldecryption.md)
  An error code for problems related to decrypting models.
- [static var update: MLModelError.Code](mlmodelerror-swift.struct/update.md)
  An error code for problems related to on-device model updates.
- [static var customLayer: MLModelError.Code](mlmodelerror-swift.struct/customlayer.md)
  An error code for problems related to custom layers.
- [static var customModel: MLModelError.Code](mlmodelerror-swift.struct/custommodel.md)
  An error code for problems related to custom models.
- [static var io: MLModelError.Code](mlmodelerror-swift.struct/io.md)
  An error code for problems related to the system’s input or output.
- [static var predictionCancelled: MLModelError.Code](mlmodelerror-swift.struct/predictioncancelled.md)
  An error code for problems related to cancelling the prediction before it completes.
- [static var generic: MLModelError.Code](mlmodelerror-swift.struct/generic.md)
  An error code for runtime issues that don’t apply to the other error codes.
- [MLModelError.Code](mlmodelerror-swift.struct/code.md)
  Information about a Core ML model error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelerror-swift.struct/featuretype)*