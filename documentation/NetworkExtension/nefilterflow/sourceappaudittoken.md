# sourceAppAuditToken

**Framework**: Network Extension  
**Kind**: property

The audit token of the source application of the flow.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var sourceAppAuditToken: Data? { get }
```

## See Also

- [var sourceAppUniqueIdentifier: Data?](nefilterflow/sourceappuniqueidentifier.md)
  A byte string that uniquely identifies the binary for each build of the app that is the source of the flow.
- [var sourceAppIdentifier: String?](nefilterflow/sourceappidentifier.md)
  A string containing the identifier of the source app of the flow.
- [var sourceAppVersion: String?](nefilterflow/sourceappversion.md)
  The short version string of the app that is the source of the flow.
- [var sourceProcessAuditToken: Data?](nefilterflow/sourceprocessaudittoken.md)
  The audit token of the process that created the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterflow/sourceappaudittoken)*