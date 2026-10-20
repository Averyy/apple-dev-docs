# MTRClusterBasicInformation

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
class MTRClusterBasicInformation
```

```objc
@interface MTRClusterBasicInformation : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterbasicinformation/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributeattributelist%28with%29.md)
- [func readAttributeCapabilityMinima(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributecapabilityminima%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributeclusterrevision%28with%29.md)
- [func readAttributeDataModelRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributedatamodelrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeHardwareVersion(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributehardwareversion%28with%29.md)
- [func readAttributeHardwareVersionString(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributehardwareversionstring%28with%29.md)
- [func readAttributeLocalConfigDisabled(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributelocalconfigdisabled%28with%29.md)
- [func readAttributeLocation(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributelocation%28with%29.md)
- [func readAttributeManufacturingDate(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributemanufacturingdate%28with%29.md)
- [func readAttributeNodeLabel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributenodelabel%28with%29.md)
- [func readAttributePartNumber(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributepartnumber%28with%29.md)
- [func readAttributeProductAppearance(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributeproductappearance%28with%29.md)
- [func readAttributeProductID(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributeproductid%28with%29.md)
- [func readAttributeProductLabel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributeproductlabel%28with%29.md)
- [func readAttributeProductName(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributeproductname%28with%29.md)
- [func readAttributeProductURL(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributeproducturl%28with%29.md)
- [func readAttributeReachable(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributereachable%28with%29.md)
- [func readAttributeSerialNumber(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributeserialnumber%28with%29.md)
- [func readAttributeSoftwareVersion(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributesoftwareversion%28with%29.md)
- [func readAttributeSoftwareVersionString(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributesoftwareversionstring%28with%29.md)
- [func readAttributeUniqueID(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributeuniqueid%28with%29.md)
- [func readAttributeVendorID(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributevendorid%28with%29.md)
- [func readAttributeVendorName(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributevendorname%28with%29.md)
- [func writeAttributeLocalConfigDisabled(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterbasicinformation/writeattributelocalconfigdisabled%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeLocalConfigDisabled(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterbasicinformation/writeattributelocalconfigdisabled%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeLocation(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterbasicinformation/writeattributelocation%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeLocation(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterbasicinformation/writeattributelocation%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeNodeLabel(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterbasicinformation/writeattributenodelabel%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeNodeLabel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterbasicinformation/writeattributenodelabel%28withvalue,expectedvalueinterval,params%29.md)
- [func readAttributeMaxPathsPerInvoke(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributemaxpathsperinvoke%28with%29.md)
- [func readAttributeSpecificationVersion(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbasicinformation/readattributespecificationversion%28with%29.md)

## Relationships

### Inherits From
- [MTRGenericCluster](./mtrgenericcluster.md)
### Inherited By
- [MTRClusterBasic](./mtrclusterbasic.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterbasicinformation)*