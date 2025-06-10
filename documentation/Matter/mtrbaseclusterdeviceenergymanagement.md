# MTRBaseClusterDeviceEnergyManagement

**Framework**: Matter  
**Kind**: class

Cluster Device Energy Management

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
class MTRBaseClusterDeviceEnergyManagement
```

#### Overview

This cluster allows a client to manage the power draw of a device. An example of such a client could be an Energy Management System (EMS) which controls an Energy Smart Appliance (ESA).

## Topics

### Initializers
- [init?(device: MTRBaseDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrbaseclusterdeviceenergymanagement/init(device:endpointid:queue:).md)
  For all instance methods (reads, writes, commands) that take a completion, the completion will be called on the provided queue.
### Instance Methods
- [func cancelPowerAdjustRequest(completion: ((any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/cancelpoweradjustrequest(completion:).md)
- [func cancelPowerAdjustRequest(with: MTRDeviceEnergyManagementClusterCancelPowerAdjustRequestParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/cancelpoweradjustrequest(with:completion:).md)
  Command CancelPowerAdjustRequest
- [func cancelRequest(completion: ((any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/cancelrequest(completion:).md)
- [func cancelRequest(with: MTRDeviceEnergyManagementClusterCancelRequestParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/cancelrequest(with:completion:).md)
  Command CancelRequest
- [func modifyForecastRequest(with: MTRDeviceEnergyManagementClusterModifyForecastRequestParams, completion: ((any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/modifyforecastrequest(with:completion:).md)
  Command ModifyForecastRequest
- [func pauseRequest(with: MTRDeviceEnergyManagementClusterPauseRequestParams, completion: ((any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/pauserequest(with:completion:).md)
  Command PauseRequest
- [func powerAdjustRequest(with: MTRDeviceEnergyManagementClusterPowerAdjustRequestParams, completion: ((any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/poweradjustrequest(with:completion:).md)
  Command PowerAdjustRequest
- [func readAttributeAbsMaxPower(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeabsmaxpower(completion:).md)
- [func readAttributeAbsMinPower(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeabsminpower(completion:).md)
- [func readAttributeAcceptedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeacceptedcommandlist(completion:).md)
- [func readAttributeAttributeList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeattributelist(completion:).md)
- [func readAttributeClusterRevision(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeclusterrevision(completion:).md)
- [func readAttributeESACanGenerate(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeesacangenerate(completion:).md)
- [func readAttributeESAState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeesastate(completion:).md)
- [func readAttributeESAType(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeesatype(completion:).md)
- [func readAttributeFeatureMap(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributefeaturemap(completion:).md)
- [func readAttributeForecast(completion: (MTRDeviceEnergyManagementClusterForecastStruct?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeforecast(completion:).md)
- [func readAttributeGeneratedCommandList(completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributegeneratedcommandlist(completion:).md)
- [func readAttributeOptOutState(completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeoptoutstate(completion:).md)
- [func readAttributePowerAdjustmentCapability(completion: (MTRDeviceEnergyManagementClusterPowerAdjustCapabilityStruct?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributepoweradjustmentcapability(completion:).md)
- [func requestConstraintBasedForecast(with: MTRDeviceEnergyManagementClusterRequestConstraintBasedForecastParams, completion: ((any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/requestconstraintbasedforecast(with:completion:).md)
  Command RequestConstraintBasedForecast
- [func resumeRequest(completion: ((any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/resumerequest(completion:).md)
- [func resumeRequest(with: MTRDeviceEnergyManagementClusterResumeRequestParams?, completion: ((any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/resumerequest(with:completion:).md)
  Command ResumeRequest
- [func startTimeAdjustRequest(with: MTRDeviceEnergyManagementClusterStartTimeAdjustRequestParams, completion: ((any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/starttimeadjustrequest(with:completion:).md)
  Command StartTimeAdjustRequest
- [func subscribeAttributeAbsMaxPower(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/subscribeattributeabsmaxpower(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAbsMinPower(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/subscribeattributeabsminpower(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAcceptedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/subscribeattributeacceptedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeAttributeList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/subscribeattributeattributelist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeClusterRevision(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/subscribeattributeclusterrevision(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeESACanGenerate(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/subscribeattributeesacangenerate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeESAState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/subscribeattributeesastate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeESAType(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/subscribeattributeesatype(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeFeatureMap(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/subscribeattributefeaturemap(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeForecast(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRDeviceEnergyManagementClusterForecastStruct?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/subscribeattributeforecast(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeGeneratedCommandList(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/subscribeattributegeneratedcommandlist(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributeOptOutState(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/subscribeattributeoptoutstate(with:subscriptionestablished:reporthandler:).md)
- [func subscribeAttributePowerAdjustmentCapability(with: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: (MTRDeviceEnergyManagementClusterPowerAdjustCapabilityStruct?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/subscribeattributepoweradjustmentcapability(with:subscriptionestablished:reporthandler:).md)
### Type Methods
- [class func readAttributeAbsMaxPower(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeabsmaxpower(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAbsMinPower(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeabsminpower(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAcceptedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeacceptedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeAttributeList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeattributelist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeClusterRevision(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeclusterrevision(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeESACanGenerate(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeesacangenerate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeESAState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeesastate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeESAType(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeesatype(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeFeatureMap(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributefeaturemap(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeForecast(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRDeviceEnergyManagementClusterForecastStruct?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeforecast(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeGeneratedCommandList(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: ([Any]?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributegeneratedcommandlist(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributeOptOutState(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (NSNumber?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributeoptoutstate(withclusterstatecache:endpoint:queue:completion:).md)
- [class func readAttributePowerAdjustmentCapability(withClusterStateCache: MTRClusterStateCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completion: (MTRDeviceEnergyManagementClusterPowerAdjustCapabilityStruct?, (any Error)?) -> Void)](mtrbaseclusterdeviceenergymanagement/readattributepoweradjustmentcapability(withclusterstatecache:endpoint:queue:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdeviceenergymanagement)*