# MTRClusterDishwasherAlarm

**Framework**: Matter  
**Kind**: class

Cluster Dishwasher Alarm Attributes and commands for configuring the Dishwasher alarm.

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
class MTRClusterDishwasherAlarm
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterdishwasheralarm/init(device:endpointid:queue:).md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func modifyEnabledAlarms(with: MTRDishwasherAlarmClusterModifyEnabledAlarmsParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdishwasheralarm/modifyenabledalarms(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdishwasheralarm/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdishwasheralarm/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterdishwasheralarm/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterdishwasheralarm/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdishwasheralarm/readattributegeneratedcommandlist(with:).md)
- [func readAttributeLatch(with: MTRReadParams?) -> [String : Any]?](mtrclusterdishwasheralarm/readattributelatch(with:).md)
- [func readAttributeMask(with: MTRReadParams?) -> [String : Any]?](mtrclusterdishwasheralarm/readattributemask(with:).md)
- [func readAttributeState(with: MTRReadParams?) -> [String : Any]?](mtrclusterdishwasheralarm/readattributestate(with:).md)
- [func readAttributeSupported(with: MTRReadParams?) -> [String : Any]?](mtrclusterdishwasheralarm/readattributesupported(with:).md)
- [func reset(with: MTRDishwasherAlarmClusterResetParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdishwasheralarm/reset(with:expectedvalues:expectedvalueinterval:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdishwasheralarm)*