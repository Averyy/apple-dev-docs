# MTRClusterICDManagement

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterICDManagement : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclustericdmanagement/init%28device,endpointid,queue%29.md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustericdmanagement/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeActiveModeDuration(with: MTRReadParams?) -> [String : Any]?](./mtrclustericdmanagement/readattributeactivemodeduration%28with%29.md)
- [func readAttributeActiveModeThreshold(with: MTRReadParams?) -> [String : Any]?](./mtrclustericdmanagement/readattributeactivemodethreshold%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclustericdmanagement/readattributeattributelist%28with%29.md)
- [func readAttributeClientsSupportedPerFabric(with: MTRReadParams?) -> [String : Any]?](./mtrclustericdmanagement/readattributeclientssupportedperfabric%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclustericdmanagement/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclustericdmanagement/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclustericdmanagement/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeICDCounter(with: MTRReadParams?) -> [String : Any]?](./mtrclustericdmanagement/readattributeicdcounter%28with%29.md)
- [func readAttributeIdleModeDuration(with: MTRReadParams?) -> [String : Any]?](./mtrclustericdmanagement/readattributeidlemodeduration%28with%29.md)
- [func readAttributeMaximumCheckInBackOff(with: MTRReadParams?) -> [String : Any]?](./mtrclustericdmanagement/readattributemaximumcheckinbackoff%28with%29.md)
- [func readAttributeOperatingMode(with: MTRReadParams?) -> [String : Any]?](./mtrclustericdmanagement/readattributeoperatingmode%28with%29.md)
- [func readAttributeRegisteredClients(with: MTRReadParams?) -> [String : Any]?](./mtrclustericdmanagement/readattributeregisteredclients%28with%29.md)
- [func readAttributeUserActiveModeTriggerHint(with: MTRReadParams?) -> [String : Any]?](./mtrclustericdmanagement/readattributeuseractivemodetriggerhint%28with%29.md)
- [func readAttributeUserActiveModeTriggerInstruction(with: MTRReadParams?) -> [String : Any]?](./mtrclustericdmanagement/readattributeuseractivemodetriggerinstruction%28with%29.md)
- [func registerClient(with: MTRICDManagementClusterRegisterClientParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRICDManagementClusterRegisterClientResponseParams?, (any Error)?) -> Void)](./mtrclustericdmanagement/registerclient%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func stayActiveRequest(with: MTRICDManagementClusterStayActiveRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRICDManagementClusterStayActiveResponseParams?, (any Error)?) -> Void)](./mtrclustericdmanagement/stayactiverequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func unregisterClient(with: MTRICDManagementClusterUnregisterClientParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclustericdmanagement/unregisterclient%28with,expectedvalues,expectedvalueinterval,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustericdmanagement)*