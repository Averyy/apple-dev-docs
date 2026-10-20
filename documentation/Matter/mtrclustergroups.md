# MTRClusterGroups

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
class MTRClusterGroups
```

```objc
@interface MTRClusterGroups : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclustergroups/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustergroups/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func addGroup(with: MTRGroupsClusterAddGroupParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGroupsClusterAddGroupResponseParams?, (any Error)?) -> Void)](./mtrclustergroups/addgroup%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func addGroup(with: MTRGroupsClusterAddGroupParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGroupsClusterAddGroupResponseParams?, (any Error)?) -> Void)](./mtrclustergroups/addgroup%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func addGroupIfIdentifying(with: MTRGroupsClusterAddGroupIfIdentifyingParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustergroups/addgroupifidentifying%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func addGroupIfIdentifying(with: MTRGroupsClusterAddGroupIfIdentifyingParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustergroups/addgroupifidentifying%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func getGroupMembership(with: MTRGroupsClusterGetGroupMembershipParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGroupsClusterGetGroupMembershipResponseParams?, (any Error)?) -> Void)](./mtrclustergroups/getgroupmembership%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func getGroupMembership(with: MTRGroupsClusterGetGroupMembershipParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGroupsClusterGetGroupMembershipResponseParams?, (any Error)?) -> Void)](./mtrclustergroups/getgroupmembership%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustergroups/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustergroups/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustergroups/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustergroups/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustergroups/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeNameSupport(with: MTRReadParams?) -> [String : Any]?](./mtrclustergroups/readattributenamesupport%28with%29.md)
- [func removeAllGroups(with: MTRGroupsClusterRemoveAllGroupsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustergroups/removeallgroups%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func removeAllGroups(with: MTRGroupsClusterRemoveAllGroupsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustergroups/removeallgroups%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func removeAllGroups(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustergroups/removeallgroups%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func removeAllGroups(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclustergroups/removeallgroups%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func removeGroup(with: MTRGroupsClusterRemoveGroupParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGroupsClusterRemoveGroupResponseParams?, (any Error)?) -> Void)](./mtrclustergroups/removegroup%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func removeGroup(with: MTRGroupsClusterRemoveGroupParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGroupsClusterRemoveGroupResponseParams?, (any Error)?) -> Void)](./mtrclustergroups/removegroup%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func viewGroup(with: MTRGroupsClusterViewGroupParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRGroupsClusterViewGroupResponseParams?, (any Error)?) -> Void)](./mtrclustergroups/viewgroup%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func viewGroup(with: MTRGroupsClusterViewGroupParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRGroupsClusterViewGroupResponseParams?, (any Error)?) -> Void)](./mtrclustergroups/viewgroup%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustergroups)*