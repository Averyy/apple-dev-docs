# init(xpcRepresentation:)

**Framework**: BrowserEngineKit  
**Kind**: init

Creates a transaction coordinator from an XPC object.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
init(xpcRepresentation: xpc_object_t?) throws
```

#### Overview

This initializer can fail and throw an error if the `xpcRepresentation` doesn’t represent a transaction coordinator.

## Parameters

- `xpcRepresentation`: An XPC object describing the transaction coordinator to initialize.

## See Also

- [init?(coder: NSCoder)](layerhierarchyhostingtransactioncoordinator/init(coder:).md)
  Creates a transaction coordinator from an encoded representation.
- [func createXPCRepresentation() -> xpc_object_t](layerhierarchyhostingtransactioncoordinator/createxpcrepresentation.md)
  Creates a representation of the transaction coordinator you send to another process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/init(xpcrepresentation:))*