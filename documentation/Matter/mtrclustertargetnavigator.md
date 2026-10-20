# MTRClusterTargetNavigator

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
class MTRClusterTargetNavigator
```

```objc
@interface MTRClusterTargetNavigator : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclustertargetnavigator/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustertargetnavigator/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func navigateTarget(with: MTRTargetNavigatorClusterNavigateTargetParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRTargetNavigatorClusterNavigateTargetResponseParams?, (any Error)?) -> Void)](./mtrclustertargetnavigator/navigatetarget%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func navigateTarget(with: MTRTargetNavigatorClusterNavigateTargetParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTargetNavigatorClusterNavigateTargetResponseParams?, (any Error)?) -> Void)](./mtrclustertargetnavigator/navigatetarget%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustertargetnavigator/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustertargetnavigator/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustertargetnavigator/readattributeclusterrevision%28with%29.md)
- [func readAttributeCurrentTarget(with: MTRReadParams?) -> [String : Any]?](./mtrclustertargetnavigator/readattributecurrenttarget%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustertargetnavigator/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustertargetnavigator/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeTargetList(with: MTRReadParams?) -> [String : Any]?](./mtrclustertargetnavigator/readattributetargetlist%28with%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustertargetnavigator)*