# sourceProcessAuditToken

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The audit token of the process that created the flow.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var sourceProcessAuditToken: Data? { get }
```

```objc
@property (readonly, nullable) NSData * sourceProcessAuditToken;
```

## Discussion

In cases where a system process creates the connection on behalf of a source app, this value is different from [`sourceAppAuditToken`](./sourceappaudittoken.md). In cases where the source app directly creates the connection, these values are identical.

## See Also

### Source app identification
- [var sourceAppUniqueIdentifier: Data?](./sourceappuniqueidentifier.md)
  A byte string that uniquely identifies the binary for each build of the app that is the source of the flow.
- [var sourceAppIdentifier: String?](./sourceappidentifier.md)
  A string containing the identifier of the source app of the flow.
- [var sourceAppVersion: String?](./sourceappversion.md)
  The short version string of the app that is the source of the flow.
- [var sourceAppAuditToken: Data?](./sourceappaudittoken.md)
  The audit token of the source application of the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterflow/sourceprocessaudittoken)*