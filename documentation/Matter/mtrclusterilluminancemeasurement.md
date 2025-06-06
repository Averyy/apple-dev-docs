# MTRClusterIlluminanceMeasurement

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
class MTRClusterIlluminanceMeasurement
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterilluminancemeasurement/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterilluminancemeasurement/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterilluminancemeasurement/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterilluminancemeasurement/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterilluminancemeasurement/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterilluminancemeasurement/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterilluminancemeasurement/readattributegeneratedcommandlist(with:).md)
- [func readAttributeLightSensorType(with: MTRReadParams?) -> [String : Any]?](mtrclusterilluminancemeasurement/readattributelightsensortype(with:).md)
- [func readAttributeMaxMeasuredValue(with: MTRReadParams?) -> [String : Any]?](mtrclusterilluminancemeasurement/readattributemaxmeasuredvalue(with:).md)
- [func readAttributeMeasuredValue(with: MTRReadParams?) -> [String : Any]?](mtrclusterilluminancemeasurement/readattributemeasuredvalue(with:).md)
- [func readAttributeMinMeasuredValue(with: MTRReadParams?) -> [String : Any]?](mtrclusterilluminancemeasurement/readattributeminmeasuredvalue(with:).md)
- [func readAttributeTolerance(with: MTRReadParams?) -> [String : Any]?](mtrclusterilluminancemeasurement/readattributetolerance(with:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterilluminancemeasurement)*