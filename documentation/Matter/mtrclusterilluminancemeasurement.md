# MTRClusterIlluminanceMeasurement

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
class MTRClusterIlluminanceMeasurement
```

```objc
@interface MTRClusterIlluminanceMeasurement : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterilluminancemeasurement/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterilluminancemeasurement/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterilluminancemeasurement/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterilluminancemeasurement/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterilluminancemeasurement/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterilluminancemeasurement/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterilluminancemeasurement/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeLightSensorType(with: MTRReadParams?) -> [String : Any]?](./mtrclusterilluminancemeasurement/readattributelightsensortype%28with%29.md)
- [func readAttributeMaxMeasuredValue(with: MTRReadParams?) -> [String : Any]?](./mtrclusterilluminancemeasurement/readattributemaxmeasuredvalue%28with%29.md)
- [func readAttributeMeasuredValue(with: MTRReadParams?) -> [String : Any]?](./mtrclusterilluminancemeasurement/readattributemeasuredvalue%28with%29.md)
- [func readAttributeMinMeasuredValue(with: MTRReadParams?) -> [String : Any]?](./mtrclusterilluminancemeasurement/readattributeminmeasuredvalue%28with%29.md)
- [func readAttributeTolerance(with: MTRReadParams?) -> [String : Any]?](./mtrclusterilluminancemeasurement/readattributetolerance%28with%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterilluminancemeasurement)*