# MTRServerCluster

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRServerCluster : NSObject
```

## Topics

### Initializers
- [init?(clusterID: NSNumber, revision: NSNumber)](./mtrservercluster/init%28clusterid,revision%29.md)
### Instance Properties
- [var accessGrants: [MTRAccessGrant]](./mtrservercluster/accessgrants.md)
- [var attributes: [MTRServerAttribute]](./mtrservercluster/attributes.md)
- [var clusterID: NSNumber](./mtrservercluster/clusterid.md)
- [var clusterRevision: NSNumber](./mtrservercluster/clusterrevision.md)
### Instance Methods
- [func addAccessGrant(MTRAccessGrant)](./mtrservercluster/addaccessgrant%28_%29.md)
- [func addAttribute(MTRServerAttribute) -> Bool](./mtrservercluster/addattribute%28_%29.md)
- [func removeAccessGrant(MTRAccessGrant)](./mtrservercluster/removeaccessgrant%28_%29.md)
### Type Methods
- [class func newDescriptor() -> Self](./mtrservercluster/newdescriptor%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrservercluster)*