# SAError.Code

**Framework**: SafetyKit  
**Kind**: enum

Codes for identifying errors in SafetyKit.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 10.1+

## Declaration

```swift
enum Code
```

## Topics

### Determining the error type
- [SAError.Code.invalidArgument](saerror/code/invalidargument.md)
  The passed argument is invalid.
- [SAError.Code.notAllowed](saerror/code/notallowed.md)
  The system restricts the feature on this iPhone at the current time.
- [SAError.Code.notAuthorized](saerror/code/notauthorized.md)
  The app isn’t authorized to perform the requested operation.
- [SAError.Code.operationFailed](saerror/code/operationfailed.md)
  The requested operation failed; retrying may succeed.
### Initializers
- [init?(rawValue: Int)](saerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let SAErrorDomain: String](saerrordomain.md)
  The domain for error objects that SafetyKit produces.
- [struct SAError](saerror.md)
  An error reported by SafetyKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/saerror/code)*