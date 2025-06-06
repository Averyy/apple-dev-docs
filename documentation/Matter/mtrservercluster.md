# MTRServerCluster

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
class MTRServerCluster
```

## Topics

### Initializers
- [init?(clusterID: NSNumber, revision: NSNumber)](mtrservercluster/init(clusterid:revision:).md)
### Instance Properties
- [var accessGrants: [MTRAccessGrant]](mtrservercluster/accessgrants.md)
- [var attributes: [MTRServerAttribute]](mtrservercluster/attributes.md)
- [var clusterID: NSNumber](mtrservercluster/clusterid.md)
- [var clusterRevision: NSNumber](mtrservercluster/clusterrevision.md)
### Instance Methods
- [func addAccessGrant(MTRAccessGrant)](mtrservercluster/addaccessgrant(_:).md)
- [func addAttribute(MTRServerAttribute) -> Bool](mtrservercluster/addattribute(_:).md)
- [func removeAccessGrant(MTRAccessGrant)](mtrservercluster/removeaccessgrant(_:).md)
### Type Methods
- [class func newDescriptor() -> Self](mtrservercluster/newdescriptor.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrservercluster)*