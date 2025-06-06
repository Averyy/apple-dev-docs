# MTRClusterPressureMeasurement

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
class MTRClusterPressureMeasurement
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterpressuremeasurement/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterpressuremeasurement/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterpressuremeasurement/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterpressuremeasurement/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterpressuremeasurement/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterpressuremeasurement/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterpressuremeasurement/readattributegeneratedcommandlist(with:).md)
- [func readAttributeMaxMeasuredValue(with: MTRReadParams?) -> [String : Any]?](mtrclusterpressuremeasurement/readattributemaxmeasuredvalue(with:).md)
- [func readAttributeMaxScaledValue(with: MTRReadParams?) -> [String : Any]?](mtrclusterpressuremeasurement/readattributemaxscaledvalue(with:).md)
- [func readAttributeMeasuredValue(with: MTRReadParams?) -> [String : Any]?](mtrclusterpressuremeasurement/readattributemeasuredvalue(with:).md)
- [func readAttributeMinMeasuredValue(with: MTRReadParams?) -> [String : Any]?](mtrclusterpressuremeasurement/readattributeminmeasuredvalue(with:).md)
- [func readAttributeMinScaledValue(with: MTRReadParams?) -> [String : Any]?](mtrclusterpressuremeasurement/readattributeminscaledvalue(with:).md)
- [func readAttributeScale(with: MTRReadParams?) -> [String : Any]?](mtrclusterpressuremeasurement/readattributescale(with:).md)
- [func readAttributeScaledTolerance(with: MTRReadParams?) -> [String : Any]?](mtrclusterpressuremeasurement/readattributescaledtolerance(with:).md)
- [func readAttributeScaledValue(with: MTRReadParams?) -> [String : Any]?](mtrclusterpressuremeasurement/readattributescaledvalue(with:).md)
- [func readAttributeTolerance(with: MTRReadParams?) -> [String : Any]?](mtrclusterpressuremeasurement/readattributetolerance(with:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterpressuremeasurement)*