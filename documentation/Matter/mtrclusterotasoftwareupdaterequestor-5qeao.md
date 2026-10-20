# MTRClusterOTASoftwareUpdateRequestor

**Framework**: Matter  
**Kind**: class  
**Role**: Class

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

```objc
@interface MTRClusterOTASoftwareUpdateRequestor : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterotasoftwareupdaterequestor-5qeao/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func announceOTAProvider(with: MTROTASoftwareUpdateRequestorClusterAnnounceOTAProviderParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterotasoftwareupdaterequestor-5qeao/announceotaprovider%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterotasoftwareupdaterequestor-5qeao/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterotasoftwareupdaterequestor-5qeao/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterotasoftwareupdaterequestor-5qeao/readattributeclusterrevision%28with%29.md)
- [func readAttributeDefaultOTAProviders(with: MTRReadParams?) -> [String : Any]?](./mtrclusterotasoftwareupdaterequestor-5qeao/readattributedefaultotaproviders%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterotasoftwareupdaterequestor-5qeao/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterotasoftwareupdaterequestor-5qeao/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeUpdatePossible(with: MTRReadParams?) -> [String : Any]?](./mtrclusterotasoftwareupdaterequestor-5qeao/readattributeupdatepossible%28with%29.md)
- [func readAttributeUpdateState(with: MTRReadParams?) -> [String : Any]?](./mtrclusterotasoftwareupdaterequestor-5qeao/readattributeupdatestate%28with%29.md)
- [func readAttributeUpdateStateProgress(with: MTRReadParams?) -> [String : Any]?](./mtrclusterotasoftwareupdaterequestor-5qeao/readattributeupdatestateprogress%28with%29.md)
- [func writeAttributeDefaultOTAProviders(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterotasoftwareupdaterequestor-5qeao/writeattributedefaultotaproviders%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeDefaultOTAProviders(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterotasoftwareupdaterequestor-5qeao/writeattributedefaultotaproviders%28withvalue,expectedvalueinterval,params%29.md)

## Relationships

### Inherits From
- [MTRGenericCluster](./mtrgenericcluster.md)
### Inherited By
- [MTRClusterOtaSoftwareUpdateRequestor](./mtrclusterotasoftwareupdaterequestor-22dfp.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterotasoftwareupdaterequestor-5qeao)*