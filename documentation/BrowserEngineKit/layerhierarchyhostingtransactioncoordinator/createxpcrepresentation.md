# createXPCRepresentation()

**Framework**: BrowserEngineKit  
**Kind**: method

Creates a representation of the transaction coordinator you send to another process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func createXPCRepresentation() -> xpc_object_t
```

## See Also

- [init?(coder: NSCoder)](layerhierarchyhostingtransactioncoordinator/init(coder:).md)
  Creates a transaction coordinator from an encoded representation.
- [init(xpcRepresentation: xpc_object_t?) throws](layerhierarchyhostingtransactioncoordinator/init(xpcrepresentation:).md)
  Creates a transaction coordinator from an XPC object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/createxpcrepresentation())*