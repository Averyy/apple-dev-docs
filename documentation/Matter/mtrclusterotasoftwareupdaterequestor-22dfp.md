# MTRClusterOtaSoftwareUpdateRequestor

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use MTRClusterOTASoftwareUpdateRequestor

## Declaration

```swift
class MTRClusterOtaSoftwareUpdateRequestor
```

```objc
@interface MTRClusterOtaSoftwareUpdateRequestor : MTRClusterOTASoftwareUpdateRequestor
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterotasoftwareupdaterequestor-22dfp/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterotasoftwareupdaterequestor-5qeao/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func announceOtaProvider(with: MTROtaSoftwareUpdateRequestorClusterAnnounceOtaProviderParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterotasoftwareupdaterequestor-22dfp/announceotaprovider%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeDefaultOtaProviders(with: MTRReadParams?) -> [String : Any]](./mtrclusterotasoftwareupdaterequestor-22dfp/readattributedefaultotaproviders%28with%29.md)
- [func writeAttributeDefaultOtaProviders(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterotasoftwareupdaterequestor-22dfp/writeattributedefaultotaproviders%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeDefaultOtaProviders(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterotasoftwareupdaterequestor-22dfp/writeattributedefaultotaproviders%28withvalue,expectedvalueinterval,params%29.md)
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
- [MTRClusterOTASoftwareUpdateRequestor](./mtrclusterotasoftwareupdaterequestor-5qeao.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterotasoftwareupdaterequestor-22dfp)*