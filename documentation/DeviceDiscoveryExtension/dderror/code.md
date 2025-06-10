# DDError.Code

**Framework**: DeviceDiscoveryExtension  
**Kind**: enum

Codes that identify errors that can occur during the framework’s use.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

#### Overview

The system returns one of these codes to describe a completed operation by invoking a [`DDErrorHandler`](dderrorhandler.md) that the client provides.

## Topics

### Errors
- [DDError.Code.success](dderror/code/success.md)
  An error that indicates an operation succeeds.
- [DDError.Code.unknown](dderror/code/unknown.md)
  An error that indicates an uncategorized problem.
- [DDError.Code.badParameter](dderror/code/badparameter.md)
  An error that indicates the framework doesn’t support a parameter that the extension provides.
- [DDError.Code.unsupported](dderror/code/unsupported.md)
  An error that indicates an unsupported configuration.
- [DDError.Code.timeout](dderror/code/timeout.md)
  An error that indicates a timeout occurs.
- [DDError.Code.internal](dderror/code/internal.md)
  An error that indicates a problem of internal origin.
- [DDError.Code.missingEntitlement](dderror/code/missingentitlement.md)
  An error that indicates that the app extension lacks a required entitlement.
- [DDError.Code.permission](dderror/code/permission.md)
  An error that indicates the app extension lacks necessary permissions.
- [DDError.Code.next](dderror/code/next.md)
  An error the framework reserves for future use.
### Initializers
- [init?(rawValue: Int)](dderror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct DDError](dderror.md)
  An error that the framework reports.
- [typealias DDErrorHandler](dderrorhandler.md)
  A function that executes code you provide when an operation returns an error or completes successfully.
- [typealias DDErrorOutType](dderrorouttype.md)
  A type for framework functions that return error references.
- [let DDErrorDomain: String](dderrordomain.md)
  A unique error domain for the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dderror/code)*