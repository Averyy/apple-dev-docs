# MTRClusterGroups

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
class MTRClusterGroups
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclustergroups/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustergroups/init(device:endpointid:queue:).md)
### Instance Methods
- [func addGroup(with: MTRGroupsClusterAddGroupParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGroupsClusterAddGroupResponseParams?, (any Error)?) -> Void)](mtrclustergroups/addgroup(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func addGroup(with: MTRGroupsClusterAddGroupParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGroupsClusterAddGroupResponseParams?, (any Error)?) -> Void)](mtrclustergroups/addgroup(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func addGroupIfIdentifying(with: MTRGroupsClusterAddGroupIfIdentifyingParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustergroups/addgroupifidentifying(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func addGroupIfIdentifying(with: MTRGroupsClusterAddGroupIfIdentifyingParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustergroups/addgroupifidentifying(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func getGroupMembership(with: MTRGroupsClusterGetGroupMembershipParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGroupsClusterGetGroupMembershipResponseParams?, (any Error)?) -> Void)](mtrclustergroups/getgroupmembership(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func getGroupMembership(with: MTRGroupsClusterGetGroupMembershipParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGroupsClusterGetGroupMembershipResponseParams?, (any Error)?) -> Void)](mtrclustergroups/getgroupmembership(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustergroups/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustergroups/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustergroups/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustergroups/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustergroups/readattributegeneratedcommandlist(with:).md)
- [func readAttributeNameSupport(with: MTRReadParams?) -> [String : Any]?](mtrclustergroups/readattributenamesupport(with:).md)
- [func removeAllGroups(with: MTRGroupsClusterRemoveAllGroupsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustergroups/removeallgroups(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func removeAllGroups(with: MTRGroupsClusterRemoveAllGroupsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustergroups/removeallgroups(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func removeAllGroups(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclustergroups/removeallgroups(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func removeAllGroups(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclustergroups/removeallgroups(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func removeGroup(with: MTRGroupsClusterRemoveGroupParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGroupsClusterRemoveGroupResponseParams?, (any Error)?) -> Void)](mtrclustergroups/removegroup(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func removeGroup(with: MTRGroupsClusterRemoveGroupParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGroupsClusterRemoveGroupResponseParams?, (any Error)?) -> Void)](mtrclustergroups/removegroup(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func viewGroup(with: MTRGroupsClusterViewGroupParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGroupsClusterViewGroupResponseParams?, (any Error)?) -> Void)](mtrclustergroups/viewgroup(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func viewGroup(with: MTRGroupsClusterViewGroupParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGroupsClusterViewGroupResponseParams?, (any Error)?) -> Void)](mtrclustergroups/viewgroup(with:expectedvalues:expectedvalueinterval:completionhandler:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustergroups)*