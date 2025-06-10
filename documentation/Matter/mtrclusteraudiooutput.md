# MTRClusterAudioOutput

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
class MTRClusterAudioOutput
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusteraudiooutput/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusteraudiooutput/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteraudiooutput/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusteraudiooutput/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusteraudiooutput/readattributeclusterrevision(with:).md)
- [func readAttributeCurrentOutput(with: MTRReadParams?) -> [String : Any]?](mtrclusteraudiooutput/readattributecurrentoutput(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusteraudiooutput/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteraudiooutput/readattributegeneratedcommandlist(with:).md)
- [func readAttributeOutputList(with: MTRReadParams?) -> [String : Any]?](mtrclusteraudiooutput/readattributeoutputlist(with:).md)
- [func renameOutput(with: MTRAudioOutputClusterRenameOutputParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteraudiooutput/renameoutput(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func renameOutput(with: MTRAudioOutputClusterRenameOutputParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteraudiooutput/renameoutput(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func select(with: MTRAudioOutputClusterSelectOutputParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteraudiooutput/select(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func select(with: MTRAudioOutputClusterSelectOutputParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteraudiooutput/select(with:expectedvalues:expectedvalueinterval:completionhandler:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteraudiooutput)*