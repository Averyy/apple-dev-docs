# MLCreateError.incompatibleParameters(parameter:originalValue:newValue:)

**Framework**: Create ML  
**Kind**: case

An error that indicates the training session parameters are incompatible.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case incompatibleParameters(parameter: String, originalValue: String, newValue: String)
```

## See Also

- [MLCreateError.cancelled](mlcreateerror/cancelled.md)
  An error that indicates you canceled the training session.
- [MLCreateError.modifiedTrainingData](mlcreateerror/modifiedtrainingdata.md)
  An error that indicates the training data is different from the data when you created the session.
- [MLCreateError.io(reason:)](mlcreateerror/io(reason:).md)
  An error that indicates an I/O failure.
- [MLCreateError.type(reason:)](mlcreateerror/type(reason:).md)
  An error that indicates a missing or incorrect type.
- [MLCreateError.generic(reason:)](mlcreateerror/generic(reason:).md)
  An error that indicates a failure not covered by one of the other errors.
- [let MLCreateErrorDomain: String](mlcreateerrordomain.md)
  A global constant that defines the domain for Create ML errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlcreateerror/incompatibleparameters(parameter:originalvalue:newvalue:))*