# DDErrorDomain

**Framework**: DeviceDiscoveryExtension  
**Kind**: var  
**Role**: Global Variable

A unique error domain for the framework.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
let DDErrorDomain: String
```

```c
extern NSString * const DDErrorDomain;
```

#### Discussion

For more information, see [Error domains](../CoreFoundation/error-domains.md).

## See Also

### Errors
- [struct DDError](./dderror.md)
  An error that the framework reports.
- [DDError.Code](./dderror/code.md)
  Codes that identify errors that can occur during the framework’s use.
- [typealias DDErrorHandler](./dderrorhandler.md)
  A function that executes code you provide when an operation returns an error or completes successfully.
- [typealias DDErrorOutType](./dderrorouttype.md)
  A type for framework functions that return error references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dderrordomain)*