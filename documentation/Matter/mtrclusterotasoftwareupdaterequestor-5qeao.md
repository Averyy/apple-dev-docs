# MTRClusterOTASoftwareUpdateRequestor

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
class MTRClusterOTASoftwareUpdateRequestor
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterotasoftwareupdaterequestor-5qeao/init(device:endpointid:queue:).md)
### Instance Methods
- [func announceOTAProvider(with: MTROTASoftwareUpdateRequestorClusterAnnounceOTAProviderParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterotasoftwareupdaterequestor-5qeao/announceotaprovider(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdaterequestor-5qeao/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdaterequestor-5qeao/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdaterequestor-5qeao/readattributeclusterrevision(with:).md)
- [func readAttributeDefaultOTAProviders(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdaterequestor-5qeao/readattributedefaultotaproviders(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdaterequestor-5qeao/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdaterequestor-5qeao/readattributegeneratedcommandlist(with:).md)
- [func readAttributeUpdatePossible(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdaterequestor-5qeao/readattributeupdatepossible(with:).md)
- [func readAttributeUpdateState(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdaterequestor-5qeao/readattributeupdatestate(with:).md)
- [func readAttributeUpdateStateProgress(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdaterequestor-5qeao/readattributeupdatestateprogress(with:).md)
- [func writeAttributeDefaultOTAProviders(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterotasoftwareupdaterequestor-5qeao/writeattributedefaultotaproviders(withvalue:expectedvalueinterval:).md)
- [func writeAttributeDefaultOTAProviders(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterotasoftwareupdaterequestor-5qeao/writeattributedefaultotaproviders(withvalue:expectedvalueinterval:params:).md)

## Relationships

### Inherits From
- [MTRGenericCluster](mtrgenericcluster.md)
### Inherited By
- [MTRClusterOtaSoftwareUpdateRequestor](mtrclusterotasoftwareupdaterequestor-22dfp.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterotasoftwareupdaterequestor-5qeao)*