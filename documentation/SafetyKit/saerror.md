# SAError

**Framework**: SafetyKit  
**Kind**: struct

An error reported by SafetyKit.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
struct SAError
```

## Topics

### Inspecting error information
- [var localizedDescription: String](saerror/localizeddescription.md)
  Retrieve the localized description for this error.
- [static var errorDomain: String](saerror/errordomain.md)
  The domain of the error.
### Comparing errors
- [static func != (Self, Self) -> Bool](saerror/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Identifying an error cause
- [SAError.Code](saerror/code.md)
  Codes for identifying errors in SafetyKit.
- [let SAErrorDomain: String](saerrordomain.md)
  The domain for error objects that SafetyKit produces.
- [static var invalidArgument: SAError.Code](saerror/invalidargument.md)
  The method received an argument that it can’t validate.
- [static var notAllowed: SAError.Code](saerror/notallowed.md)
  The system currently restricts the feature on this device.
- [static var notAuthorized: SAError.Code](saerror/notauthorized.md)
  The system denies the app from performing the requested operation.
- [static var operationFailed: SAError.Code](saerror/operationfailed.md)
  The requested operation failed; retrying may succeed.
### Default Implementations
- [CustomNSError Implementations](saerror/customnserror-implementations.md)
- [Equatable Implementations](saerror/equatable-implementations.md)
- [Error Implementations](saerror/error-implementations.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let SAErrorDomain: String](saerrordomain.md)
  The domain for error objects that SafetyKit produces.
- [SAError.Code](saerror/code.md)
  Codes for identifying errors in SafetyKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/saerror)*