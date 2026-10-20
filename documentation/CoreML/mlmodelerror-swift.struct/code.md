# MLModelError.Code

**Framework**: Core ML  
**Kind**: enum  
**Role**: Enumeration

Information about a Core ML model error.

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
enum Code
```

```c
enum MLModelError : NSInteger;
```

## Topics

### Error codes
- [MLModelError.Code.featureType](./code/featuretype.md)
  An error code for problems related to model features.
- [MLModelError.Code.parameters](./code/parameters.md)
  An error code for problems related to model parameters.
- [MLModelError.Code.modelCollection](./code/modelcollection.md)
  An error code for problems related to retrieving a model collection from the deployment system.
- [MLModelError.Code.modelDecryptionKeyFetch](./code/modeldecryptionkeyfetch.md)
  An error code for problems related to retrieving a model’s decryption key.
- [MLModelError.Code.modelDecryption](./code/modeldecryption.md)
  An error code for problems related to decrypting models.
- [MLModelError.Code.update](./code/update.md)
  An error code for problems related to on-device model updates.
- [MLModelError.Code.customLayer](./code/customlayer.md)
  An error code for problems related to custom layers.
- [MLModelError.Code.customModel](./code/custommodel.md)
  An error code for problems related to custom models.
- [MLModelError.Code.io](./code/io.md)
  An error code for problems related to the system’s input or output.
- [MLModelError.Code.predictionCancelled](./code/predictioncancelled.md)
  An error code for problems related to canceling the prediction before it completes.
- [MLModelError.Code.generic](./code/generic.md)
  An error code for runtime issues that don’t apply to the other error codes.
### Error domain
- [let MLModelErrorDomain: String](../mlmodelerrordomain.md)
  The domain for Core ML errors.
- [static var errorDomain: String](./errordomain.md)
### Creating a model error
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Model errors
- [struct MLModelError](../mlmodelerror-swift.struct.md)
  Information about a Core ML model error.
- [let MLModelErrorDomain: String](../mlmodelerrordomain.md)
  The domain for Core ML errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelerror-swift.struct/code)*