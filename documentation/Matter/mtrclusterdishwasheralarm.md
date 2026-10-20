# MTRClusterDishwasherAlarm

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterDishwasherAlarm : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterdishwasheralarm/init%28device,endpointid,queue%29.md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func modifyEnabledAlarms(with: MTRDishwasherAlarmClusterModifyEnabledAlarmsParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdishwasheralarm/modifyenabledalarms%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdishwasheralarm/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdishwasheralarm/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdishwasheralarm/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdishwasheralarm/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdishwasheralarm/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeLatch(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdishwasheralarm/readattributelatch%28with%29.md)
- [func readAttributeMask(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdishwasheralarm/readattributemask%28with%29.md)
- [func readAttributeState(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdishwasheralarm/readattributestate%28with%29.md)
- [func readAttributeSupported(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdishwasheralarm/readattributesupported%28with%29.md)
- [func reset(with: MTRDishwasherAlarmClusterResetParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdishwasheralarm/reset%28with,expectedvalues,expectedvalueinterval,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdishwasheralarm)*