# MTRClusterOTASoftwareUpdateProvider

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
class MTRClusterOTASoftwareUpdateProvider
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterotasoftwareupdateprovider-wrfu/init(device:endpointid:queue:).md)
### Instance Methods
- [func applyUpdateRequest(with: MTROTASoftwareUpdateProviderClusterApplyUpdateRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROTASoftwareUpdateProviderClusterApplyUpdateResponseParams?, (any Error)?) -> Void)](mtrclusterotasoftwareupdateprovider-wrfu/applyupdaterequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func notifyUpdateApplied(with: MTROTASoftwareUpdateProviderClusterNotifyUpdateAppliedParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterotasoftwareupdateprovider-wrfu/notifyupdateapplied(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func queryImage(with: MTROTASoftwareUpdateProviderClusterQueryImageParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROTASoftwareUpdateProviderClusterQueryImageResponseParams?, (any Error)?) -> Void)](mtrclusterotasoftwareupdateprovider-wrfu/queryimage(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdateprovider-wrfu/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdateprovider-wrfu/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdateprovider-wrfu/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdateprovider-wrfu/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdateprovider-wrfu/readattributegeneratedcommandlist(with:).md)

## Relationships

### Inherits From
- [MTRGenericCluster](mtrgenericcluster.md)
### Inherited By
- [MTRClusterOtaSoftwareUpdateProvider](mtrclusterotasoftwareupdateprovider-4p8us.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterotasoftwareupdateprovider-wrfu)*