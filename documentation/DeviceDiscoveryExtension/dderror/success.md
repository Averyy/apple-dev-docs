# success

**Framework**: DeviceDiscoveryExtension  
**Kind**: property  
**Role**: Type Property

An error that indicates an operation succeeds.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
static var success: DDError.Code { get }
```

## See Also

### Identifying an error cause
- [DDError.Code](./code.md)
  Codes that identify errors that can occur during the framework’s use.
- [static var unknown: DDError.Code](./unknown.md)
  An error that indicates an uncategorized problem.
- [static var badParameter: DDError.Code](./badparameter.md)
  An error that indicates the framework doesn’t support a parameter that the extension provides.
- [static var unsupported: DDError.Code](./unsupported.md)
  An error that indicates an unsupported configuration.
- [static var timeout: DDError.Code](./timeout.md)
  An error that indicates a timeout occurs.
- [static var `internal`: DDError.Code](./internal.md)
  An error that indicates a problem of internal origin.
- [static var missingEntitlement: DDError.Code](./missingentitlement.md)
  An error that indicates that the app extension lacks a required entitlement.
- [static var permission: DDError.Code](./permission.md)
  An error that indicates the app extension lacks necessary permissions.
- [static var next: DDError.Code](./next.md)
  An error the framework reserves for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dderror/success)*