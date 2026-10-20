# MTRClusterEnergyEVSE

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Energy EVSE Electric Vehicle Supply Equipment (EVSE) is equipment used to charge an Electric Vehicle (EV) or Plug-In Hybrid Electric Vehicle. This cluster provides an interface to the functionality of Electric Vehicle Supply Equipment (EVSE) management.

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
class MTRClusterEnergyEVSE
```

```objc
@interface MTRClusterEnergyEVSE : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterenergyevse/init%28device,endpointid,queue%29.md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func clearTargets(with: MTREnergyEVSEClusterClearTargetsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterenergyevse/cleartargets%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func clearTargets(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterenergyevse/cleartargets%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func disable(with: MTREnergyEVSEClusterDisableParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterenergyevse/disable%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func disable(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterenergyevse/disable%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func enableCharging(with: MTREnergyEVSEClusterEnableChargingParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterenergyevse/enablecharging%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func getTargetsWith(MTREnergyEVSEClusterGetTargetsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTREnergyEVSEClusterGetTargetsResponseParams?, (any Error)?) -> Void)](./mtrclusterenergyevse/gettargetswith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func getTargetsWithExpectedValues([[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTREnergyEVSEClusterGetTargetsResponseParams?, (any Error)?) -> Void)](./mtrclusterenergyevse/gettargetswithexpectedvalues%28_,expectedvalueinterval,completion%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeApproximateEVEfficiency(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributeapproximateevefficiency%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributeattributelist%28with%29.md)
- [func readAttributeChargingEnabledUntil(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributechargingenableduntil%28with%29.md)
- [func readAttributeCircuitCapacity(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributecircuitcapacity%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributeclusterrevision%28with%29.md)
- [func readAttributeFaultState(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributefaultstate%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeMaximumChargeCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributemaximumchargecurrent%28with%29.md)
- [func readAttributeMinimumChargeCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributeminimumchargecurrent%28with%29.md)
- [func readAttributeNextChargeRequiredEnergy(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributenextchargerequiredenergy%28with%29.md)
- [func readAttributeNextChargeStartTime(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributenextchargestarttime%28with%29.md)
- [func readAttributeNextChargeTargetSoC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributenextchargetargetsoc%28with%29.md)
- [func readAttributeNextChargeTargetTime(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributenextchargetargettime%28with%29.md)
- [func readAttributeRandomizationDelayWindow(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributerandomizationdelaywindow%28with%29.md)
- [func readAttributeSessionDuration(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributesessionduration%28with%29.md)
- [func readAttributeSessionEnergyCharged(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributesessionenergycharged%28with%29.md)
- [func readAttributeSessionID(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributesessionid%28with%29.md)
- [func readAttributeState(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributestate%28with%29.md)
- [func readAttributeSupplyState(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributesupplystate%28with%29.md)
- [func readAttributeUserMaximumChargeCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterenergyevse/readattributeusermaximumchargecurrent%28with%29.md)
- [func setTargetsWith(MTREnergyEVSEClusterSetTargetsParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterenergyevse/settargetswith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func startDiagnostics(with: MTREnergyEVSEClusterStartDiagnosticsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterenergyevse/startdiagnostics%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func startDiagnostics(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterenergyevse/startdiagnostics%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func writeAttributeApproximateEVEfficiency(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterenergyevse/writeattributeapproximateevefficiency%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeApproximateEVEfficiency(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterenergyevse/writeattributeapproximateevefficiency%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeRandomizationDelayWindow(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterenergyevse/writeattributerandomizationdelaywindow%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeRandomizationDelayWindow(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterenergyevse/writeattributerandomizationdelaywindow%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeUserMaximumChargeCurrent(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterenergyevse/writeattributeusermaximumchargecurrent%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeUserMaximumChargeCurrent(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterenergyevse/writeattributeusermaximumchargecurrent%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterenergyevse)*