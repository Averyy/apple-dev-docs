# MTRClusterAccessControl

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
class MTRClusterAccessControl
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusteraccesscontrol/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusteraccesscontrol/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeACL(with: MTRReadParams?) -> [String : Any]?](mtrclusteraccesscontrol/readattributeacl(with:)-4l4no.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteraccesscontrol/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAccessControlEntriesPerFabric(with: MTRReadParams?) -> [String : Any]?](mtrclusteraccesscontrol/readattributeaccesscontrolentriesperfabric(with:).md)
- [func readAttributeAcl(with: MTRReadParams?) -> [String : Any]](mtrclusteraccesscontrol/readattributeacl(with:)-7usq4.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusteraccesscontrol/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusteraccesscontrol/readattributeclusterrevision(with:).md)
- [func readAttributeExtension(with: MTRReadParams?) -> [String : Any]?](mtrclusteraccesscontrol/readattributeextension(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusteraccesscontrol/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteraccesscontrol/readattributegeneratedcommandlist(with:).md)
- [func readAttributeSubjectsPerAccessControlEntry(with: MTRReadParams?) -> [String : Any]?](mtrclusteraccesscontrol/readattributesubjectsperaccesscontrolentry(with:).md)
- [func readAttributeTargetsPerAccessControlEntry(with: MTRReadParams?) -> [String : Any]?](mtrclusteraccesscontrol/readattributetargetsperaccesscontrolentry(with:).md)
- [func writeAttributeACL(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteraccesscontrol/writeattributeacl(withvalue:expectedvalueinterval:)-69lwc.md)
- [func writeAttributeACL(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteraccesscontrol/writeattributeacl(withvalue:expectedvalueinterval:params:)-o1ih.md)
- [func writeAttributeAcl(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteraccesscontrol/writeattributeacl(withvalue:expectedvalueinterval:)-6povm.md)
- [func writeAttributeAcl(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteraccesscontrol/writeattributeacl(withvalue:expectedvalueinterval:params:)-9dn9j.md)
- [func writeAttributeExtension(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusteraccesscontrol/writeattributeextension(withvalue:expectedvalueinterval:).md)
- [func writeAttributeExtension(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusteraccesscontrol/writeattributeextension(withvalue:expectedvalueinterval:params:).md)
- [func readAttributeARL(with: MTRReadParams?) -> [String : Any]?](mtrclusteraccesscontrol/readattributearl(with:).md)
- [func readAttributeCommissioningARL(with: MTRReadParams?) -> [String : Any]?](mtrclusteraccesscontrol/readattributecommissioningarl(with:).md)
- [func reviewFabricRestrictions(with: MTRAccessControlClusterReviewFabricRestrictionsParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRAccessControlClusterReviewFabricRestrictionsResponseParams?, (any Error)?) -> Void)](mtrclusteraccesscontrol/reviewfabricrestrictions(with:expectedvalues:expectedvalueinterval:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteraccesscontrol)*