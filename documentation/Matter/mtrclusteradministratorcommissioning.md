# MTRClusterAdministratorCommissioning

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
class MTRClusterAdministratorCommissioning
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusteradministratorcommissioning/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusteradministratorcommissioning/init(device:endpointid:queue:).md)
### Instance Methods
- [func openBasicCommissioningWindow(with: MTRAdministratorCommissioningClusterOpenBasicCommissioningWindowParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteradministratorcommissioning/openbasiccommissioningwindow(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func openBasicCommissioningWindow(with: MTRAdministratorCommissioningClusterOpenBasicCommissioningWindowParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteradministratorcommissioning/openbasiccommissioningwindow(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func openWindow(with: MTRAdministratorCommissioningClusterOpenCommissioningWindowParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteradministratorcommissioning/openwindow(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func openWindow(with: MTRAdministratorCommissioningClusterOpenCommissioningWindowParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteradministratorcommissioning/openwindow(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteradministratorcommissioning/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAdminFabricIndex(with: MTRReadParams?) -> [String : Any]?](mtrclusteradministratorcommissioning/readattributeadminfabricindex(with:).md)
- [func readAttributeAdminVendorId(with: MTRReadParams?) -> [String : Any]?](mtrclusteradministratorcommissioning/readattributeadminvendorid(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusteradministratorcommissioning/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusteradministratorcommissioning/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusteradministratorcommissioning/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusteradministratorcommissioning/readattributegeneratedcommandlist(with:).md)
- [func readAttributeWindowStatus(with: MTRReadParams?) -> [String : Any]?](mtrclusteradministratorcommissioning/readattributewindowstatus(with:).md)
- [func revokeCommissioning(with: MTRAdministratorCommissioningClusterRevokeCommissioningParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteradministratorcommissioning/revokecommissioning(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func revokeCommissioning(with: MTRAdministratorCommissioningClusterRevokeCommissioningParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteradministratorcommissioning/revokecommissioning(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func revokeCommissioning(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusteradministratorcommissioning/revokecommissioning(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func revokeCommissioning(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusteradministratorcommissioning/revokecommissioning(withexpectedvalues:expectedvalueinterval:completionhandler:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteradministratorcommissioning)*