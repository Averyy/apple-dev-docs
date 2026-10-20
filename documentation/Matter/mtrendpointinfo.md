# MTREndpointInfo

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTREndpointInfo : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./mtrendpointinfo/init%28coder%29.md)
### Instance Properties
- [var children: [MTREndpointInfo]](./mtrendpointinfo/children.md)
  The direct children of this endpoint. This excludes indirect descendants even if they are listed in the PartsList attribute of this endpoint due to the Full-Family Pattern being used. Refer to Endpoint Composition Patterns in the Matter specification for details.
- [var deviceTypes: [MTRDeviceTypeRevision]](./mtrendpointinfo/devicetypes.md)
- [var endpointID: NSNumber](./mtrendpointinfo/endpointid.md)
- [var partsList: [NSNumber]](./mtrendpointinfo/partslist.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrendpointinfo)*