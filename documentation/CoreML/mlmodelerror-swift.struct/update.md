# update

**Framework**: Core ML  
**Kind**: property  
**Role**: Type Property

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
static var update: MLModelError.Code { get }
```

## Discussion

Core ML typically throws this error when the update process encounters a problem at runtime, such as an [`MLMultiArray`](../mlmultiarray.md) input with an incorrect shape.

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
- [static var customLayer: MLModelError.Code](./customlayer.md)
  An error code for problems related to custom layers.
- [static var customModel: MLModelError.Code](./custommodel.md)
  An error code for problems related to custom models.
- [static var io: MLModelError.Code](./io.md)
  An error code for problems related to the system’s input or output.
- [static var predictionCancelled: MLModelError.Code](./predictioncancelled.md)
  An error code for problems related to cancelling the prediction before it completes.
- [static var generic: MLModelError.Code](./generic.md)
  An error code for runtime issues that don’t apply to the other error codes.
- [MLModelError.Code](./code.md)
  Information about a Core ML model error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelerror-swift.struct/update)*