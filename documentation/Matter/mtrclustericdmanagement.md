# MTRClusterICDManagement

**Framework**: Matter  
**Kind**: class

Cluster ICD Management Allows servers to ensure that listed clients are notified when a server is available for communication.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
class MTRClusterICDManagement
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclustericdmanagement/init(device:endpointid:queue:).md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustericdmanagement/readattributeacceptedcommandlist(with:).md)
- [func readAttributeActiveModeDuration(with: MTRReadParams?) -> [String : Any]?](mtrclustericdmanagement/readattributeactivemodeduration(with:).md)
- [func readAttributeActiveModeThreshold(with: MTRReadParams?) -> [String : Any]?](mtrclustericdmanagement/readattributeactivemodethreshold(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclustericdmanagement/readattributeattributelist(with:).md)
- [func readAttributeClientsSupportedPerFabric(with: MTRReadParams?) -> [String : Any]?](mtrclustericdmanagement/readattributeclientssupportedperfabric(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclustericdmanagement/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclustericdmanagement/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclustericdmanagement/readattributegeneratedcommandlist(with:).md)
- [func readAttributeICDCounter(with: MTRReadParams?) -> [String : Any]?](mtrclustericdmanagement/readattributeicdcounter(with:).md)
- [func readAttributeIdleModeDuration(with: MTRReadParams?) -> [String : Any]?](mtrclustericdmanagement/readattributeidlemodeduration(with:).md)
- [func readAttributeMaximumCheckInBackOff(with: MTRReadParams?) -> [String : Any]?](mtrclustericdmanagement/readattributemaximumcheckinbackoff(with:).md)
- [func readAttributeOperatingMode(with: MTRReadParams?) -> [String : Any]?](mtrclustericdmanagement/readattributeoperatingmode(with:).md)
- [func readAttributeRegisteredClients(with: MTRReadParams?) -> [String : Any]?](mtrclustericdmanagement/readattributeregisteredclients(with:).md)
- [func readAttributeUserActiveModeTriggerHint(with: MTRReadParams?) -> [String : Any]?](mtrclustericdmanagement/readattributeuseractivemodetriggerhint(with:).md)
- [func readAttributeUserActiveModeTriggerInstruction(with: MTRReadParams?) -> [String : Any]?](mtrclustericdmanagement/readattributeuseractivemodetriggerinstruction(with:).md)
- [func registerClient(with: MTRICDManagementClusterRegisterClientParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRICDManagementClusterRegisterClientResponseParams?, (any Error)?) -> Void)](mtrclustericdmanagement/registerclient(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func stayActiveRequest(with: MTRICDManagementClusterStayActiveRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRICDManagementClusterStayActiveResponseParams?, (any Error)?) -> Void)](mtrclustericdmanagement/stayactiverequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func unregisterClient(with: MTRICDManagementClusterUnregisterClientParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclustericdmanagement/unregisterclient(with:expectedvalues:expectedvalueinterval:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustericdmanagement)*