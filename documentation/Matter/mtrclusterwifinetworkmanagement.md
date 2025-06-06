# MTRClusterWiFiNetworkManagement

**Framework**: Matter  
**Kind**: class

Cluster Wi-Fi Network Management Functionality to retrieve operational information about a managed Wi-Fi network.

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
class MTRClusterWiFiNetworkManagement
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterwifinetworkmanagement/init(device:endpointid:queue:).md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func networkPassphraseRequest(with: MTRWiFiNetworkManagementClusterNetworkPassphraseRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRWiFiNetworkManagementClusterNetworkPassphraseResponseParams?, (any Error)?) -> Void)](mtrclusterwifinetworkmanagement/networkpassphraserequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func networkPassphraseRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRWiFiNetworkManagementClusterNetworkPassphraseResponseParams?, (any Error)?) -> Void)](mtrclusterwifinetworkmanagement/networkpassphraserequest(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkmanagement/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkmanagement/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkmanagement/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkmanagement/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkmanagement/readattributegeneratedcommandlist(with:).md)
- [func readAttributePassphraseSurrogate(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkmanagement/readattributepassphrasesurrogate(with:).md)
- [func readAttributeSSID(with: MTRReadParams?) -> [String : Any]?](mtrclusterwifinetworkmanagement/readattributessid(with:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterwifinetworkmanagement)*