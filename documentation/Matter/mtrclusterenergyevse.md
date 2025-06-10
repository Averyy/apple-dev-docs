# MTRClusterEnergyEVSE

**Framework**: Matter  
**Kind**: class

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

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterenergyevse/init(device:endpointid:queue:).md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func clearTargets(with: MTREnergyEVSEClusterClearTargetsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterenergyevse/cleartargets(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func clearTargets(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterenergyevse/cleartargets(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func disable(with: MTREnergyEVSEClusterDisableParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterenergyevse/disable(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func disable(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterenergyevse/disable(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func enableCharging(with: MTREnergyEVSEClusterEnableChargingParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterenergyevse/enablecharging(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func getTargetsWith(MTREnergyEVSEClusterGetTargetsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTREnergyEVSEClusterGetTargetsResponseParams?, (any Error)?) -> Void)](mtrclusterenergyevse/gettargetswith(_:expectedvalues:expectedvalueinterval:completion:).md)
- [func getTargetsWithExpectedValues([[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTREnergyEVSEClusterGetTargetsResponseParams?, (any Error)?) -> Void)](mtrclusterenergyevse/gettargetswithexpectedvalues(_:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributeacceptedcommandlist(with:).md)
- [func readAttributeApproximateEVEfficiency(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributeapproximateevefficiency(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributeattributelist(with:).md)
- [func readAttributeChargingEnabledUntil(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributechargingenableduntil(with:).md)
- [func readAttributeCircuitCapacity(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributecircuitcapacity(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributeclusterrevision(with:).md)
- [func readAttributeFaultState(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributefaultstate(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributegeneratedcommandlist(with:).md)
- [func readAttributeMaximumChargeCurrent(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributemaximumchargecurrent(with:).md)
- [func readAttributeMinimumChargeCurrent(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributeminimumchargecurrent(with:).md)
- [func readAttributeNextChargeRequiredEnergy(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributenextchargerequiredenergy(with:).md)
- [func readAttributeNextChargeStartTime(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributenextchargestarttime(with:).md)
- [func readAttributeNextChargeTargetSoC(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributenextchargetargetsoc(with:).md)
- [func readAttributeNextChargeTargetTime(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributenextchargetargettime(with:).md)
- [func readAttributeRandomizationDelayWindow(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributerandomizationdelaywindow(with:).md)
- [func readAttributeSessionDuration(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributesessionduration(with:).md)
- [func readAttributeSessionEnergyCharged(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributesessionenergycharged(with:).md)
- [func readAttributeSessionID(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributesessionid(with:).md)
- [func readAttributeState(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributestate(with:).md)
- [func readAttributeSupplyState(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributesupplystate(with:).md)
- [func readAttributeUserMaximumChargeCurrent(with: MTRReadParams?) -> [String : Any]?](mtrclusterenergyevse/readattributeusermaximumchargecurrent(with:).md)
- [func setTargetsWith(MTREnergyEVSEClusterSetTargetsParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterenergyevse/settargetswith(_:expectedvalues:expectedvalueinterval:completion:).md)
- [func startDiagnostics(with: MTREnergyEVSEClusterStartDiagnosticsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterenergyevse/startdiagnostics(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func startDiagnostics(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterenergyevse/startdiagnostics(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func writeAttributeApproximateEVEfficiency(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterenergyevse/writeattributeapproximateevefficiency(withvalue:expectedvalueinterval:).md)
- [func writeAttributeApproximateEVEfficiency(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterenergyevse/writeattributeapproximateevefficiency(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeRandomizationDelayWindow(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterenergyevse/writeattributerandomizationdelaywindow(withvalue:expectedvalueinterval:).md)
- [func writeAttributeRandomizationDelayWindow(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterenergyevse/writeattributerandomizationdelaywindow(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeUserMaximumChargeCurrent(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterenergyevse/writeattributeusermaximumchargecurrent(withvalue:expectedvalueinterval:).md)
- [func writeAttributeUserMaximumChargeCurrent(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterenergyevse/writeattributeusermaximumchargecurrent(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterenergyevse)*