# sourceAppIdentifier

**Framework**: Network Extension  
**Kind**: property

A string containing the identifier of the source app of the flow.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var sourceAppIdentifier: String? { get }
```

#### Discussion

This identifier remains the same for all versions and builds of the app and is unique among all apps.

## See Also

- [var sourceAppUniqueIdentifier: Data?](nefilterflow/sourceappuniqueidentifier.md)
  A byte string that uniquely identifies the binary for each build of the app that is the source of the flow.
- [var sourceAppVersion: String?](nefilterflow/sourceappversion.md)
  The short version string of the app that is the source of the flow.
- [var sourceAppAuditToken: Data?](nefilterflow/sourceappaudittoken.md)
  The audit token of the source application of the flow.
- [var sourceProcessAuditToken: Data?](nefilterflow/sourceprocessaudittoken.md)
  The audit token of the process that created the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterflow/sourceappidentifier)*