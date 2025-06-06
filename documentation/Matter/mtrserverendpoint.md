# MTRServerEndpoint

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
class MTRServerEndpoint
```

## Topics

### Initializers
- [init?(endpointID: NSNumber, deviceTypes: [MTRDeviceTypeRevision])](mtrserverendpoint/init(endpointid:devicetypes:).md)
### Instance Properties
- [var accessGrants: [MTRAccessGrant]](mtrserverendpoint/accessgrants.md)
- [var deviceTypes: [MTRDeviceTypeRevision]](mtrserverendpoint/devicetypes.md)
- [var endpointID: NSNumber](mtrserverendpoint/endpointid.md)
- [var serverClusters: [MTRServerCluster]](mtrserverendpoint/serverclusters.md)
### Instance Methods
- [func addAccessGrant(MTRAccessGrant)](mtrserverendpoint/addaccessgrant(_:).md)
- [func addServerCluster(MTRServerCluster) -> Bool](mtrserverendpoint/addservercluster(_:).md)
- [func removeAccessGrant(MTRAccessGrant)](mtrserverendpoint/removeaccessgrant(_:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrserverendpoint)*