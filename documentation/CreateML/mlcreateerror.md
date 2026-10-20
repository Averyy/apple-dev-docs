# MLCreateError

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

The errors Create ML throws while performing various operations, such as training models, making predictions, writing models to a file system, and so on.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum MLCreateError
```

## Topics

### Identifying errors
- [MLCreateError.cancelled](./mlcreateerror/cancelled.md)
  An error that indicates you canceled the training session.
- [case incompatibleParameters(parameter: String, originalValue: String, newValue: String)](./mlcreateerror/incompatibleparameters%28parameter,originalvalue,newvalue%29.md)
  An error that indicates the training session parameters are incompatible.
- [MLCreateError.modifiedTrainingData](./mlcreateerror/modifiedtrainingdata.md)
  An error that indicates the training data is different from the data when you created the session.
- [MLCreateError.io(reason:)](./mlcreateerror/io%28reason%29.md)
  An error that indicates an I/O failure.
- [MLCreateError.type(reason:)](./mlcreateerror/type%28reason%29.md)
  An error that indicates a missing or incorrect type.
- [MLCreateError.generic(reason:)](./mlcreateerror/generic%28reason%29.md)
  An error that indicates a failure not covered by one of the other errors.
- [let MLCreateErrorDomain: String](./mlcreateerrordomain.md)
  A global constant that defines the domain for Create ML errors.
### Describing errors
- [var description: String](./mlcreateerror/description.md)
  A human-readable description of the error.
- [var debugDescription: String](./mlcreateerror/debugdescription.md)
  A human-readable description of the error that’s suitable for output during debugging.
### Describing errors in a user interface
- [var errorCode: Int](./mlcreateerror/errorcode.md)
  The numeric code of this error.
- [var errorUserInfo: [String : Any]](./mlcreateerror/erroruserinfo.md)
  A dictionary that provides additional information about the error.
- [var errorDescription: String?](./mlcreateerror/errordescription.md)
  A localized, human-readable description of the error and why it occurred, if applicable.
- [var failureReason: String?](./mlcreateerror/failurereason.md)
  A localized, human-readable reason behind the failure, if applicable.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./mlcreateerror/customdebugstringconvertible-implementations.md)
- [CustomNSError Implementations](./mlcreateerror/customnserror-implementations.md)
- [CustomStringConvertible Implementations](./mlcreateerror/customstringconvertible-implementations.md)
- [LocalizedError Implementations](./mlcreateerror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomNSError](../Foundation/customnserror.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Error](../Swift/error.md)
- [Escapable](../Swift/escapable.md)
- [LocalizedError](../Foundation/localizederror.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [struct MLModelMetadata](./mlmodelmetadata.md)
  Information about a model that’s stored in a Core ML model file.
- [enum MLSplitStrategy](./mlsplitstrategy.md)
  Data partitioning approaches, typically for creating a validation dataset from a training dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlcreateerror)*