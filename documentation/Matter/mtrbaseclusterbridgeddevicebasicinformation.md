# MTRBaseClusterBridgedDeviceBasicInformation

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
class MTRBaseClusterBridgedDeviceBasicInformation
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterbridgeddevicebasicinformation/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeattributelist(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeclusterrevision(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeHardwareVersion(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributehardwareversion(completion:).md)
- [func readAttributeHardwareVersionString(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributehardwareversionstring(completion:).md)
- [func readAttributeManufacturingDate(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributemanufacturingdate(completion:).md)
- [func readAttributeNodeLabel(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributenodelabel(completion:).md)
- [func readAttributePartNumber(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributepartnumber(completion:).md)
- [func readAttributeProductAppearance(completion: (MTRBridgedDeviceBasicInformationClusterProductAppearanceStruct?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeproductappearance(completion:).md)
- [func readAttributeProductLabel(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeproductlabel(completion:).md)
- [func readAttributeProductName(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeproductname(completion:).md)
- [func readAttributeProductURL(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeproducturl(completion:).md)
- [func readAttributeReachable(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributereachable(completion:).md)
- [func readAttributeSerialNumber(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeserialnumber(completion:).md)
- [func readAttributeSoftwareVersion(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributesoftwareversion(completion:).md)
- [func readAttributeSoftwareVersionString(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributesoftwareversionstring(completion:).md)
- [func readAttributeUniqueID(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeuniqueid(completion:).md)
- [func readAttributeVendorID(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributevendorid(completion:).md)
- [func readAttributeVendorName(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributevendorname(completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeHardwareVersion(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributehardwareversion(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeHardwareVersionString(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributehardwareversionstring(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeManufacturingDate(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributemanufacturingdate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNodeLabel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributenodelabel(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePartNumber(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributepartnumber(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeProductAppearance(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRBridgedDeviceBasicInformationClusterProductAppearanceStruct?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeproductappearance(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeProductLabel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeproductlabel(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeProductName(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeproductname(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeProductURL(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeproducturl(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeReachable(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributereachable(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSerialNumber(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeserialnumber(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSoftwareVersion(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributesoftwareversion(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSoftwareVersionString(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributesoftwareversionstring(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUniqueID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeuniqueid(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeVendorID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributevendorid(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeVendorName(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributevendorname(with:subscriptionestablished:reporthandler:).md)
- [func writeAttributeNodeLabel(withValue: String, completion: MTRStatusCompletion)](mtrbaseclusterbridgeddevicebasicinformation/writeattributenodelabel(withvalue:completion:).md)
- [func writeAttributeNodeLabel(withValue: String, params: MTRWriteParams?, completion: MTRStatusCompletion)](mtrbaseclusterbridgeddevicebasicinformation/writeattributenodelabel(withvalue:params:completion:).md)
- [func keepActive(with: MTRBridgedDeviceBasicInformationClusterKeepActiveParams, completion: MTRStatusCompletion)](mtrbaseclusterbridgeddevicebasicinformation/keepactive(with:completion:).md)
  Command KeepActive
- [func readAttributeProductID(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeproductid(completion:).md)
- [func subscribeAttributeProductID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/subscribeattributeproductid(with:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeHardwareVersion(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributehardwareversion(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeHardwareVersionString(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributehardwareversionstring(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeManufacturingDate(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributemanufacturingdate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeNodeLabel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributenodelabel(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePartNumber(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributepartnumber(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeProductAppearance(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRBridgedDeviceBasicInformationClusterProductAppearanceStruct?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeproductappearance(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeProductLabel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeproductlabel(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeProductName(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeproductname(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeProductURL(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeproducturl(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeReachable(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributereachable(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSerialNumber(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeserialnumber(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSoftwareVersion(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributesoftwareversion(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSoftwareVersionString(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributesoftwareversionstring(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeUniqueID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeuniqueid(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeVendorID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributevendorid(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeVendorName(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributevendorname(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeProductID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbridgeddevicebasicinformation/readattributeproductid(withclusterstatecache:endpoint:queue:completion:).md)

## Relationships

### Inherits From
- [MTRGenericBaseCluster](mtrgenericbasecluster.md)
### Inherited By
- [MTRBaseClusterBridgedDeviceBasic](mtrbaseclusterbridgeddevicebasic.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbridgeddevicebasicinformation)*