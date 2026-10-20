# MTRCommissioneeInfo

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRCommissioneeInfo : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./mtrcommissioneeinfo/init%28coder%29.md)
### Instance Properties
- [var attributes: [MTRAttributePath : [String : Any]]?](./mtrcommissioneeinfo/attributes.md)
  Attributes that were read from the commissionee.  This will contain the following, if they are available:
- [var endpointsById: [NSNumber : MTREndpointInfo]?](./mtrcommissioneeinfo/endpointsbyid.md)
  Endpoint information for all endpoints of the commissionee. Will be present only if readEndpointInformation is set to YES on MTRCommissioningParameters.
- [var productIdentity: MTRProductIdentity](./mtrcommissioneeinfo/productidentity.md)
  The product identity (VID / PID) of the commissionee.
- [var rootEndpoint: MTREndpointInfo?](./mtrcommissioneeinfo/rootendpoint.md)
  Endpoint information for the root endpoint of the commissionee. Will be present only if readEndpointInformation is set to YES on MTRCommissioningParameters.

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioneeinfo)*