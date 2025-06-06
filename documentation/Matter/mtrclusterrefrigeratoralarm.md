# MTRClusterRefrigeratorAlarm

**Framework**: Matter  
**Kind**: class

Cluster Refrigerator Alarm Attributes and commands for configuring the Refrigerator alarm.

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
class MTRClusterRefrigeratorAlarm
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterrefrigeratoralarm/init(device:endpointid:queue:).md)
  The queue is currently unused, but may be used in the future for calling completions for command invocations if commands are added to this cluster.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterrefrigeratoralarm/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterrefrigeratoralarm/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterrefrigeratoralarm/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterrefrigeratoralarm/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterrefrigeratoralarm/readattributegeneratedcommandlist(with:).md)
- [func readAttributeMask(with: MTRReadParams?) -> [String : Any]?](mtrclusterrefrigeratoralarm/readattributemask(with:).md)
- [func readAttributeState(with: MTRReadParams?) -> [String : Any]?](mtrclusterrefrigeratoralarm/readattributestate(with:).md)
- [func readAttributeSupported(with: MTRReadParams?) -> [String : Any]?](mtrclusterrefrigeratoralarm/readattributesupported(with:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterrefrigeratoralarm)*