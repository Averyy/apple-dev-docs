# DDErrorOutType

**Framework**: DeviceDiscoveryExtension  
**Kind**: typealias  
**Role**: Type Alias

A type for framework functions that return error references.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
typealias DDErrorOutType = AutoreleasingUnsafeMutablePointer<NSError?>
```

```c
typedef NSError ** DDErrorOutType;
```

## See Also

### Errors
- [struct DDError](./dderror.md)
  An error that the framework reports.
- [DDError.Code](./dderror/code.md)
  Codes that identify errors that can occur during the framework’s use.
- [typealias DDErrorHandler](./dderrorhandler.md)
  A function that executes code you provide when an operation returns an error or completes successfully.
- [let DDErrorDomain: String](./dderrordomain.md)
  A unique error domain for the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dderrorouttype)*