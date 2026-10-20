# handleApplyUpdateRequest(forNodeID:controller:params:completionHandler:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

## Declaration

```swift
optional func handleApplyUpdateRequest(forNodeID nodeID: NSNumber, controller: MTRDeviceController, params: MTROtaSoftwareUpdateProviderClusterApplyUpdateRequestParams, completionHandler: @escaping @Sendable (MTROtaSoftwareUpdateProviderClusterApplyUpdateResponseParams?, (any Error)?) -> Void)
```

```swift
optional func handleApplyUpdateRequest(forNodeID nodeID: NSNumber, controller: MTRDeviceController, params: MTROtaSoftwareUpdateProviderClusterApplyUpdateRequestParams) async throws -> MTROtaSoftwareUpdateProviderClusterApplyUpdateResponseParams
```

```objc
- (void) handleApplyUpdateRequestForNodeID:(NSNumber *) nodeID controller:(MTRDeviceController *) controller params:(MTROtaSoftwareUpdateProviderClusterApplyUpdateRequestParams *) params completionHandler:(void (^)(MTROtaSoftwareUpdateProviderClusterApplyUpdateResponseParams *data, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrotaproviderdelegate/handleapplyupdaterequest(fornodeid:controller:params:completionhandler:))*