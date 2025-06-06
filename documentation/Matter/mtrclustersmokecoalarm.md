# MTRClusterSmokeCOAlarm

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
class MTRClusterSmokeCOAlarm
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustersmokecoalarm/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributeattributelist(with:).md)
- [func readAttributeBatteryAlert(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributebatteryalert(with:).md)
- [func readAttributeCOState(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributecostate(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributeclusterrevision(with:).md)
- [func readAttributeContaminationState(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributecontaminationstate(with:).md)
- [func readAttributeDeviceMuted(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributedevicemuted(with:).md)
- [func readAttributeEndOfServiceAlert(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributeendofservicealert(with:).md)
- [func readAttributeExpiryDate(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributeexpirydate(with:).md)
- [func readAttributeExpressedState(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributeexpressedstate(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributegeneratedcommandlist(with:).md)
- [func readAttributeHardwareFaultAlert(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributehardwarefaultalert(with:).md)
- [func readAttributeInterconnectCOAlarm(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributeinterconnectcoalarm(with:).md)
- [func readAttributeInterconnectSmoke(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributeinterconnectsmoke(with:).md)
- [func readAttributeSmokeSensitivityLevel(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributesmokesensitivitylevel(with:).md)
- [func readAttributeSmokeState(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributesmokestate(with:).md)
- [func readAttributeTestInProgress(with: MTRReadParams?) -> [String : Any]?](mtrclustersmokecoalarm/readattributetestinprogress(with:).md)
- [func selfTestRequest(with: MTRSmokeCOAlarmClusterSelfTestRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustersmokecoalarm/selftestrequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func selfTestRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustersmokecoalarm/selftestrequest(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func writeAttributeSmokeSensitivityLevel(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustersmokecoalarm/writeattributesmokesensitivitylevel(withvalue:expectedvalueinterval:).md)
- [func writeAttributeSmokeSensitivityLevel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustersmokecoalarm/writeattributesmokesensitivitylevel(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustersmokecoalarm)*