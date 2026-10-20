# MTRClusterWiFiNetworkManagement

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterWiFiNetworkManagement : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterwifinetworkmanagement/init%28device,endpointid,queue%29.md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func networkPassphraseRequest(with: MTRWiFiNetworkManagementClusterNetworkPassphraseRequestParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRWiFiNetworkManagementClusterNetworkPassphraseResponseParams?, (any Error)?) -> Void)](./mtrclusterwifinetworkmanagement/networkpassphraserequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func networkPassphraseRequest(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRWiFiNetworkManagementClusterNetworkPassphraseResponseParams?, (any Error)?) -> Void)](./mtrclusterwifinetworkmanagement/networkpassphraserequest%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkmanagement/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkmanagement/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkmanagement/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkmanagement/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkmanagement/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributePassphraseSurrogate(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkmanagement/readattributepassphrasesurrogate%28with%29.md)
- [func readAttributeSSID(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwifinetworkmanagement/readattributessid%28with%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterwifinetworkmanagement)*