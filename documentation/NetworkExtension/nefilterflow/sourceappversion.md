# sourceAppVersion

**Framework**: Network Extension  
**Kind**: property

The short version string of the app that is the source of the flow.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var sourceAppVersion: String? { get }
```

#### Discussion

This property is `nil` if the app info is unavailable.

## See Also

- [var sourceAppUniqueIdentifier: Data?](nefilterflow/sourceappuniqueidentifier.md)
  A byte string that uniquely identifies the binary for each build of the app that is the source of the flow.
- [var sourceAppIdentifier: String?](nefilterflow/sourceappidentifier.md)
  A string containing the identifier of the source app of the flow.
- [var sourceAppAuditToken: Data?](nefilterflow/sourceappaudittoken.md)
  The audit token of the source application of the flow.
- [var sourceProcessAuditToken: Data?](nefilterflow/sourceprocessaudittoken.md)
  The audit token of the process that created the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterflow/sourceappversion)*