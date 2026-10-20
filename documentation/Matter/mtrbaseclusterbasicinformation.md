# MTRBaseClusterBasicInformation

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
class MTRBaseClusterBasicInformation
```

```objc
@interface MTRBaseClusterBasicInformation : MTRGenericBaseCluster
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrbaseclusterbasicinformation/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeacceptedcommandlist%28completion%29.md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeattributelist%28completion%29.md)
- [func readAttributeCapabilityMinima(completion: (MTRBasicInformationClusterCapabilityMinimaStruct?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributecapabilityminima%28completion%29.md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeclusterrevision%28completion%29.md)
- [func readAttributeDataModelRevision(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributedatamodelrevision%28completion%29.md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributefeaturemap%28completion%29.md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributegeneratedcommandlist%28completion%29.md)
- [func readAttributeHardwareVersion(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributehardwareversion%28completion%29.md)
- [func readAttributeHardwareVersionString(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributehardwareversionstring%28completion%29.md)
- [func readAttributeLocalConfigDisabled(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributelocalconfigdisabled%28completion%29.md)
- [func readAttributeLocation(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributelocation%28completion%29.md)
- [func readAttributeManufacturingDate(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributemanufacturingdate%28completion%29.md)
- [func readAttributeNodeLabel(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributenodelabel%28completion%29.md)
- [func readAttributePartNumber(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributepartnumber%28completion%29.md)
- [func readAttributeProductAppearance(completion: (MTRBasicInformationClusterProductAppearanceStruct?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeproductappearance%28completion%29.md)
- [func readAttributeProductID(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeproductid%28completion%29.md)
- [func readAttributeProductLabel(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeproductlabel%28completion%29.md)
- [func readAttributeProductName(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeproductname%28completion%29.md)
- [func readAttributeProductURL(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeproducturl%28completion%29.md)
- [func readAttributeReachable(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributereachable%28completion%29.md)
- [func readAttributeSerialNumber(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeserialnumber%28completion%29.md)
- [func readAttributeSoftwareVersion(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributesoftwareversion%28completion%29.md)
- [func readAttributeSoftwareVersionString(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributesoftwareversionstring%28completion%29.md)
- [func readAttributeUniqueID(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeuniqueid%28completion%29.md)
- [func readAttributeVendorID(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributevendorid%28completion%29.md)
- [func readAttributeVendorName(completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributevendorname%28completion%29.md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributeacceptedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributeattributelist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeCapabilityMinima(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRBasicInformationClusterCapabilityMinimaStruct?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributecapabilityminima%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributeclusterrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeDataModelRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributedatamodelrevision%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributefeaturemap%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributegeneratedcommandlist%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeHardwareVersion(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributehardwareversion%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeHardwareVersionString(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributehardwareversionstring%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLocalConfigDisabled(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributelocalconfigdisabled%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeLocation(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributelocation%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeManufacturingDate(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributemanufacturingdate%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeNodeLabel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributenodelabel%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributePartNumber(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributepartnumber%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeProductAppearance(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRBasicInformationClusterProductAppearanceStruct?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributeproductappearance%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeProductID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributeproductid%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeProductLabel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributeproductlabel%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeProductName(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributeproductname%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeProductURL(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributeproducturl%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeReachable(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributereachable%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSerialNumber(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributeserialnumber%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSoftwareVersion(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributesoftwareversion%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSoftwareVersionString(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributesoftwareversionstring%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeUniqueID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributeuniqueid%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeVendorID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributevendorid%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeVendorName(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributevendorname%28with,subscriptionestablished,reporthandler%29.md)
- [func writeAttributeLocalConfigDisabled(withValue: NSNumber, completion: ((any Error)?) -> Void)](./mtrbaseclusterbasicinformation/writeattributelocalconfigdisabled%28withvalue,completion%29.md)
- [func writeAttributeLocalConfigDisabled(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbasicinformation/writeattributelocalconfigdisabled%28withvalue,params,completion%29.md)
- [func writeAttributeLocation(withValue: String, completion: ((any Error)?) -> Void)](./mtrbaseclusterbasicinformation/writeattributelocation%28withvalue,completion%29.md)
- [func writeAttributeLocation(withValue: String, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbasicinformation/writeattributelocation%28withvalue,params,completion%29.md)
- [func writeAttributeNodeLabel(withValue: String, completion: ((any Error)?) -> Void)](./mtrbaseclusterbasicinformation/writeattributenodelabel%28withvalue,completion%29.md)
- [func writeAttributeNodeLabel(withValue: String, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](./mtrbaseclusterbasicinformation/writeattributenodelabel%28withvalue,params,completion%29.md)
- [func readAttributeMaxPathsPerInvoke(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributemaxpathsperinvoke%28completion%29.md)
- [func readAttributeSpecificationVersion(completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributespecificationversion%28completion%29.md)
- [func subscribeAttributeMaxPathsPerInvoke(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributemaxpathsperinvoke%28with,subscriptionestablished,reporthandler%29.md)
- [func subscribeAttributeSpecificationVersion(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/subscribeattributespecificationversion%28with,subscriptionestablished,reporthandler%29.md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeacceptedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeattributelist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeCapabilityMinima(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRBasicInformationClusterCapabilityMinimaStruct?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributecapabilityminima%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeclusterrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeDataModelRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributedatamodelrevision%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributefeaturemap%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributegeneratedcommandlist%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeHardwareVersion(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributehardwareversion%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeHardwareVersionString(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributehardwareversionstring%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeLocalConfigDisabled(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributelocalconfigdisabled%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeLocation(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributelocation%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeManufacturingDate(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributemanufacturingdate%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeNodeLabel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributenodelabel%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributePartNumber(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributepartnumber%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeProductAppearance(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRBasicInformationClusterProductAppearanceStruct?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeproductappearance%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeProductID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeproductid%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeProductLabel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeproductlabel%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeProductName(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeproductname%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeProductURL(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeproducturl%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeReachable(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributereachable%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSerialNumber(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeserialnumber%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSoftwareVersion(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributesoftwareversion%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSoftwareVersionString(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributesoftwareversionstring%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeUniqueID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributeuniqueid%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeVendorID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributevendorid%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeVendorName(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (String?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributevendorname%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeMaxPathsPerInvoke(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributemaxpathsperinvoke%28withclusterstatecache,endpoint,queue,completion%29.md)
- [class func readAttributeSpecificationVersion(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](./mtrbaseclusterbasicinformation/readattributespecificationversion%28withclusterstatecache,endpoint,queue,completion%29.md)

## Relationships

### Inherits From
- [MTRGenericBaseCluster](./mtrgenericbasecluster.md)
### Inherited By
- [MTRBaseClusterBasic](./mtrbaseclusterbasic.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbasicinformation)*