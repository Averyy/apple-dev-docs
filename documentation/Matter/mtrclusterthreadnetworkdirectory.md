# MTRClusterThreadNetworkDirectory

**Framework**: Matter  
**Kind**: class

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

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterthreadnetworkdirectory/init(device:endpointid:queue:).md)
  For all instance methods that take a completion (i.e. command invocations), the completion will be called on the provided queue.
### Instance Methods
- [func addNetwork(with: MTRThreadNetworkDirectoryClusterAddNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterthreadnetworkdirectory/addnetwork(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func getOperationalDataset(with: MTRThreadNetworkDirectoryClusterGetOperationalDatasetParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRThreadNetworkDirectoryClusterOperationalDatasetResponseParams?, (any Error)?) -> Void)](mtrclusterthreadnetworkdirectory/getoperationaldataset(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdirectory/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdirectory/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdirectory/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdirectory/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdirectory/readattributegeneratedcommandlist(with:).md)
- [func readAttributePreferredExtendedPanID(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdirectory/readattributepreferredextendedpanid(with:).md)
- [func readAttributeThreadNetworkTableSize(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdirectory/readattributethreadnetworktablesize(with:).md)
- [func readAttributeThreadNetworks(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdirectory/readattributethreadnetworks(with:).md)
- [func removeNetwork(with: MTRThreadNetworkDirectoryClusterRemoveNetworkParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterthreadnetworkdirectory/removenetwork(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func writeAttributePreferredExtendedPanID(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterthreadnetworkdirectory/writeattributepreferredextendedpanid(withvalue:expectedvalueinterval:).md)
- [func writeAttributePreferredExtendedPanID(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterthreadnetworkdirectory/writeattributepreferredextendedpanid(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterthreadnetworkdirectory)*