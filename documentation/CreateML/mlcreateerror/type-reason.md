# MLCreateError.type(reason:)

**Framework**: Create ML  
**Kind**: case

An error that indicates a missing or incorrect type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case type(reason: String)
```

## See Also

- [MLCreateError.cancelled](mlcreateerror/cancelled.md)
  An error that indicates you canceled the training session.
- [case incompatibleParameters(parameter: String, originalValue: String, newValue: String)](mlcreateerror/incompatibleparameters(parameter:originalvalue:newvalue:).md)
  An error that indicates the training session parameters are incompatible.
- [MLCreateError.modifiedTrainingData](mlcreateerror/modifiedtrainingdata.md)
  An error that indicates the training data is different from the data when you created the session.
- [MLCreateError.io(reason:)](mlcreateerror/io(reason:).md)
  An error that indicates an I/O failure.
- [MLCreateError.generic(reason:)](mlcreateerror/generic(reason:).md)
  An error that indicates a failure not covered by one of the other errors.
- [let MLCreateErrorDomain: String](mlcreateerrordomain.md)
  A global constant that defines the domain for Create ML errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlcreateerror/type(reason:))*