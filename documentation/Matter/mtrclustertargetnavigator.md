# MTRClusterTargetNavigator

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
class MTRClusterTargetNavigator
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclustertargetnavigator/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustertargetnavigator/init(device:endpointid:queue:).md)
### Instance Methods
- [func navigateTarget(with: MTRTargetNavigatorClusterNavigateTargetParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRTargetNavigatorClusterNavigateTargetResponseParams?, (any Error)?) -> Void)](mtrclustertargetnavigator/navigatetarget(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func navigateTarget(with: MTRTargetNavigatorClusterNavigateTargetParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRTargetNavigatorClusterNavigateTargetResponseParams?, (any Error)?) -> Void)](mtrclustertargetnavigator/navigatetarget(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustertargetnavigator/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustertargetnavigator/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustertargetnavigator/readattributeclusterrevision(with:).md)
- [func readAttributeCurrentTarget(with: MTRReadParams?) -> [String : Any]?](mtrclustertargetnavigator/readattributecurrenttarget(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustertargetnavigator/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustertargetnavigator/readattributegeneratedcommandlist(with:).md)
- [func readAttributeTargetList(with: MTRReadParams?) -> [String : Any]?](mtrclustertargetnavigator/readattributetargetlist(with:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustertargetnavigator)*