# MTROTAProviderDelegate

**Framework**: Matter  
**Kind**: protocol

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol MTROTAProviderDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func handleApplyUpdateRequest(forNodeID: NSNumber, controller: MTRDeviceController, params: MTROTASoftwareUpdateProviderClusterApplyUpdateRequestParams, completion: (MTROTASoftwareUpdateProviderClusterApplyUpdateResponseParams?, (any Error)?) -> Void)](mtrotaproviderdelegate/handleapplyupdaterequest(fornodeid:controller:params:completion:).md)
- [func handleApplyUpdateRequest(forNodeID: NSNumber, controller: MTRDeviceController, params: MTROtaSoftwareUpdateProviderClusterApplyUpdateRequestParams, completionHandler: (MTROtaSoftwareUpdateProviderClusterApplyUpdateResponseParams?, (any Error)?) -> Void)](mtrotaproviderdelegate/handleapplyupdaterequest(fornodeid:controller:params:completionhandler:).md)
- [func handleBDXQuery(forNodeID: NSNumber, controller: MTRDeviceController, blockSize: NSNumber, blockIndex: NSNumber, bytesToSkip: NSNumber, completion: (Data?, Bool) -> Void)](mtrotaproviderdelegate/handlebdxquery(fornodeid:controller:blocksize:blockindex:bytestoskip:completion:).md)
- [func handleBDXQuery(forNodeID: NSNumber, controller: MTRDeviceController, blockSize: NSNumber, blockIndex: NSNumber, bytesToSkip: NSNumber, completionHandler: (Data?, Bool) -> Void)](mtrotaproviderdelegate/handlebdxquery(fornodeid:controller:blocksize:blockindex:bytestoskip:completionhandler:).md)
- [func handleBDXTransferSessionBegin(forNodeID: NSNumber, controller: MTRDeviceController, fileDesignator: String, offset: NSNumber, completion: ((any Error)?) -> Void)](mtrotaproviderdelegate/handlebdxtransfersessionbegin(fornodeid:controller:filedesignator:offset:completion:).md)
- [func handleBDXTransferSessionBegin(forNodeID: NSNumber, controller: MTRDeviceController, fileDesignator: String, offset: NSNumber, completionHandler: ((any Error)?) -> Void)](mtrotaproviderdelegate/handlebdxtransfersessionbegin(fornodeid:controller:filedesignator:offset:completionhandler:).md)
- [func handleBDXTransferSessionEnd(forNodeID: NSNumber, controller: MTRDeviceController, error: (any Error)?)](mtrotaproviderdelegate/handlebdxtransfersessionend(fornodeid:controller:error:).md)
- [func handleNotifyUpdateApplied(forNodeID: NSNumber, controller: MTRDeviceController, params: MTROTASoftwareUpdateProviderClusterNotifyUpdateAppliedParams, completion: ((any Error)?) -> Void)](mtrotaproviderdelegate/handlenotifyupdateapplied(fornodeid:controller:params:completion:).md)
- [func handleNotifyUpdateApplied(forNodeID: NSNumber, controller: MTRDeviceController, params: MTROtaSoftwareUpdateProviderClusterNotifyUpdateAppliedParams, completionHandler: ((any Error)?) -> Void)](mtrotaproviderdelegate/handlenotifyupdateapplied(fornodeid:controller:params:completionhandler:).md)
- [func handleQueryImage(forNodeID: NSNumber, controller: MTRDeviceController, params: MTROTASoftwareUpdateProviderClusterQueryImageParams, completion: (MTROTASoftwareUpdateProviderClusterQueryImageResponseParams?, (any Error)?) -> Void)](mtrotaproviderdelegate/handlequeryimage(fornodeid:controller:params:completion:).md)
- [func handleQueryImage(forNodeID: NSNumber, controller: MTRDeviceController, params: MTROtaSoftwareUpdateProviderClusterQueryImageParams, completionHandler: (MTROtaSoftwareUpdateProviderClusterQueryImageResponseParams?, (any Error)?) -> Void)](mtrotaproviderdelegate/handlequeryimage(fornodeid:controller:params:completionhandler:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrotaproviderdelegate)*