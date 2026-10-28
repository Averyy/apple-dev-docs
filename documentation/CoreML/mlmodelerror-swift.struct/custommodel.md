# customModel

**Framework**: Core ML  
**Kind**: property  
**Role**: Type Property

An error code for problems related to custom models.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
static var customModel: MLModelError.Code { get }
```

## Discussion

Core ML typically throws this error when the custom model has a programming mistake. For example, a custom model’s prediction method fails with this error code if Core ML can’t find the custom model’s implementation.

## See Also

### Error Codes
- [static var featureType: MLModelError.Code](./featuretype.md)
  An error code for problems related to model features.
- [static var parameters: MLModelError.Code](./parameters.md)
  An error code for problems related to model parameters.
- [static var modelCollection: MLModelError.Code](./modelcollection.md)
  An error code for problems related to retrieving a model collection from the deployment system.
- [static var modelDecryptionKeyFetch: MLModelError.Code](./modeldecryptionkeyfetch.md)
  An error code for problems related to retrieving a model’s decryption key.
- [static var modelDecryption: MLModelError.Code](./modeldecryption.md)
  An error code for problems related to decrypting models.
- [static var update: MLModelError.Code](./update.md)
  An error code for problems related to on-device model updates.
- [static var customLayer: MLModelError.Code](./customlayer.md)
  An error code for problems related to custom layers.
- [static var io: MLModelError.Code](./io.md)
  An error code for problems related to the system’s input or output.
- [static var predictionCancelled: MLModelError.Code](./predictioncancelled.md)
  An error code for problems related to cancelling the prediction before it completes.
- [static var generic: MLModelError.Code](./generic.md)
  An error code for runtime issues that don’t apply to the other error codes.
- [MLModelError.Code](./code.md)
  Information about a Core ML model error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelerror-swift.struct/custommodel)*