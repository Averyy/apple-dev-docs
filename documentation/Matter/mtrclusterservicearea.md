# MTRClusterServiceArea

**Framework**: Matter  
**Kind**: class

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

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterservicearea/init(device:endpointid:queue:).md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterservicearea/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterservicearea/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterservicearea/readattributeclusterrevision(with:).md)
- [func readAttributeCurrentArea(with: MTRReadParams?) -> [String : Any]?](mtrclusterservicearea/readattributecurrentarea(with:).md)
- [func readAttributeEstimatedEndTime(with: MTRReadParams?) -> [String : Any]?](mtrclusterservicearea/readattributeestimatedendtime(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterservicearea/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterservicearea/readattributegeneratedcommandlist(with:).md)
- [func readAttributeProgress(with: MTRReadParams?) -> [String : Any]?](mtrclusterservicearea/readattributeprogress(with:).md)
- [func readAttributeSelectedAreas(with: MTRReadParams?) -> [String : Any]?](mtrclusterservicearea/readattributeselectedareas(with:).md)
- [func readAttributeSupportedAreas(with: MTRReadParams?) -> [String : Any]?](mtrclusterservicearea/readattributesupportedareas(with:).md)
- [func readAttributeSupportedMaps(with: MTRReadParams?) -> [String : Any]?](mtrclusterservicearea/readattributesupportedmaps(with:).md)
- [func selectAreas(with: MTRServiceAreaClusterSelectAreasParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRServiceAreaClusterSelectAreasResponseParams?, (any Error)?) -> Void)](mtrclusterservicearea/selectareas(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func skip(with: MTRServiceAreaClusterSkipAreaParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRServiceAreaClusterSkipAreaResponseParams?, (any Error)?) -> Void)](mtrclusterservicearea/skip(with:expectedvalues:expectedvalueinterval:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterservicearea)*