# MTRClusterAdministratorCommissioning

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
class MTRClusterAdministratorCommissioning
```

```objc
@interface MTRClusterAdministratorCommissioning : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusteradministratorcommissioning/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusteradministratorcommissioning/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func openBasicCommissioningWindow(with: MTRAdministratorCommissioningClusterOpenBasicCommissioningWindowParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteradministratorcommissioning/openbasiccommissioningwindow%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func openBasicCommissioningWindow(with: MTRAdministratorCommissioningClusterOpenBasicCommissioningWindowParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteradministratorcommissioning/openbasiccommissioningwindow%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func openWindow(with: MTRAdministratorCommissioningClusterOpenCommissioningWindowParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteradministratorcommissioning/openwindow%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func openWindow(with: MTRAdministratorCommissioningClusterOpenCommissioningWindowParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteradministratorcommissioning/openwindow%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteradministratorcommissioning/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAdminFabricIndex(with: MTRReadParams?) -> [String : Any]?](./mtrclusteradministratorcommissioning/readattributeadminfabricindex%28with%29.md)
- [func readAttributeAdminVendorId(with: MTRReadParams?) -> [String : Any]?](./mtrclusteradministratorcommissioning/readattributeadminvendorid%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteradministratorcommissioning/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusteradministratorcommissioning/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusteradministratorcommissioning/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusteradministratorcommissioning/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeWindowStatus(with: MTRReadParams?) -> [String : Any]?](./mtrclusteradministratorcommissioning/readattributewindowstatus%28with%29.md)
- [func revokeCommissioning(with: MTRAdministratorCommissioningClusterRevokeCommissioningParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteradministratorcommissioning/revokecommissioning%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func revokeCommissioning(with: MTRAdministratorCommissioningClusterRevokeCommissioningParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteradministratorcommissioning/revokecommissioning%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func revokeCommissioning(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusteradministratorcommissioning/revokecommissioning%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func revokeCommissioning(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusteradministratorcommissioning/revokecommissioning%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusteradministratorcommissioning)*