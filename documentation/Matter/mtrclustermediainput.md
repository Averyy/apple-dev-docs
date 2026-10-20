# MTRClusterMediaInput

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
class MTRClusterMediaInput
```

```objc
@interface MTRClusterMediaInput : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclustermediainput/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustermediainput/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func hideStatus(with: MTRMediaInputClusterHideInputStatusParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustermediainput/hidestatus%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func hideStatus(with: MTRMediaInputClusterHideInputStatusParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustermediainput/hidestatus%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func hideStatus(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustermediainput/hidestatus%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func hideStatus(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustermediainput/hidestatus%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediainput/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediainput/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediainput/readattributeclusterrevision%28with%29.md)
- [func readAttributeCurrentInput(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediainput/readattributecurrentinput%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediainput/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediainput/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeInputList(with: MTRReadParams?) -> [String : Any]?](./mtrclustermediainput/readattributeinputlist%28with%29.md)
- [func renameInput(with: MTRMediaInputClusterRenameInputParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustermediainput/renameinput%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func renameInput(with: MTRMediaInputClusterRenameInputParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustermediainput/renameinput%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func select(with: MTRMediaInputClusterSelectInputParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustermediainput/select%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func select(with: MTRMediaInputClusterSelectInputParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustermediainput/select%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func showStatus(with: MTRMediaInputClusterShowInputStatusParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustermediainput/showstatus%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func showStatus(with: MTRMediaInputClusterShowInputStatusParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustermediainput/showstatus%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func showStatus(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustermediainput/showstatus%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func showStatus(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustermediainput/showstatus%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustermediainput)*