# MTRClusterServiceArea

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Service Area The Service Area cluster provides an interface for controlling the areas where a device should operate, and for querying the current area being serviced.

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
class MTRClusterServiceArea
```

```objc
@interface MTRClusterServiceArea : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterservicearea/init%28device,endpointid,queue%29.md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterservicearea/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterservicearea/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterservicearea/readattributeclusterrevision%28with%29.md)
- [func readAttributeCurrentArea(with: MTRReadParams?) -> [String : Any]?](./mtrclusterservicearea/readattributecurrentarea%28with%29.md)
- [func readAttributeEstimatedEndTime(with: MTRReadParams?) -> [String : Any]?](./mtrclusterservicearea/readattributeestimatedendtime%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterservicearea/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterservicearea/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeProgress(with: MTRReadParams?) -> [String : Any]?](./mtrclusterservicearea/readattributeprogress%28with%29.md)
- [func readAttributeSelectedAreas(with: MTRReadParams?) -> [String : Any]?](./mtrclusterservicearea/readattributeselectedareas%28with%29.md)
- [func readAttributeSupportedAreas(with: MTRReadParams?) -> [String : Any]?](./mtrclusterservicearea/readattributesupportedareas%28with%29.md)
- [func readAttributeSupportedMaps(with: MTRReadParams?) -> [String : Any]?](./mtrclusterservicearea/readattributesupportedmaps%28with%29.md)
- [func selectAreas(with: MTRServiceAreaClusterSelectAreasParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRServiceAreaClusterSelectAreasResponseParams?, (any Error)?) -> Void)](./mtrclusterservicearea/selectareas%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func skip(with: MTRServiceAreaClusterSkipAreaParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRServiceAreaClusterSkipAreaResponseParams?, (any Error)?) -> Void)](./mtrclusterservicearea/skip%28with,expectedvalues,expectedvalueinterval,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterservicearea)*