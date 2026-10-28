# sourceAppSigningIdentifier

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) NSString * sourceAppSigningIdentifier;
```

## Discussion

For all apps that are signed in the standard way using Xcode, this value is identical to the app’s bundle identifier.

## See Also

### Getting source app information
- [var sourceAppUniqueIdentifier: Data](./sourceappuniqueidentifier.md)
  A data instance that contains a unique hash value for the source application.
- [var sourceAppAuditToken: Data?](./sourceappaudittoken.md)
  The audit token of the source application of the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neflowmetadata/sourceappsigningidentifier)*