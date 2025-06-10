# MTRClusterGeneralDiagnostics

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRClusterGeneralDiagnostics
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclustergeneraldiagnostics/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustergeneraldiagnostics/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneraldiagnostics/readattributeacceptedcommandlist(with:).md)
- [func readAttributeActiveHardwareFaults(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneraldiagnostics/readattributeactivehardwarefaults(with:).md)
- [func readAttributeActiveNetworkFaults(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneraldiagnostics/readattributeactivenetworkfaults(with:).md)
- [func readAttributeActiveRadioFaults(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneraldiagnostics/readattributeactiveradiofaults(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneraldiagnostics/readattributeattributelist(with:).md)
- [func readAttributeBootReason(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneraldiagnostics/readattributebootreason(with:).md)
- [func readAttributeBootReasons(with: MTRReadParams?) -> [String : Any]](mtrclustergeneraldiagnostics/readattributebootreasons(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneraldiagnostics/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneraldiagnostics/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneraldiagnostics/readattributegeneratedcommandlist(with:).md)
- [func readAttributeNetworkInterfaces(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneraldiagnostics/readattributenetworkinterfaces(with:).md)
- [func readAttributeRebootCount(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneraldiagnostics/readattributerebootcount(with:).md)
- [func readAttributeTestEventTriggersEnabled(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneraldiagnostics/readattributetesteventtriggersenabled(with:).md)
- [func readAttributeTotalOperationalHours(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneraldiagnostics/readattributetotaloperationalhours(with:).md)
- [func readAttributeUpTime(with: MTRReadParams?) -> [String : Any]?](mtrclustergeneraldiagnostics/readattributeuptime(with:).md)
- [func testEventTrigger(with: MTRGeneralDiagnosticsClusterTestEventTriggerParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclustergeneraldiagnostics/testeventtrigger(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func testEventTrigger(with: MTRGeneralDiagnosticsClusterTestEventTriggerParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclustergeneraldiagnostics/testeventtrigger(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func payloadTestRequest(with: MTRGeneralDiagnosticsClusterPayloadTestRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGeneralDiagnosticsClusterPayloadTestResponseParams?, (any Error)?) -> Void)](mtrclustergeneraldiagnostics/payloadtestrequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func timeSnapshot(with: MTRGeneralDiagnosticsClusterTimeSnapshotParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGeneralDiagnosticsClusterTimeSnapshotResponseParams?, (any Error)?) -> Void)](mtrclustergeneraldiagnostics/timesnapshot(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func timeSnapshot(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGeneralDiagnosticsClusterTimeSnapshotResponseParams?, (any Error)?) -> Void)](mtrclustergeneraldiagnostics/timesnapshot(withexpectedvalues:expectedvalueinterval:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustergeneraldiagnostics)*