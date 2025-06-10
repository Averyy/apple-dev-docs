# MTRBaseClusterBasicInformation

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
class MTRBaseClusterBasicInformation
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterbasicinformation/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeattributelist(completion:).md)
- [func readAttributeCapabilityMinima(completion: (MTRBasicInformationClusterCapabilityMinimaStruct?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributecapabilityminima(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeclusterrevision(completion:).md)
- [func readAttributeDataModelRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributedatamodelrevision(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeHardwareVersion(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributehardwareversion(completion:).md)
- [func readAttributeHardwareVersionString(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributehardwareversionstring(completion:).md)
- [func readAttributeLocalConfigDisabled(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributelocalconfigdisabled(completion:).md)
- [func readAttributeLocation(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributelocation(completion:).md)
- [func readAttributeManufacturingDate(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributemanufacturingdate(completion:).md)
- [func readAttributeNodeLabel(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributenodelabel(completion:).md)
- [func readAttributePartNumber(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributepartnumber(completion:).md)
- [func readAttributeProductAppearance(completion: (MTRBasicInformationClusterProductAppearanceStruct?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeproductappearance(completion:).md)
- [func readAttributeProductID(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeproductid(completion:).md)
- [func readAttributeProductLabel(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeproductlabel(completion:).md)
- [func readAttributeProductName(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeproductname(completion:).md)
- [func readAttributeProductURL(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeproducturl(completion:).md)
- [func readAttributeReachable(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributereachable(completion:).md)
- [func readAttributeSerialNumber(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeserialnumber(completion:).md)
- [func readAttributeSoftwareVersion(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributesoftwareversion(completion:).md)
- [func readAttributeSoftwareVersionString(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributesoftwareversionstring(completion:).md)
- [func readAttributeUniqueID(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeuniqueid(completion:).md)
- [func readAttributeVendorID(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributevendorid(completion:).md)
- [func readAttributeVendorName(completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributevendorname(completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCapabilityMinima(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRBasicInformationClusterCapabilityMinimaStruct?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributecapabilityminima(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDataModelRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributedatamodelrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeHardwareVersion(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributehardwareversion(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeHardwareVersionString(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributehardwareversionstring(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLocalConfigDisabled(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributelocalconfigdisabled(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeLocation(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributelocation(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeManufacturingDate(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributemanufacturingdate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNodeLabel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributenodelabel(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePartNumber(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributepartnumber(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeProductAppearance(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRBasicInformationClusterProductAppearanceStruct?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributeproductappearance(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeProductID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributeproductid(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeProductLabel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributeproductlabel(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeProductName(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributeproductname(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeProductURL(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributeproducturl(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeReachable(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributereachable(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSerialNumber(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributeserialnumber(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSoftwareVersion(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributesoftwareversion(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSoftwareVersionString(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributesoftwareversionstring(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUniqueID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributeuniqueid(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeVendorID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributevendorid(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeVendorName(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributevendorname(with:subscriptionestablished:reporthandler:).md)
- [func writeAttributeLocalConfigDisabled(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclusterbasicinformation/writeattributelocalconfigdisabled(withvalue:completion:).md)
- [func writeAttributeLocalConfigDisabled(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterbasicinformation/writeattributelocalconfigdisabled(withvalue:params:completion:).md)
- [func writeAttributeLocation(withValue: String, completion: ((any Error)?) -> Void)](mtrbaseclusterbasicinformation/writeattributelocation(withvalue:completion:).md)
- [func writeAttributeLocation(withValue: String, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterbasicinformation/writeattributelocation(withvalue:params:completion:).md)
- [func writeAttributeNodeLabel(withValue: String, completion: ((any Error)?) -> Void)](mtrbaseclusterbasicinformation/writeattributenodelabel(withvalue:completion:).md)
- [func writeAttributeNodeLabel(withValue: String, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterbasicinformation/writeattributenodelabel(withvalue:params:completion:).md)
- [func readAttributeMaxPathsPerInvoke(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributemaxpathsperinvoke(completion:).md)
- [func readAttributeSpecificationVersion(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributespecificationversion(completion:).md)
- [func subscribeAttributeMaxPathsPerInvoke(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributemaxpathsperinvoke(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSpecificationVersion(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/subscribeattributespecificationversion(with:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCapabilityMinima(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRBasicInformationClusterCapabilityMinimaStruct?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributecapabilityminima(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeDataModelRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributedatamodelrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeHardwareVersion(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributehardwareversion(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeHardwareVersionString(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributehardwareversionstring(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeLocalConfigDisabled(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributelocalconfigdisabled(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeLocation(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributelocation(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeManufacturingDate(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributemanufacturingdate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeNodeLabel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributenodelabel(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePartNumber(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributepartnumber(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeProductAppearance(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRBasicInformationClusterProductAppearanceStruct?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeproductappearance(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeProductID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeproductid(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeProductLabel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeproductlabel(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeProductName(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeproductname(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeProductURL(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeproducturl(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeReachable(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributereachable(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSerialNumber(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeserialnumber(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSoftwareVersion(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributesoftwareversion(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSoftwareVersionString(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributesoftwareversionstring(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeUniqueID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributeuniqueid(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeVendorID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributevendorid(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeVendorName(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributevendorname(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMaxPathsPerInvoke(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributemaxpathsperinvoke(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSpecificationVersion(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbasicinformation/readattributespecificationversion(withclusterstatecache:endpoint:queue:completion:).md)

## Relationships

### Inherits From
- [MTRGenericBaseCluster](mtrgenericbasecluster.md)
### Inherited By
- [MTRBaseClusterBasic](mtrbaseclusterbasic.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbasicinformation)*