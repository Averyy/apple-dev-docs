# DDError

**Framework**: DeviceDiscoveryExtension  
**Kind**: struct

An error that the framework reports.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
struct DDError
```

## Topics

### Identifying an error cause
- [DDError.Code](dderror/code.md)
  Codes that identify errors that can occur during the framework’s use.
- [static var success: DDError.Code](dderror/success.md)
  An error that indicates an operation succeeds.
- [static var unknown: DDError.Code](dderror/unknown.md)
  An error that indicates an uncategorized problem.
- [static var badParameter: DDError.Code](dderror/badparameter.md)
  An error that indicates the framework doesn’t support a parameter that the extension provides.
- [static var unsupported: DDError.Code](dderror/unsupported.md)
  An error that indicates an unsupported configuration.
- [static var timeout: DDError.Code](dderror/timeout.md)
  An error that indicates a timeout occurs.
- [static var `internal`: DDError.Code](dderror/internal.md)
  An error that indicates a problem of internal origin.
- [static var missingEntitlement: DDError.Code](dderror/missingentitlement.md)
  An error that indicates that the app extension lacks a required entitlement.
- [static var permission: DDError.Code](dderror/permission.md)
  An error that indicates the app extension lacks necessary permissions.
- [static var next: DDError.Code](dderror/next.md)
  An error the framework reserves for future use.
### Type Properties
- [static var errorDomain: String](dderror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [DDError.Code](dderror/code.md)
  Codes that identify errors that can occur during the framework’s use.
- [typealias DDErrorHandler](dderrorhandler.md)
  A function that executes code you provide when an operation returns an error or completes successfully.
- [typealias DDErrorOutType](dderrorouttype.md)
  A type for framework functions that return error references.
- [let DDErrorDomain: String](dderrordomain.md)
  A unique error domain for the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dderror)*