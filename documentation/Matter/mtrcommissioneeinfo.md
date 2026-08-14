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

### Initializers
- [init?(coder: NSCoder)](mtrcommissioneeinfo/init(coder:).md)
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
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioneeinfo)*