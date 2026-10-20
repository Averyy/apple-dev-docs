# MTRServerEndpoint

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
class MTRServerEndpoint
```

```objc
@interface MTRServerEndpoint : NSObject
```

## Topics

### Initializers
- [init?(endpointID: NSNumber, deviceTypes: [MTRDeviceTypeRevision])](./mtrserverendpoint/init%28endpointid,devicetypes%29.md)
### Instance Properties
- [var accessGrants: [MTRAccessGrant]](./mtrserverendpoint/accessgrants.md)
- [var deviceTypes: [MTRDeviceTypeRevision]](./mtrserverendpoint/devicetypes.md)
- [var endpointID: NSNumber](./mtrserverendpoint/endpointid.md)
- [var serverClusters: [MTRServerCluster]](./mtrserverendpoint/serverclusters.md)
### Instance Methods
- [func addAccessGrant(MTRAccessGrant)](./mtrserverendpoint/addaccessgrant%28_%29.md)
- [func addServerCluster(MTRServerCluster) -> Bool](./mtrserverendpoint/addservercluster%28_%29.md)
- [func removeAccessGrant(MTRAccessGrant)](./mtrserverendpoint/removeaccessgrant%28_%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrserverendpoint)*