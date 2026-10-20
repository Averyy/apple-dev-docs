# MTRClusterGroupKeyManagement

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
class MTRClusterGroupKeyManagement
```

```objc
@interface MTRClusterGroupKeyManagement : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclustergroupkeymanagement/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustergroupkeymanagement/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func keySetRead(with: MTRGroupKeyManagementClusterKeySetReadParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGroupKeyManagementClusterKeySetReadResponseParams?, (any Error)?) -> Void)](./mtrclustergroupkeymanagement/keysetread%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func keySetRead(with: MTRGroupKeyManagementClusterKeySetReadParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGroupKeyManagementClusterKeySetReadResponseParams?, (any Error)?) -> Void)](./mtrclustergroupkeymanagement/keysetread%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func keySetReadAllIndices(with: MTRGroupKeyManagementClusterKeySetReadAllIndicesParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams?, (any Error)?) -> Void)](./mtrclustergroupkeymanagement/keysetreadallindices%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func keySetReadAllIndices(with: MTRGroupKeyManagementClusterKeySetReadAllIndicesParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams?, (any Error)?) -> Void)](./mtrclustergroupkeymanagement/keysetreadallindices%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func keySetReadAllIndices(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams?, (any Error)?) -> Void)](./mtrclustergroupkeymanagement/keysetreadallindices%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func keySetRemove(with: MTRGroupKeyManagementClusterKeySetRemoveParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustergroupkeymanagement/keysetremove%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func keySetRemove(with: MTRGroupKeyManagementClusterKeySetRemoveParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustergroupkeymanagement/keysetremove%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func keySetWrite(with: MTRGroupKeyManagementClusterKeySetWriteParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustergroupkeymanagement/keysetwrite%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func keySetWrite(with: MTRGroupKeyManagementClusterKeySetWriteParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustergroupkeymanagement/keysetwrite%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustergroupkeymanagement/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustergroupkeymanagement/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustergroupkeymanagement/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustergroupkeymanagement/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustergroupkeymanagement/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeGroupKeyMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustergroupkeymanagement/readattributegroupkeymap%28with%29.md)
- [func readAttributeGroupTable(with: MTRReadParams?) -> [String : Any]?](./mtrclustergroupkeymanagement/readattributegrouptable%28with%29.md)
- [func readAttributeMaxGroupKeysPerFabric(with: MTRReadParams?) -> [String : Any]?](./mtrclustergroupkeymanagement/readattributemaxgroupkeysperfabric%28with%29.md)
- [func readAttributeMaxGroupsPerFabric(with: MTRReadParams?) -> [String : Any]?](./mtrclustergroupkeymanagement/readattributemaxgroupsperfabric%28with%29.md)
- [func writeAttributeGroupKeyMap(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclustergroupkeymanagement/writeattributegroupkeymap%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeGroupKeyMap(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclustergroupkeymanagement/writeattributegroupkeymap%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustergroupkeymanagement)*