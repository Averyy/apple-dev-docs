# MTRCommissioneeInfo

**Framework**: Matter  
**Kind**: class

Information read from the commissionee device during commissioning.

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
class MTRCommissioneeInfo
```

## Topics

### Instance Properties
- [var attributes: [MTRAttributePath : [String : Any]]?](mtrcommissioneeinfo/attributes.md)
  Attributes that were read from the commissionee.  This will contain the following, if they are available:
- [var endpointsById: [NSNumber : MTREndpointInfo]?](mtrcommissioneeinfo/endpointsbyid.md)
  Endpoint information for all endpoints of the commissionee. Will be present only if readEndpointInformation is set to YES on MTRCommissioningParameters.
- [var productIdentity: MTRProductIdentity](mtrcommissioneeinfo/productidentity.md)
  The product identity (VID / PID) of the commissionee.
- [var rootEndpoint: MTREndpointInfo?](mtrcommissioneeinfo/rootendpoint.md)
  Endpoint information for the root endpoint of the commissionee. Will be present only if readEndpointInformation is set to YES on MTRCommissioningParameters.

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioneeinfo)*