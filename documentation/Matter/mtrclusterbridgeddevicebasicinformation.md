# MTRClusterBridgedDeviceBasicInformation

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
class MTRClusterBridgedDeviceBasicInformation
```

```objc
@interface MTRClusterBridgedDeviceBasicInformation : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterbridgeddevicebasicinformation/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeHardwareVersion(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributehardwareversion%28with%29.md)
- [func readAttributeHardwareVersionString(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributehardwareversionstring%28with%29.md)
- [func readAttributeManufacturingDate(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributemanufacturingdate%28with%29.md)
- [func readAttributeNodeLabel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributenodelabel%28with%29.md)
- [func readAttributePartNumber(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributepartnumber%28with%29.md)
- [func readAttributeProductAppearance(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributeproductappearance%28with%29.md)
- [func readAttributeProductLabel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributeproductlabel%28with%29.md)
- [func readAttributeProductName(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributeproductname%28with%29.md)
- [func readAttributeProductURL(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributeproducturl%28with%29.md)
- [func readAttributeReachable(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributereachable%28with%29.md)
- [func readAttributeSerialNumber(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributeserialnumber%28with%29.md)
- [func readAttributeSoftwareVersion(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributesoftwareversion%28with%29.md)
- [func readAttributeSoftwareVersionString(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributesoftwareversionstring%28with%29.md)
- [func readAttributeUniqueID(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributeuniqueid%28with%29.md)
- [func readAttributeVendorID(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributevendorid%28with%29.md)
- [func readAttributeVendorName(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributevendorname%28with%29.md)
- [func writeAttributeNodeLabel(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterbridgeddevicebasicinformation/writeattributenodelabel%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeNodeLabel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterbridgeddevicebasicinformation/writeattributenodelabel%28withvalue,expectedvalueinterval,params%29.md)
- [func keepActive(with: MTRBridgedDeviceBasicInformationClusterKeepActiveParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterbridgeddevicebasicinformation/keepactive%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeProductID(with: MTRReadParams?) -> [String : Any]?](./mtrclusterbridgeddevicebasicinformation/readattributeproductid%28with%29.md)

## Relationships

### Inherits From
- [MTRGenericCluster](./mtrgenericcluster.md)
### Inherited By
- [MTRClusterBridgedDeviceBasic](./mtrclusterbridgeddevicebasic.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterbridgeddevicebasicinformation)*