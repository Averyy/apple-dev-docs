# sourceAppAuditToken

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The audit token of the source application of the flow.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var sourceAppAuditToken: Data? { get }
```

```objc
@property (readonly, nullable) NSData * sourceAppAuditToken;
```

## See Also

### Source app identification
- [var sourceAppUniqueIdentifier: Data?](./sourceappuniqueidentifier.md)
  A byte string that uniquely identifies the binary for each build of the app that is the source of the flow.
- [var sourceAppIdentifier: String?](./sourceappidentifier.md)
  A string containing the identifier of the source app of the flow.
- [var sourceAppVersion: String?](./sourceappversion.md)
  The short version string of the app that is the source of the flow.
- [var sourceProcessAuditToken: Data?](./sourceprocessaudittoken.md)
  The audit token of the process that created the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterflow/sourceappaudittoken)*