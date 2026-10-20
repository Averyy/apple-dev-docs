# SAError.Code

**Framework**: SafetyKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum SAErrorCode : NSInteger;
```

## Topics

### Determining the error type
- [SAError.Code.invalidArgument](./code/invalidargument.md)
  The passed argument is invalid.
- [SAError.Code.notAllowed](./code/notallowed.md)
  The system restricts the feature on this iPhone at the current time.
- [SAError.Code.notAuthorized](./code/notauthorized.md)
  The app isn’t authorized to perform the requested operation.
- [SAError.Code.operationFailed](./code/operationfailed.md)
  The requested operation failed; retrying may succeed.
### Initializers
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

### Handling errors
- [let SAErrorDomain: String](../saerrordomain.md)
  The domain for error objects that SafetyKit produces.
- [struct SAError](../saerror.md)
  An error reported by SafetyKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/saerror/code)*