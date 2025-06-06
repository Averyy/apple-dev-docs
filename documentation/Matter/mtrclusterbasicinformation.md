# MTRClusterBasicInformation

**Framework**: Matter  
**Kind**: class

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

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterbasicinformation/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributeattributelist(with:).md)
- [func readAttributeCapabilityMinima(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributecapabilityminima(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributeclusterrevision(with:).md)
- [func readAttributeDataModelRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributedatamodelrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributegeneratedcommandlist(with:).md)
- [func readAttributeHardwareVersion(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributehardwareversion(with:).md)
- [func readAttributeHardwareVersionString(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributehardwareversionstring(with:).md)
- [func readAttributeLocalConfigDisabled(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributelocalconfigdisabled(with:).md)
- [func readAttributeLocation(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributelocation(with:).md)
- [func readAttributeManufacturingDate(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributemanufacturingdate(with:).md)
- [func readAttributeNodeLabel(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributenodelabel(with:).md)
- [func readAttributePartNumber(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributepartnumber(with:).md)
- [func readAttributeProductAppearance(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributeproductappearance(with:).md)
- [func readAttributeProductID(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributeproductid(with:).md)
- [func readAttributeProductLabel(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributeproductlabel(with:).md)
- [func readAttributeProductName(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributeproductname(with:).md)
- [func readAttributeProductURL(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributeproducturl(with:).md)
- [func readAttributeReachable(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributereachable(with:).md)
- [func readAttributeSerialNumber(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributeserialnumber(with:).md)
- [func readAttributeSoftwareVersion(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributesoftwareversion(with:).md)
- [func readAttributeSoftwareVersionString(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributesoftwareversionstring(with:).md)
- [func readAttributeUniqueID(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributeuniqueid(with:).md)
- [func readAttributeVendorID(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributevendorid(with:).md)
- [func readAttributeVendorName(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributevendorname(with:).md)
- [func writeAttributeLocalConfigDisabled(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterbasicinformation/writeattributelocalconfigdisabled(withvalue:expectedvalueinterval:).md)
- [func writeAttributeLocalConfigDisabled(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterbasicinformation/writeattributelocalconfigdisabled(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeLocation(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterbasicinformation/writeattributelocation(withvalue:expectedvalueinterval:).md)
- [func writeAttributeLocation(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterbasicinformation/writeattributelocation(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeNodeLabel(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterbasicinformation/writeattributenodelabel(withvalue:expectedvalueinterval:).md)
- [func writeAttributeNodeLabel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterbasicinformation/writeattributenodelabel(withvalue:expectedvalueinterval:params:).md)
- [func readAttributeMaxPathsPerInvoke(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributemaxpathsperinvoke(with:).md)
- [func readAttributeSpecificationVersion(with: MTRReadParams?) -> [String : Any]?](mtrclusterbasicinformation/readattributespecificationversion(with:).md)

## Relationships

### Inherits From
- [MTRGenericCluster](mtrgenericcluster.md)
### Inherited By
- [MTRClusterBasic](mtrclusterbasic.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterbasicinformation)*