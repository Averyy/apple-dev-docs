# sourceAppUniqueIdentifier

**Framework**: Network Extension  
**Kind**: property

A data instance that contains a unique hash value for the source application.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var sourceAppUniqueIdentifier: Data { get }
```

#### Discussion

The property contains the Code Directory Hash for the application.

> **Note**:  The property’s value changes between different versions of an application.

 The property’s value changes between different versions of an application.

## See Also

- [var sourceAppSigningIdentifier: String](neflowmetadata/sourceappsigningidentifier.md)
  A string that contains the signing identifier of the source application.
- [var sourceAppAuditToken: Data?](neflowmetadata/sourceappaudittoken.md)
  The audit token of the source application of the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neflowmetadata/sourceappuniqueidentifier)*