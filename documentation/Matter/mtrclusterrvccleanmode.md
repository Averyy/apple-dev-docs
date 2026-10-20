# MTRClusterRVCCleanMode

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
class MTRClusterRVCCleanMode
```

```objc
@interface MTRClusterRVCCleanMode : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterrvccleanmode/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func changeToMode(with: MTRRVCCleanModeClusterChangeToModeParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRRVCCleanModeClusterChangeToModeResponseParams?, (any Error)?) -> Void)](./mtrclusterrvccleanmode/changetomode%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvccleanmode/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvccleanmode/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvccleanmode/readattributeclusterrevision%28with%29.md)
- [func readAttributeCurrentMode(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvccleanmode/readattributecurrentmode%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvccleanmode/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvccleanmode/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeSupportedModes(with: MTRReadParams?) -> [String : Any]?](./mtrclusterrvccleanmode/readattributesupportedmodes%28with%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterrvccleanmode)*