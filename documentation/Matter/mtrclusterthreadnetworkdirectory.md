# MTRClusterThreadNetworkDirectory

**Framework**: Matter  
**Kind**: class  
**Role**: Class

Cluster Thread Network Directory Manages the names and credentials of Thread networks visible to the user.

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
class MTRClusterThreadNetworkDirectory
```

```objc
@interface MTRClusterThreadNetworkDirectory : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterthreadnetworkdirectory/init%28device,endpointid,queue%29.md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func addNetwork(with: MTRThreadNetworkDirectoryClusterAddNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterthreadnetworkdirectory/addnetwork%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func getOperationalDataset(with: MTRThreadNetworkDirectoryClusterGetOperationalDatasetParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRThreadNetworkDirectoryClusterOperationalDatasetResponseParams?, (any Error)?) -> Void)](./mtrclusterthreadnetworkdirectory/getoperationaldataset%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdirectory/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdirectory/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdirectory/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdirectory/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdirectory/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributePreferredExtendedPanID(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdirectory/readattributepreferredextendedpanid%28with%29.md)
- [func readAttributeThreadNetworkTableSize(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdirectory/readattributethreadnetworktablesize%28with%29.md)
- [func readAttributeThreadNetworks(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdirectory/readattributethreadnetworks%28with%29.md)
- [func removeNetwork(with: MTRThreadNetworkDirectoryClusterRemoveNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterthreadnetworkdirectory/removenetwork%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func writeAttributePreferredExtendedPanID(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthreadnetworkdirectory/writeattributepreferredextendedpanid%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributePreferredExtendedPanID(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthreadnetworkdirectory/writeattributepreferredextendedpanid%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterthreadnetworkdirectory)*