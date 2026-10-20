# MTRClusterOtaSoftwareUpdateProvider

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

> **Deprecated**: Please use MTRClusterOTASoftwareUpdateProvider

## Declaration

```swift
class MTRClusterOtaSoftwareUpdateProvider
```

```objc
@interface MTRClusterOtaSoftwareUpdateProvider : MTRClusterOTASoftwareUpdateProvider
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterotasoftwareupdateprovider-4p8us/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterotasoftwareupdateprovider-wrfu/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func applyUpdateRequest(with: MTROtaSoftwareUpdateProviderClusterApplyUpdateRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROtaSoftwareUpdateProviderClusterApplyUpdateResponseParams?, (any Error)?) -> Void)](./mtrclusterotasoftwareupdateprovider-4p8us/applyupdaterequest%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func notifyUpdateApplied(with: MTROtaSoftwareUpdateProviderClusterNotifyUpdateAppliedParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterotasoftwareupdateprovider-4p8us/notifyupdateapplied%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func queryImage(with: MTROtaSoftwareUpdateProviderClusterQueryImageParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTROtaSoftwareUpdateProviderClusterQueryImageResponseParams?, (any Error)?) -> Void)](./mtrclusterotasoftwareupdateprovider-4p8us/queryimage%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func applyUpdateRequest(with: MTROTASoftwareUpdateProviderClusterApplyUpdateRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROTASoftwareUpdateProviderClusterApplyUpdateResponseParams?, (any Error)?) -> Void)](./mtrclusterotasoftwareupdateprovider-wrfu/applyupdaterequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func notifyUpdateApplied(with: MTROTASoftwareUpdateProviderClusterNotifyUpdateAppliedParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterotasoftwareupdateprovider-wrfu/notifyupdateapplied%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func queryImage(with: MTROTASoftwareUpdateProviderClusterQueryImageParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTROTASoftwareUpdateProviderClusterQueryImageResponseParams?, (any Error)?) -> Void)](./mtrclusterotasoftwareupdateprovider-wrfu/queryimage%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterotasoftwareupdateprovider-wrfu/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterotasoftwareupdateprovider-wrfu/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterotasoftwareupdateprovider-wrfu/readattributeclusterrevision%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterotasoftwareupdateprovider-wrfu/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterotasoftwareupdateprovider-wrfu/readattributegeneratedcommandlist%28with%29.md)

## Relationships

### Inherits From
- [MTRClusterOTASoftwareUpdateProvider](./mtrclusterotasoftwareupdateprovider-wrfu.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterotasoftwareupdateprovider-4p8us)*