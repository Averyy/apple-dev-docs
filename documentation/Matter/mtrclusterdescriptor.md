# MTRClusterDescriptor

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
class MTRClusterDescriptor
```

```objc
@interface MTRClusterDescriptor : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterdescriptor/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterdescriptor/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdescriptor/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdescriptor/readattributeattributelist%28with%29.md)
- [func readAttributeClientList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdescriptor/readattributeclientlist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdescriptor/readattributeclusterrevision%28with%29.md)
- [func readAttributeDeviceList(with: MTRReadParams?) -> [String : Any]](./mtrclusterdescriptor/readattributedevicelist%28with%29.md)
- [func readAttributeDeviceTypeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdescriptor/readattributedevicetypelist%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdescriptor/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdescriptor/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributePartsList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdescriptor/readattributepartslist%28with%29.md)
- [func readAttributeServerList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdescriptor/readattributeserverlist%28with%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdescriptor)*