# RecoverableError

**Framework**: Foundation  
**Kind**: protocol

A specialized error that may be recoverable by presenting several potential recovery options to the user.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol RecoverableError : Error
```

## Topics

### Instance Properties
- [var recoveryOptions: [String]](recoverableerror/recoveryoptions.md)
  Provides a set of possible recovery options to present to the user.
### Instance Methods
- [func attemptRecovery(optionIndex: Int) -> Bool](recoverableerror/attemptrecovery(optionindex:).md)
  Attempt to recover from this error when the user selected the option at the given index. Returns true to indicate successful recovery, and false otherwise.
- [func attemptRecovery(optionIndex: Int, resultHandler: (Bool) -> Void)](recoverableerror/attemptrecovery(optionindex:resulthandler:).md)

## Relationships

### Inherits From
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol Error : Sendable](../Swift/Error.md)
  A type representing an error value that can be thrown.
- [class NSError](nserror.md)
  Information about an error condition including a domain, a domain-specific error code, and application-specific information.
- [protocol LocalizedError](localizederror.md)
  A specialized error that provides localized messages describing the error and why it occurred.
- [protocol CustomNSError](customnserror.md)
  A specialized error that provides a domain, error code, and user-info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/recoverableerror)*