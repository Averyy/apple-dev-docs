# operationFailed

**Framework**: SafetyKit  
**Kind**: property  
**Role**: Type Property

The requested operation failed; retrying may succeed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 10.1+

## Declaration

```swift
static var operationFailed: SAError.Code { get }
```

## See Also

### Identifying an error cause
- [SAError.Code](./code.md)
  Codes for identifying errors in SafetyKit.
- [let SAErrorDomain: String](../saerrordomain.md)
  The domain for error objects that SafetyKit produces.
- [static var invalidArgument: SAError.Code](./invalidargument.md)
  The method received an argument that it can’t validate.
- [static var notAllowed: SAError.Code](./notallowed.md)
  The system currently restricts the feature on this device.
- [static var notAuthorized: SAError.Code](./notauthorized.md)
  The system denies the app from performing the requested operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safetykit/saerror/operationfailed)*