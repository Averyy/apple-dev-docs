# MTRClusterOtaSoftwareUpdateProvider

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRClusterOtaSoftwareUpdateProvider
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterotasoftwareupdateprovider-4p8us/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterotasoftwareupdateprovider-wrfu/init(device:endpointid:queue:).md)
### Instance Methods
- [func applyUpdateRequest(with: MTROtaSoftwareUpdateProviderClusterApplyUpdateRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROtaSoftwareUpdateProviderClusterApplyUpdateResponseParams?, (any Error)?) -> Void)](mtrclusterotasoftwareupdateprovider-4p8us/applyupdaterequest(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func notifyUpdateApplied(with: MTROtaSoftwareUpdateProviderClusterNotifyUpdateAppliedParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusterotasoftwareupdateprovider-4p8us/notifyupdateapplied(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func queryImage(with: MTROtaSoftwareUpdateProviderClusterQueryImageParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROtaSoftwareUpdateProviderClusterQueryImageResponseParams?, (any Error)?) -> Void)](mtrclusterotasoftwareupdateprovider-4p8us/queryimage(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func applyUpdateRequest(with: MTROTASoftwareUpdateProviderClusterApplyUpdateRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROTASoftwareUpdateProviderClusterApplyUpdateResponseParams?, (any Error)?) -> Void)](mtrclusterotasoftwareupdateprovider-wrfu/applyupdaterequest(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func notifyUpdateApplied(with: MTROTASoftwareUpdateProviderClusterNotifyUpdateAppliedParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterotasoftwareupdateprovider-wrfu/notifyupdateapplied(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func queryImage(with: MTROTASoftwareUpdateProviderClusterQueryImageParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROTASoftwareUpdateProviderClusterQueryImageResponseParams?, (any Error)?) -> Void)](mtrclusterotasoftwareupdateprovider-wrfu/queryimage(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdateprovider-wrfu/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdateprovider-wrfu/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdateprovider-wrfu/readattributeclusterrevision(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdateprovider-wrfu/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterotasoftwareupdateprovider-wrfu/readattributegeneratedcommandlist(with:).md)

## Relationships

### Inherits From
- [MTRClusterOTASoftwareUpdateProvider](mtrclusterotasoftwareupdateprovider-wrfu.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterotasoftwareupdateprovider-4p8us)*