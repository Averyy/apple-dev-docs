# MTREndpointInfo

**Framework**: Matter  
**Kind**: class

Meta-data about an endpoint of a Matter node.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
class MTREndpointInfo
```

## Topics

### Instance Properties
- [var children: [MTREndpointInfo]](mtrendpointinfo/children.md)
  The direct children of this endpoint. This excludes indirect descendants even if they are listed in the PartsList attribute of this endpoint due to the Full-Family Pattern being used. Refer to Endpoint Composition Patterns in the Matter specification for details.
- [var deviceTypes: [MTRDeviceTypeRevision]](mtrendpointinfo/devicetypes.md)
- [var endpointID: NSNumber](mtrendpointinfo/endpointid.md)
- [var partsList: [NSNumber]](mtrendpointinfo/partslist.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrendpointinfo)*