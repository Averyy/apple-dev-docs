# MTRClusterBridgedDeviceBasicInformation

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
class MTRClusterBridgedDeviceBasicInformation
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterbridgeddevicebasicinformation/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributegeneratedcommandlist(with:).md)
- [func readAttributeHardwareVersion(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributehardwareversion(with:).md)
- [func readAttributeHardwareVersionString(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributehardwareversionstring(with:).md)
- [func readAttributeManufacturingDate(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributemanufacturingdate(with:).md)
- [func readAttributeNodeLabel(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributenodelabel(with:).md)
- [func readAttributePartNumber(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributepartnumber(with:).md)
- [func readAttributeProductAppearance(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributeproductappearance(with:).md)
- [func readAttributeProductLabel(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributeproductlabel(with:).md)
- [func readAttributeProductName(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributeproductname(with:).md)
- [func readAttributeProductURL(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributeproducturl(with:).md)
- [func readAttributeReachable(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributereachable(with:).md)
- [func readAttributeSerialNumber(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributeserialnumber(with:).md)
- [func readAttributeSoftwareVersion(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributesoftwareversion(with:).md)
- [func readAttributeSoftwareVersionString(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributesoftwareversionstring(with:).md)
- [func readAttributeUniqueID(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributeuniqueid(with:).md)
- [func readAttributeVendorID(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributevendorid(with:).md)
- [func readAttributeVendorName(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributevendorname(with:).md)
- [func writeAttributeNodeLabel(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterbridgeddevicebasicinformation/writeattributenodelabel(withvalue:expectedvalueinterval:).md)
- [func writeAttributeNodeLabel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterbridgeddevicebasicinformation/writeattributenodelabel(withvalue:expectedvalueinterval:params:).md)
- [func keepActive(with: MTRBridgedDeviceBasicInformationClusterKeepActiveParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterbridgeddevicebasicinformation/keepactive(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeProductID(with: MTRReadParams?) -> [String : Any]?](mtrclusterbridgeddevicebasicinformation/readattributeproductid(with:).md)

## Relationships

### Inherits From
- [MTRGenericCluster](mtrgenericcluster.md)
### Inherited By
- [MTRClusterBridgedDeviceBasic](mtrclusterbridgeddevicebasic.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterbridgeddevicebasicinformation)*