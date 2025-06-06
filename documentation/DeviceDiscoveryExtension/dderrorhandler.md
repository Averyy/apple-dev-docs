# DDErrorHandler

**Framework**: DeviceDiscoveryExtension  
**Kind**: typealias

A function that executes code you provide when an operation returns an error or completes successfully.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
typealias DDErrorHandler = ((any Error)?) -> Void
```

## Parameters

- `inError`: A reference that the framework assigns an error object when the operation fails. When the operation succeeds, the value may be   or  .

## See Also

- [struct DDError](dderror.md)
  An error that the framework reports.
- [DDError.Code](dderror/code.md)
  Codes that identify errors that can occur during the framework’s use.
- [typealias DDErrorOutType](dderrorouttype.md)
  A type for framework functions that return error references.
- [let DDErrorDomain: String](dderrordomain.md)
  A unique error domain for the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dderrorhandler)*