# RecoverableError

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

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
- [var recoveryOptions: [String]](./recoverableerror/recoveryoptions.md)
  Provides a set of possible recovery options to present to the user.
### Instance Methods
- [func attemptRecovery(optionIndex: Int) -> Bool](./recoverableerror/attemptrecovery%28optionindex%29.md)
  Attempt to recover from this error when the user selected the option at the given index. Returns true to indicate successful recovery, and false otherwise.
- [func attemptRecovery(optionIndex: Int, resultHandler: (Bool) -> Void)](./recoverableerror/attemptrecovery%28optionindex,resulthandler%29.md)
  Attempt to recover from this error when the user selected the option at the given index. This routine must call handler and indicate whether recovery was successful (or not).

## Relationships

### Inherits From
- [Error](../Swift/error.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### User-Relevant Errors
- [protocol Error](../Swift/error.md)
  A type representing an error value that can be thrown.
- [class NSError](./nserror.md)
  Information about an error condition including a domain, a domain-specific error code, and application-specific information.
- [protocol LocalizedError](./localizederror.md)
  A specialized error that provides localized messages describing the error and why it occurred.
- [protocol CustomNSError](./customnserror.md)
  A specialized error that provides a domain, error code, and user-info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/recoverableerror)*