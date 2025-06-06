# sourceAppSigningIdentifier

**Framework**: Network Extension  
**Kind**: property

A string that contains the signing identifier of the source application.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var sourceAppSigningIdentifier: String { get }
```

#### Discussion

For all apps that are signed in the standard way using Xcode, this value is identical to the app’s bundle identifier.

## See Also

- [var sourceAppUniqueIdentifier: Data](neflowmetadata/sourceappuniqueidentifier.md)
  A data instance that contains a unique hash value for the source application.
- [var sourceAppAuditToken: Data?](neflowmetadata/sourceappaudittoken.md)
  The audit token of the source application of the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neflowmetadata/sourceappsigningidentifier)*