# MTRClusterGroupKeyManagement

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
class MTRClusterGroupKeyManagement
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclustergroupkeymanagement/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustergroupkeymanagement/init(device:endpointid:queue:).md)
### Instance Methods
- [func keySetRead(with: MTRGroupKeyManagementClusterKeySetReadParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGroupKeyManagementClusterKeySetReadResponseParams?, (any Error)?) -> Void)](mtrclustergroupkeymanagement/keysetread(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func keySetRead(with: MTRGroupKeyManagementClusterKeySetReadParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGroupKeyManagementClusterKeySetReadResponseParams?, (any Error)?) -> Void)](mtrclustergroupkeymanagement/keysetread(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func keySetReadAllIndices(with: MTRGroupKeyManagementClusterKeySetReadAllIndicesParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams?, (any Error)?) -> Void)](mtrclustergroupkeymanagement/keysetreadallindices(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func keySetReadAllIndices(with: MTRGroupKeyManagementClusterKeySetReadAllIndicesParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams?, (any Error)?) -> Void)](mtrclustergroupkeymanagement/keysetreadallindices(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func keySetReadAllIndices(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams?, (any Error)?) -> Void)](mtrclustergroupkeymanagement/keysetreadallindices(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func keySetRemove(with: MTRGroupKeyManagementClusterKeySetRemoveParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclustergroupkeymanagement/keysetremove(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func keySetRemove(with: MTRGroupKeyManagementClusterKeySetRemoveParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclustergroupkeymanagement/keysetremove(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func keySetWrite(with: MTRGroupKeyManagementClusterKeySetWriteParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclustergroupkeymanagement/keysetwrite(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func keySetWrite(with: MTRGroupKeyManagementClusterKeySetWriteParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclustergroupkeymanagement/keysetwrite(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustergroupkeymanagement/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustergroupkeymanagement/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustergroupkeymanagement/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustergroupkeymanagement/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustergroupkeymanagement/readattributegeneratedcommandlist(with:).md)
- [func readAttributeGroupKeyMap(with: MTRReadParams?) -> [String : Any]?](mtrclustergroupkeymanagement/readattributegroupkeymap(with:).md)
- [func readAttributeGroupTable(with: MTRReadParams?) -> [String : Any]?](mtrclustergroupkeymanagement/readattributegrouptable(with:).md)
- [func readAttributeMaxGroupKeysPerFabric(with: MTRReadParams?) -> [String : Any]?](mtrclustergroupkeymanagement/readattributemaxgroupkeysperfabric(with:).md)
- [func readAttributeMaxGroupsPerFabric(with: MTRReadParams?) -> [String : Any]?](mtrclustergroupkeymanagement/readattributemaxgroupsperfabric(with:).md)
- [func writeAttributeGroupKeyMap(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclustergroupkeymanagement/writeattributegroupkeymap(withvalue:expectedvalueinterval:).md)
- [func writeAttributeGroupKeyMap(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclustergroupkeymanagement/writeattributegroupkeymap(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustergroupkeymanagement)*