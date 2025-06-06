# MTRClusterFlowMeasurement

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
class MTRClusterFlowMeasurement
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterflowmeasurement/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterflowmeasurement/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterflowmeasurement/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterflowmeasurement/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterflowmeasurement/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterflowmeasurement/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterflowmeasurement/readattributegeneratedcommandlist(with:).md)
- [func readAttributeMaxMeasuredValue(with: MTRReadParams?) -> [String : Any]?](mtrclusterflowmeasurement/readattributemaxmeasuredvalue(with:).md)
- [func readAttributeMeasuredValue(with: MTRReadParams?) -> [String : Any]?](mtrclusterflowmeasurement/readattributemeasuredvalue(with:).md)
- [func readAttributeMinMeasuredValue(with: MTRReadParams?) -> [String : Any]?](mtrclusterflowmeasurement/readattributeminmeasuredvalue(with:).md)
- [func readAttributeTolerance(with: MTRReadParams?) -> [String : Any]?](mtrclusterflowmeasurement/readattributetolerance(with:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterflowmeasurement)*