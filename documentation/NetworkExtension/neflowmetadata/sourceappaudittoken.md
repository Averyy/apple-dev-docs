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

### Getting source app information
- [var sourceAppUniqueIdentifier: Data](./sourceappuniqueidentifier.md)
  A data instance that contains a unique hash value for the source application.
- [var sourceAppSigningIdentifier: String](./sourceappsigningidentifier.md)
  A string that contains the signing identifier of the source application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neflowmetadata/sourceappaudittoken)*