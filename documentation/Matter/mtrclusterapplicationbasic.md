# MTRClusterApplicationBasic

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRClusterApplicationBasic
```

```objc
@interface MTRClusterApplicationBasic : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterapplicationbasic/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterapplicationbasic/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationbasic/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAllowedVendorList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationbasic/readattributeallowedvendorlist%28with%29.md)
- [func readAttributeApplication(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationbasic/readattributeapplication%28with%29.md)
- [func readAttributeApplicationName(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationbasic/readattributeapplicationname%28with%29.md)
- [func readAttributeApplicationVersion(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationbasic/readattributeapplicationversion%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationbasic/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationbasic/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationbasic/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationbasic/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeProductID(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationbasic/readattributeproductid%28with%29.md)
- [func readAttributeStatus(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationbasic/readattributestatus%28with%29.md)
- [func readAttributeVendorID(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationbasic/readattributevendorid%28with%29.md)
- [func readAttributeVendorName(with: MTRReadParams?) -> [String : Any]?](./mtrclusterapplicationbasic/readattributevendorname%28with%29.md)

## Relationships

### Inherits From
- [MTRGenericCluster](./mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterapplicationbasic)*