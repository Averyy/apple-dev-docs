# MTRClusterAccessControl

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
class MTRClusterAccessControl
```

```objc
@interface MTRClusterAccessControl : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusteraccesscontrol/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusteraccesscontrol/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeACL(with: MTRReadParams?) -> [String : Any]?](./mtrclusteraccesscontrol/readattributeacl%28with%29-4l4no.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteraccesscontrol/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAccessControlEntriesPerFabric(with: MTRReadParams?) -> [String : Any]?](./mtrclusteraccesscontrol/readattributeaccesscontrolentriesperfabric%28with%29.md)
- [func readAttributeAcl(with: MTRReadParams?) -> [String : Any]](./mtrclusteraccesscontrol/readattributeacl%28with%29-7usq4.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteraccesscontrol/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusteraccesscontrol/readattributeclusterrevision%28with%29.md)
- [func readAttributeExtension(with: MTRReadParams?) -> [String : Any]?](./mtrclusteraccesscontrol/readattributeextension%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusteraccesscontrol/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteraccesscontrol/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeSubjectsPerAccessControlEntry(with: MTRReadParams?) -> [String : Any]?](./mtrclusteraccesscontrol/readattributesubjectsperaccesscontrolentry%28with%29.md)
- [func readAttributeTargetsPerAccessControlEntry(with: MTRReadParams?) -> [String : Any]?](./mtrclusteraccesscontrol/readattributetargetsperaccesscontrolentry%28with%29.md)
- [func writeAttributeACL(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteraccesscontrol/writeattributeacl%28withvalue,expectedvalueinterval%29-69lwc.md)
- [func writeAttributeACL(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteraccesscontrol/writeattributeacl%28withvalue,expectedvalueinterval,params%29-o1ih.md)
- [func writeAttributeAcl(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteraccesscontrol/writeattributeacl%28withvalue,expectedvalueinterval%29-6povm.md)
- [func writeAttributeAcl(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteraccesscontrol/writeattributeacl%28withvalue,expectedvalueinterval,params%29-9dn9j.md)
- [func writeAttributeExtension(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusteraccesscontrol/writeattributeextension%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeExtension(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusteraccesscontrol/writeattributeextension%28withvalue,expectedvalueinterval,params%29.md)
- [func readAttributeARL(with: MTRReadParams?) -> [String : Any]?](./mtrclusteraccesscontrol/readattributearl%28with%29.md)
- [func readAttributeCommissioningARL(with: MTRReadParams?) -> [String : Any]?](./mtrclusteraccesscontrol/readattributecommissioningarl%28with%29.md)
- [func reviewFabricRestrictions(with: MTRAccessControlClusterReviewFabricRestrictionsParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRAccessControlClusterReviewFabricRestrictionsResponseParams?, (any Error)?) -> Void)](./mtrclusteraccesscontrol/reviewfabricrestrictions%28with,expectedvalues,expectedvalueinterval,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteraccesscontrol)*