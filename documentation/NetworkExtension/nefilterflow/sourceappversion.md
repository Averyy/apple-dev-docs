# sourceAppVersion

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, nullable) NSString * sourceAppVersion;
```

## Discussion

This property is `nil` if the app info is unavailable.

## See Also

### Source app identification
- [var sourceAppUniqueIdentifier: Data?](./sourceappuniqueidentifier.md)
  A byte string that uniquely identifies the binary for each build of the app that is the source of the flow.
- [var sourceAppIdentifier: String?](./sourceappidentifier.md)
  A string containing the identifier of the source app of the flow.
- [var sourceAppAuditToken: Data?](./sourceappaudittoken.md)
  The audit token of the source application of the flow.
- [var sourceProcessAuditToken: Data?](./sourceprocessaudittoken.md)
  The audit token of the process that created the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterflow/sourceappversion)*