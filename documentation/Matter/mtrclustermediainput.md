# MTRClusterMediaInput

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
class MTRClusterMediaInput
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclustermediainput/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustermediainput/init(device:endpointid:queue:).md)
### Instance Methods
- [func hideStatus(with: MTRMediaInputClusterHideInputStatusParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustermediainput/hidestatus(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func hideStatus(with: MTRMediaInputClusterHideInputStatusParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustermediainput/hidestatus(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func hideStatus(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustermediainput/hidestatus(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func hideStatus(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustermediainput/hidestatus(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustermediainput/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustermediainput/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustermediainput/readattributeclusterrevision(with:).md)
- [func readAttributeCurrentInput(with: MTRReadParams?) -> [String : Any]?](mtrclustermediainput/readattributecurrentinput(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustermediainput/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustermediainput/readattributegeneratedcommandlist(with:).md)
- [func readAttributeInputList(with: MTRReadParams?) -> [String : Any]?](mtrclustermediainput/readattributeinputlist(with:).md)
- [func renameInput(with: MTRMediaInputClusterRenameInputParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustermediainput/renameinput(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func renameInput(with: MTRMediaInputClusterRenameInputParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustermediainput/renameinput(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func select(with: MTRMediaInputClusterSelectInputParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustermediainput/select(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func select(with: MTRMediaInputClusterSelectInputParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustermediainput/select(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func showStatus(with: MTRMediaInputClusterShowInputStatusParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustermediainput/showstatus(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func showStatus(with: MTRMediaInputClusterShowInputStatusParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustermediainput/showstatus(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func showStatus(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustermediainput/showstatus(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func showStatus(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustermediainput/showstatus(withexpectedvalues:expectedvalueinterval:completionhandler:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustermediainput)*