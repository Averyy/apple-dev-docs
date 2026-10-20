# MTRBaseClusterBridgedDeviceBasicInformation

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
class MTRBaseClusterBridgedDeviceBasicInformation
```

```objc
@interface MTRBaseClusterBridgedDeviceBasicInformation : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterbridgeddevicebasicinformation/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeattributelist%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeclusterrevision%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeHardwareVersion(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributehardwareversion%28completion%29.md)
- [func readAttributeHardwareVersionString(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributehardwareversionstring%28completion%29.md)
- [func readAttributeManufacturingDate(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributemanufacturingdate%28completion%29.md)
- [func readAttributeNodeLabel(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributenodelabel%28completion%29.md)
- [func readAttributePartNumber(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributepartnumber%28completion%29.md)
- [func readAttributeProductAppearance(completion: (MTRBridgedDeviceBasicInformationClusterProductAppearanceStruct?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeproductappearance%28completion%29.md)
- [func readAttributeProductLabel(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeproductlabel%28completion%29.md)
- [func readAttributeProductName(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeproductname%28completion%29.md)
- [func readAttributeProductURL(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeproducturl%28completion%29.md)
- [func readAttributeReachable(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributereachable%28completion%29.md)
- [func readAttributeSerialNumber(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeserialnumber%28completion%29.md)
- [func readAttributeSoftwareVersion(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributesoftwareversion%28completion%29.md)
- [func readAttributeSoftwareVersionString(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributesoftwareversionstring%28completion%29.md)
- [func readAttributeUniqueID(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeuniqueid%28completion%29.md)
- [func readAttributeVendorID(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributevendorid%28completion%29.md)
- [func readAttributeVendorName(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributevendorname%28completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeHardwareVersion(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributehardwareversion%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeHardwareVersionString(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributehardwareversionstring%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeManufacturingDate(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributemanufacturingdate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNodeLabel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributenodelabel%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePartNumber(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributepartnumber%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeProductAppearance(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRBridgedDeviceBasicInformationClusterProductAppearanceStruct?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeproductappearance%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeProductLabel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeproductlabel%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeProductName(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeproductname%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeProductURL(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeproducturl%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeReachable(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributereachable%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSerialNumber(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeserialnumber%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSoftwareVersion(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributesoftwareversion%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSoftwareVersionString(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributesoftwareversionstring%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUniqueID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeuniqueid%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeVendorID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributevendorid%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeVendorName(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributevendorname%28with,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeNodeLabel(withValue: String, completion: ((any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/writeattributenodelabel%28withvalue,completion%29.md)
- [func writeAttributeNodeLabel(withValue: String, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/writeattributenodelabel%28withvalue,params,completion%29.md)
- [func keepActive(with: MTRBridgedDeviceBasicInformationClusterKeepActiveParams, completion: ((any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/keepactive%28with,completion%29.md)
  Command KeepActive
- [func readAttributeProductID(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeproductid%28completion%29.md)
- [func subscribeAttributeProductID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeproductid%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeHardwareVersion(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributehardwareversion%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeHardwareVersionString(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributehardwareversionstring%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeManufacturingDate(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributemanufacturingdate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeNodeLabel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributenodelabel%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePartNumber(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributepartnumber%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeProductAppearance(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRBridgedDeviceBasicInformationClusterProductAppearanceStruct?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeproductappearance%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeProductLabel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeproductlabel%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeProductName(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeproductname%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeProductURL(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeproducturl%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeReachable(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributereachable%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSerialNumber(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeserialnumber%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSoftwareVersion(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributesoftwareversion%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSoftwareVersionString(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributesoftwareversionstring%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeUniqueID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeuniqueid%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeVendorID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributevendorid%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeVendorName(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributevendorname%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeProductID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbridgeddevicebasicinformation/readattributeproductid%28withclusterstatecache,endpoint,queue,completion%29.md)

## Relationships

### Inherits From
- [MTRGenericBaseCluster](./mtrgenericbasecluster.md)
### Inherited By
- [MTRBaseClusterBridgedDeviceBasic](./mtrbaseclusterbridgeddevicebasic.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbridgeddevicebasicinformation)*