# MTRClusterDeviceEnergyManagement

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterDeviceEnergyManagement : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterdeviceenergymanagement/init%28device,endpointid,queue%29.md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func cancelPowerAdjustRequest(with: MTRDeviceEnergyManagementClusterCancelPowerAdjustRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdeviceenergymanagement/cancelpoweradjustrequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func cancelPowerAdjustRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdeviceenergymanagement/cancelpoweradjustrequest%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func cancelRequest(with: MTRDeviceEnergyManagementClusterCancelRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdeviceenergymanagement/cancelrequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func cancelRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdeviceenergymanagement/cancelrequest%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func modifyForecastRequest(with: MTRDeviceEnergyManagementClusterModifyForecastRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdeviceenergymanagement/modifyforecastrequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func pauseRequest(with: MTRDeviceEnergyManagementClusterPauseRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdeviceenergymanagement/pauserequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func powerAdjustRequest(with: MTRDeviceEnergyManagementClusterPowerAdjustRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdeviceenergymanagement/poweradjustrequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAbsMaxPower(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdeviceenergymanagement/readattributeabsmaxpower%28with%29.md)
- [func readAttributeAbsMinPower(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdeviceenergymanagement/readattributeabsminpower%28with%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdeviceenergymanagement/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdeviceenergymanagement/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdeviceenergymanagement/readattributeclusterrevision%28with%29.md)
- [func readAttributeESACanGenerate(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdeviceenergymanagement/readattributeesacangenerate%28with%29.md)
- [func readAttributeESAState(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdeviceenergymanagement/readattributeesastate%28with%29.md)
- [func readAttributeESAType(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdeviceenergymanagement/readattributeesatype%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdeviceenergymanagement/readattributefeaturemap%28with%29.md)
- [func readAttributeForecast(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdeviceenergymanagement/readattributeforecast%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdeviceenergymanagement/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeOptOutState(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdeviceenergymanagement/readattributeoptoutstate%28with%29.md)
- [func readAttributePowerAdjustmentCapability(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdeviceenergymanagement/readattributepoweradjustmentcapability%28with%29.md)
- [func requestConstraintBasedForecast(with: MTRDeviceEnergyManagementClusterRequestConstraintBasedForecastParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdeviceenergymanagement/requestconstraintbasedforecast%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func resumeRequest(with: MTRDeviceEnergyManagementClusterResumeRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdeviceenergymanagement/resumerequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func resumeRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdeviceenergymanagement/resumerequest%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func startTimeAdjustRequest(with: MTRDeviceEnergyManagementClusterStartTimeAdjustRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdeviceenergymanagement/starttimeadjustrequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)

## Relationships

### Inherits From
- [MTRGenericCluster](./mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdeviceenergymanagement)*