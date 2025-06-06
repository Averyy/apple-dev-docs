# init(coder:)

**Framework**: BrowserEngineKit  
**Kind**: init

Creates a transaction coordinator from an encoded representation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
init?(coder: NSCoder)
```

#### Overview

This initializer can fail and return `nil` if it can’t decode the data it needs from the `coder`.

## Parameters

- `coder`: An object that contains the encoded representation of the transaction coordinator.

## See Also

- [init(xpcRepresentation: xpc_object_t?) throws](layerhierarchyhostingtransactioncoordinator/init(xpcrepresentation:).md)
  Creates a transaction coordinator from an XPC object.
- [func createXPCRepresentation() -> xpc_object_t](layerhierarchyhostingtransactioncoordinator/createxpcrepresentation.md)
  Creates a representation of the transaction coordinator you send to another process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/init(coder:))*