# MTRClusterModeSelect

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
class MTRClusterModeSelect
```

```objc
@interface MTRClusterModeSelect : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclustermodeselect/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustermodeselect/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func changeToMode(with: MTRModeSelectClusterChangeToModeParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustermodeselect/changetomode%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func changeToMode(with: MTRModeSelectClusterChangeToModeParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustermodeselect/changetomode%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustermodeselect/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustermodeselect/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustermodeselect/readattributeclusterrevision%28with%29.md)
- [func readAttributeCurrentMode(with: MTRReadParams?) -> [String : Any]?](./mtrclustermodeselect/readattributecurrentmode%28with%29.md)
- [func readAttributeDescription(with: MTRReadParams?) -> [String : Any]?](./mtrclustermodeselect/readattributedescription%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustermodeselect/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustermodeselect/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeOnMode(with: MTRReadParams?) -> [String : Any]?](./mtrclustermodeselect/readattributeonmode%28with%29.md)
- [func readAttributeStandardNamespace(with: MTRReadParams?) -> [String : Any]?](./mtrclustermodeselect/readattributestandardnamespace%28with%29.md)
- [func readAttributeStartUpMode(with: MTRReadParams?) -> [String : Any]?](./mtrclustermodeselect/readattributestartupmode%28with%29.md)
- [func readAttributeSupportedModes(with: MTRReadParams?) -> [String : Any]?](./mtrclustermodeselect/readattributesupportedmodes%28with%29.md)
- [func writeAttributeOnMode(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustermodeselect/writeattributeonmode%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeOnMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustermodeselect/writeattributeonmode%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeStartUpMode(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustermodeselect/writeattributestartupmode%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeStartUpMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustermodeselect/writeattributestartupmode%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustermodeselect)*