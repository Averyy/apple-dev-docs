# MTRBaseClusterEnergyEVSE

**Framework**: Matter  
**Kind**: class

Cluster Energy EVSE

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
class MTRBaseClusterEnergyEVSE
```

#### Overview

Electric Vehicle Supply Equipment (EVSE) is equipment used to charge an Electric Vehicle (EV) or Plug-In Hybrid Electric Vehicle. This cluster provides an interface to the functionality of Electric Vehicle Supply Equipment (EVSE) management.

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterenergyevse/init(device:endpointid:queue:).md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func clearTargets(completion: ((any Error)?) -> Void)](mtrbaseclusterenergyevse/cleartargets(completion:).md)
- [func clearTargets(with: MTREnergyEVSEClusterClearTargetsParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterenergyevse/cleartargets(with:completion:).md)
  Command ClearTargets
- [func disable(completion: ((any Error)?) -> Void)](mtrbaseclusterenergyevse/disable(completion:).md)
- [func disable(with: MTREnergyEVSEClusterDisableParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterenergyevse/disable(with:completion:).md)
  Command Disable
- [func enableCharging(with: MTREnergyEVSEClusterEnableChargingParams, completion: ((any Error)?) -> Void)](mtrbaseclusterenergyevse/enablecharging(with:completion:).md)
  Command EnableCharging
- [func getTargetsWith(MTREnergyEVSEClusterGetTargetsParams?, completion: (MTREnergyEVSEClusterGetTargetsResponseParams?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/gettargetswith(_:completion:).md)
  Command GetTargets
- [func getTargetsWithCompletion((MTREnergyEVSEClusterGetTargetsResponseParams?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/gettargetswithcompletion(_:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeApproximateEVEfficiency(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributeapproximateevefficiency(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributeattributelist(completion:).md)
- [func readAttributeChargingEnabledUntil(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributechargingenableduntil(completion:).md)
- [func readAttributeCircuitCapacity(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributecircuitcapacity(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributeclusterrevision(completion:).md)
- [func readAttributeFaultState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributefaultstate(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributefeaturemap(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeMaximumChargeCurrent(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributemaximumchargecurrent(completion:).md)
- [func readAttributeMinimumChargeCurrent(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributeminimumchargecurrent(completion:).md)
- [func readAttributeNextChargeRequiredEnergy(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributenextchargerequiredenergy(completion:).md)
- [func readAttributeNextChargeStartTime(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributenextchargestarttime(completion:).md)
- [func readAttributeNextChargeTargetSoC(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributenextchargetargetsoc(completion:).md)
- [func readAttributeNextChargeTargetTime(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributenextchargetargettime(completion:).md)
- [func readAttributeRandomizationDelayWindow(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributerandomizationdelaywindow(completion:).md)
- [func readAttributeSessionDuration(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributesessionduration(completion:).md)
- [func readAttributeSessionEnergyCharged(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributesessionenergycharged(completion:).md)
- [func readAttributeSessionID(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributesessionid(completion:).md)
- [func readAttributeState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributestate(completion:).md)
- [func readAttributeSupplyState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributesupplystate(completion:).md)
- [func readAttributeUserMaximumChargeCurrent(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributeusermaximumchargecurrent(completion:).md)
- [func setTargetsWith(MTREnergyEVSEClusterSetTargetsParams, completion: ((any Error)?) -> Void)](mtrbaseclusterenergyevse/settargetswith(_:completion:).md)
  Command SetTargets
- [func startDiagnostics(completion: ((any Error)?) -> Void)](mtrbaseclusterenergyevse/startdiagnostics(completion:).md)
- [func startDiagnostics(with: MTREnergyEVSEClusterStartDiagnosticsParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterenergyevse/startdiagnostics(with:completion:).md)
  Command StartDiagnostics
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeApproximateEVEfficiency(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributeapproximateevefficiency(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeChargingEnabledUntil(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributechargingenableduntil(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeCircuitCapacity(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributecircuitcapacity(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFaultState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributefaultstate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMaximumChargeCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributemaximumchargecurrent(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeMinimumChargeCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributeminimumchargecurrent(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNextChargeRequiredEnergy(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributenextchargerequiredenergy(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNextChargeStartTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributenextchargestarttime(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNextChargeTargetSoC(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributenextchargetargetsoc(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeNextChargeTargetTime(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributenextchargetargettime(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeRandomizationDelayWindow(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributerandomizationdelaywindow(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSessionDuration(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributesessionduration(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSessionEnergyCharged(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributesessionenergycharged(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSessionID(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributesessionid(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributestate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeSupplyState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributesupplystate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeUserMaximumChargeCurrent(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/subscribeattributeusermaximumchargecurrent(with:subscriptionestablished:reporthandler:).md)
- [func writeAttributeApproximateEVEfficiency(withValue: NSNumber?, completion: ((any Error)?) -> Void)](mtrbaseclusterenergyevse/writeattributeapproximateevefficiency(withvalue:completion:).md)
- [func writeAttributeApproximateEVEfficiency(withValue: NSNumber?, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterenergyevse/writeattributeapproximateevefficiency(withvalue:params:completion:).md)
- [func writeAttributeRandomizationDelayWindow(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclusterenergyevse/writeattributerandomizationdelaywindow(withvalue:completion:).md)
- [func writeAttributeRandomizationDelayWindow(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterenergyevse/writeattributerandomizationdelaywindow(withvalue:params:completion:).md)
- [func writeAttributeUserMaximumChargeCurrent(withValue: NSNumber, completion: ((any Error)?) -> Void)](mtrbaseclusterenergyevse/writeattributeusermaximumchargecurrent(withvalue:completion:).md)
- [func writeAttributeUserMaximumChargeCurrent(withValue: NSNumber, params: MTRWriteParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterenergyevse/writeattributeusermaximumchargecurrent(withvalue:params:completion:).md)
### Type Methods
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeApproximateEVEfficiency(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributeapproximateevefficiency(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeChargingEnabledUntil(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributechargingenableduntil(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeCircuitCapacity(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributecircuitcapacity(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFaultState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributefaultstate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMaximumChargeCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributemaximumchargecurrent(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeMinimumChargeCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributeminimumchargecurrent(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeNextChargeRequiredEnergy(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributenextchargerequiredenergy(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeNextChargeStartTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributenextchargestarttime(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeNextChargeTargetSoC(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributenextchargetargetsoc(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeNextChargeTargetTime(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributenextchargetargettime(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeRandomizationDelayWindow(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributerandomizationdelaywindow(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSessionDuration(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributesessionduration(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSessionEnergyCharged(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributesessionenergycharged(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSessionID(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributesessionid(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributestate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeSupplyState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributesupplystate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeUserMaximumChargeCurrent(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterenergyevse/readattributeusermaximumchargecurrent(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterenergyevse)*