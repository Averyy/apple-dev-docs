# MTRClusterDescriptor

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
class MTRClusterDescriptor
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterdescriptor/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterdescriptor/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdescriptor/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdescriptor/readattributeattributelist(with:).md)
- [func readAttributeClientList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdescriptor/readattributeclientlist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterdescriptor/readattributeclusterrevision(with:).md)
- [func readAttributeDeviceList(with: MTRReadParams?) -> [String : Any]](mtrclusterdescriptor/readattributedevicelist(with:).md)
- [func readAttributeDeviceTypeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdescriptor/readattributedevicetypelist(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterdescriptor/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdescriptor/readattributegeneratedcommandlist(with:).md)
- [func readAttributePartsList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdescriptor/readattributepartslist(with:).md)
- [func readAttributeServerList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdescriptor/readattributeserverlist(with:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdescriptor)*