# DDError.Code

**Framework**: DeviceDiscoveryExtension  
**Kind**: enum  
**Role**: Enumeration

Codes that identify errors that can occur during the framework’s use.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum DDErrorCode : NSInteger;
```

#### Overview

The system returns one of these codes to describe a completed operation by invoking a [`DDErrorHandler`](../dderrorhandler.md) that the client provides.

## Topics

### Errors
- [DDError.Code.success](./code/success.md)
  An error that indicates an operation succeeds.
- [DDError.Code.unknown](./code/unknown.md)
  An error that indicates an uncategorized problem.
- [DDError.Code.badParameter](./code/badparameter.md)
  An error that indicates the framework doesn’t support a parameter that the extension provides.
- [DDError.Code.unsupported](./code/unsupported.md)
  An error that indicates an unsupported configuration.
- [DDError.Code.timeout](./code/timeout.md)
  An error that indicates a timeout occurs.
- [DDError.Code.internal](./code/internal.md)
  An error that indicates a problem of internal origin.
- [DDError.Code.missingEntitlement](./code/missingentitlement.md)
  An error that indicates that the app extension lacks a required entitlement.
- [DDError.Code.permission](./code/permission.md)
  An error that indicates the app extension lacks necessary permissions.
- [DDError.Code.next](./code/next.md)
  An error the framework reserves for future use.
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

### Errors
- [struct DDError](../dderror.md)
  An error that the framework reports.
- [typealias DDErrorHandler](../dderrorhandler.md)
  A function that executes code you provide when an operation returns an error or completes successfully.
- [typealias DDErrorOutType](../dderrorouttype.md)
  A type for framework functions that return error references.
- [let DDErrorDomain: String](../dderrordomain.md)
  A unique error domain for the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dderror/code)*