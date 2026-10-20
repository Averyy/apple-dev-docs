# MTRClusterPressureMeasurement

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
class MTRClusterPressureMeasurement
```

```objc
@interface MTRClusterPressureMeasurement : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterpressuremeasurement/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterpressuremeasurement/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpressuremeasurement/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpressuremeasurement/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpressuremeasurement/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpressuremeasurement/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpressuremeasurement/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeMaxMeasuredValue(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpressuremeasurement/readattributemaxmeasuredvalue%28with%29.md)
- [func readAttributeMaxScaledValue(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpressuremeasurement/readattributemaxscaledvalue%28with%29.md)
- [func readAttributeMeasuredValue(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpressuremeasurement/readattributemeasuredvalue%28with%29.md)
- [func readAttributeMinMeasuredValue(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpressuremeasurement/readattributeminmeasuredvalue%28with%29.md)
- [func readAttributeMinScaledValue(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpressuremeasurement/readattributeminscaledvalue%28with%29.md)
- [func readAttributeScale(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpressuremeasurement/readattributescale%28with%29.md)
- [func readAttributeScaledTolerance(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpressuremeasurement/readattributescaledtolerance%28with%29.md)
- [func readAttributeScaledValue(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpressuremeasurement/readattributescaledvalue%28with%29.md)
- [func readAttributeTolerance(with: MTRReadParams?) -> [String : Any]?](./mtrclusterpressuremeasurement/readattributetolerance%28with%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterpressuremeasurement)*