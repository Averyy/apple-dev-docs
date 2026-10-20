# sourceAppUniqueIdentifier

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A byte string that uniquely identifies the binary for each build of the app that is the source of the flow.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var sourceAppUniqueIdentifier: Data? { get }
```

```objc
@property (readonly, nullable) NSData * sourceAppUniqueIdentifier;
```

## See Also

### Source app identification
- [var sourceAppIdentifier: String?](./sourceappidentifier.md)
  A string containing the identifier of the source app of the flow.
- [var sourceAppVersion: String?](./sourceappversion.md)
  The short version string of the app that is the source of the flow.
- [var sourceAppAuditToken: Data?](./sourceappaudittoken.md)
  The audit token of the source application of the flow.
- [var sourceProcessAuditToken: Data?](./sourceprocessaudittoken.md)
  The audit token of the process that created the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterflow/sourceappuniqueidentifier)*