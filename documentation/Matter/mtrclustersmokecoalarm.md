# MTRClusterSmokeCOAlarm

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterSmokeCOAlarm : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustersmokecoalarm/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributeattributelist%28with%29.md)
- [func readAttributeBatteryAlert(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributebatteryalert%28with%29.md)
- [func readAttributeCOState(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributecostate%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributeclusterrevision%28with%29.md)
- [func readAttributeContaminationState(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributecontaminationstate%28with%29.md)
- [func readAttributeDeviceMuted(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributedevicemuted%28with%29.md)
- [func readAttributeEndOfServiceAlert(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributeendofservicealert%28with%29.md)
- [func readAttributeExpiryDate(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributeexpirydate%28with%29.md)
- [func readAttributeExpressedState(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributeexpressedstate%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeHardwareFaultAlert(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributehardwarefaultalert%28with%29.md)
- [func readAttributeInterconnectCOAlarm(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributeinterconnectcoalarm%28with%29.md)
- [func readAttributeInterconnectSmoke(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributeinterconnectsmoke%28with%29.md)
- [func readAttributeSmokeSensitivityLevel(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributesmokesensitivitylevel%28with%29.md)
- [func readAttributeSmokeState(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributesmokestate%28with%29.md)
- [func readAttributeTestInProgress(with: MTRReadParams?) -> [String : Any]?](./mtrclustersmokecoalarm/readattributetestinprogress%28with%29.md)
- [func selfTestRequest(with: MTRSmokeCOAlarmClusterSelfTestRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustersmokecoalarm/selftestrequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func selfTestRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustersmokecoalarm/selftestrequest%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func writeAttributeSmokeSensitivityLevel(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustersmokecoalarm/writeattributesmokesensitivitylevel%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeSmokeSensitivityLevel(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustersmokecoalarm/writeattributesmokesensitivitylevel%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustersmokecoalarm)*