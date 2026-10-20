# MTRClusterGeneralDiagnostics

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterGeneralDiagnostics : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclustergeneraldiagnostics/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustergeneraldiagnostics/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneraldiagnostics/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeActiveHardwareFaults(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneraldiagnostics/readattributeactivehardwarefaults%28with%29.md)
- [func readAttributeActiveNetworkFaults(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneraldiagnostics/readattributeactivenetworkfaults%28with%29.md)
- [func readAttributeActiveRadioFaults(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneraldiagnostics/readattributeactiveradiofaults%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneraldiagnostics/readattributeattributelist%28with%29.md)
- [func readAttributeBootReason(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneraldiagnostics/readattributebootreason%28with%29.md)
- [func readAttributeBootReasons(with: MTRReadParams?) -> [String : Any]](./mtrclustergeneraldiagnostics/readattributebootreasons%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneraldiagnostics/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneraldiagnostics/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneraldiagnostics/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeNetworkInterfaces(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneraldiagnostics/readattributenetworkinterfaces%28with%29.md)
- [func readAttributeRebootCount(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneraldiagnostics/readattributerebootcount%28with%29.md)
- [func readAttributeTestEventTriggersEnabled(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneraldiagnostics/readattributetesteventtriggersenabled%28with%29.md)
- [func readAttributeTotalOperationalHours(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneraldiagnostics/readattributetotaloperationalhours%28with%29.md)
- [func readAttributeUpTime(with: MTRReadParams?) -> [String : Any]?](./mtrclustergeneraldiagnostics/readattributeuptime%28with%29.md)
- [func testEventTrigger(with: MTRGeneralDiagnosticsClusterTestEventTriggerParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustergeneraldiagnostics/testeventtrigger%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func testEventTrigger(with: MTRGeneralDiagnosticsClusterTestEventTriggerParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustergeneraldiagnostics/testeventtrigger%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func payloadTestRequest(with: MTRGeneralDiagnosticsClusterPayloadTestRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGeneralDiagnosticsClusterPayloadTestResponseParams?, (any Error)?) -> Void)](./mtrclustergeneraldiagnostics/payloadtestrequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func timeSnapshot(with: MTRGeneralDiagnosticsClusterTimeSnapshotParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGeneralDiagnosticsClusterTimeSnapshotResponseParams?, (any Error)?) -> Void)](./mtrclustergeneraldiagnostics/timesnapshot%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func timeSnapshot(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGeneralDiagnosticsClusterTimeSnapshotResponseParams?, (any Error)?) -> Void)](./mtrclustergeneraldiagnostics/timesnapshot%28withexpectedvalues,expectedvalueinterval,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustergeneraldiagnostics)*