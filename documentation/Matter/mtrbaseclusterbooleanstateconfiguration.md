# MTRBaseClusterBooleanStateConfiguration

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
class MTRBaseClusterBooleanStateConfiguration
```

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterbooleanstateconfiguration/init(device:endpointid:queue:).md)
### Instance Methods
- [func enableDisableAlarm(with: MTRBooleanStateConfigurationClusterEnableDisableAlarmParams, completion: ((any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/enabledisablealarm(with:completion:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAlarmsActive(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributealarmsactive(completion:).md)
- [func readAttributeAlarmsEnabled(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributealarmsenabled(completion:).md)
- [func readAttributeAlarmsSupported(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributealarmssupported(completion:).md)
- [func readAttributeAlarmsSuppressed(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributealarmssuppressed(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributeattributelist(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributeclusterrevision(completion:).md)
- [func readAttributeCurrentSensitivityLevel(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributecurrentsensitivitylevel(completion:).md)
- [func readAttributeDefaultSensitivityLevel(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributedefaultsensitivitylevel(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeSensorFault(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributesensorfault(completion:).md)
- [func readAttributeSupportedSensitivityLevels(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributesupportedsensitivitylevels(completion:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAlarmsActive(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/subscribeattributealarmsactive(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAlarmsEnabled(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/subscribeattributealarmsenabled(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAlarmsSupported(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/subscribeattributealarmssupported(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAlarmsSuppressed(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/subscribeattributealarmssuppressed(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCurrentSensitivityLevel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/subscribeattributecurrentsensitivitylevel(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeDefaultSensitivityLevel(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/subscribeattributedefaultsensitivitylevel(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSensorFault(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/subscribeattributesensorfault(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSupportedSensitivityLevels(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/subscribeattributesupportedsensitivitylevels(with:subscriptionestablished:reporthandler:).md)
- [func suppressAlarm(with: MTRBooleanStateConfigurationClusterSuppressAlarmParams, completion: ((any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/suppressalarm(with:completion:).md)
- [func writeAttributeCurrentSensitivityLevel(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/writeattributecurrentsensitivitylevel(withvalue:completion:).md)
- [func writeAttributeCurrentSensitivityLevel(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/writeattributecurrentsensitivitylevel(withvalue:params:completion:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAlarmsActive(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributealarmsactive(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAlarmsEnabled(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributealarmsenabled(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAlarmsSupported(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributealarmssupported(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAlarmsSuppressed(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributealarmssuppressed(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCurrentSensitivityLevel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributecurrentsensitivitylevel(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeDefaultSensitivityLevel(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributedefaultsensitivitylevel(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSensorFault(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributesensorfault(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSupportedSensitivityLevels(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterbooleanstateconfiguration/readattributesupportedsensitivitylevels(withclusterstatecache:endpoint:queue:completion:).md)

## Relationships

### Inherits From
- [MTRGenericBaseCluster](mtrgenericbasecluster.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbooleanstateconfiguration)*