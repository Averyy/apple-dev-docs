# init(xpcRepresentation:)

**Framework**: BrowserEngineKit  
**Kind**: init  
**Role**: Initializer

Creates a transaction coordinator from an XPC object.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
init(xpcRepresentation: xpc_object_t?) throws
```

```objc
+ (BELayerHierarchyHostingTransactionCoordinator *) coordinatorWithXPCRepresentation:(xpc_object_t) xpcRepresentation error:(NSError **) error;
```

## Discussion

This initializer can fail and throw an error if the `xpcRepresentation` doesn’t represent a transaction coordinator.

## Parameters

- `xpcRepresentation`: An XPC object describing the transaction coordinator to initialize.

## See Also

### Sharing a transaction coordinator using XPC
- [func createXPCRepresentation() -> xpc_object_t](./createxpcrepresentation%28%29.md)
  Creates a representation of the transaction coordinator that you send to another process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingtransactioncoordinator/init(xpcrepresentation:))*