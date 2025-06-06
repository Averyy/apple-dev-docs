# MTRClusterDeviceEnergyManagement

**Framework**: Matter  
**Kind**: class

Cluster Device Energy Management This cluster allows a client to manage the power draw of a device. An example of such a client could be an Energy Management System (EMS) which controls an Energy Smart Appliance (ESA).

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
class MTRClusterDeviceEnergyManagement
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterdeviceenergymanagement/init(device:endpointid:queue:).md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func cancelPowerAdjustRequest(with: MTRDeviceEnergyManagementClusterCancelPowerAdjustRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterdeviceenergymanagement/cancelpoweradjustrequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func cancelPowerAdjustRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterdeviceenergymanagement/cancelpoweradjustrequest(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func cancelRequest(with: MTRDeviceEnergyManagementClusterCancelRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterdeviceenergymanagement/cancelrequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func cancelRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterdeviceenergymanagement/cancelrequest(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func modifyForecastRequest(with: MTRDeviceEnergyManagementClusterModifyForecastRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterdeviceenergymanagement/modifyforecastrequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func pauseRequest(with: MTRDeviceEnergyManagementClusterPauseRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterdeviceenergymanagement/pauserequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func powerAdjustRequest(with: MTRDeviceEnergyManagementClusterPowerAdjustRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterdeviceenergymanagement/poweradjustrequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAbsMaxPower(with: MTRReadParams?) -> [String : Any]?](mtrclusterdeviceenergymanagement/readattributeabsmaxpower(with:).md)
- [func readAttributeAbsMinPower(with: MTRReadParams?) -> [String : Any]?](mtrclusterdeviceenergymanagement/readattributeabsminpower(with:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdeviceenergymanagement/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdeviceenergymanagement/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterdeviceenergymanagement/readattributeclusterrevision(with:).md)
- [func readAttributeESACanGenerate(with: MTRReadParams?) -> [String : Any]?](mtrclusterdeviceenergymanagement/readattributeesacangenerate(with:).md)
- [func readAttributeESAState(with: MTRReadParams?) -> [String : Any]?](mtrclusterdeviceenergymanagement/readattributeesastate(with:).md)
- [func readAttributeESAType(with: MTRReadParams?) -> [String : Any]?](mtrclusterdeviceenergymanagement/readattributeesatype(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterdeviceenergymanagement/readattributefeaturemap(with:).md)
- [func readAttributeForecast(with: MTRReadParams?) -> [String : Any]?](mtrclusterdeviceenergymanagement/readattributeforecast(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdeviceenergymanagement/readattributegeneratedcommandlist(with:).md)
- [func readAttributeOptOutState(with: MTRReadParams?) -> [String : Any]?](mtrclusterdeviceenergymanagement/readattributeoptoutstate(with:).md)
- [func readAttributePowerAdjustmentCapability(with: MTRReadParams?) -> [String : Any]?](mtrclusterdeviceenergymanagement/readattributepoweradjustmentcapability(with:).md)
- [func requestConstraintBasedForecast(with: MTRDeviceEnergyManagementClusterRequestConstraintBasedForecastParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterdeviceenergymanagement/requestconstraintbasedforecast(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func resumeRequest(with: MTRDeviceEnergyManagementClusterResumeRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterdeviceenergymanagement/resumerequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func resumeRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterdeviceenergymanagement/resumerequest(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func startTimeAdjustRequest(with: MTRDeviceEnergyManagementClusterStartTimeAdjustRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterdeviceenergymanagement/starttimeadjustrequest(with:expectedvalues:expectedvalueinterval:completion:).md)

## Relationships

### Inherits From
- [MTRGenericCluster](mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdeviceenergymanagement)*