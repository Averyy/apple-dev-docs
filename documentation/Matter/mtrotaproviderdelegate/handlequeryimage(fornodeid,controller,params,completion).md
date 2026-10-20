# handleQueryImage(forNodeID:controller:params:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

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
optional func handleQueryImage(forNodeID nodeID: NSNumber, controller: MTRDeviceController, params: MTROTASoftwareUpdateProviderClusterQueryImageParams, completion: @escaping @Sendable (MTROTASoftwareUpdateProviderClusterQueryImageResponseParams?, (any Error)?) -> Void)
```

```swift
optional func handleQueryImage(forNodeID nodeID: NSNumber, controller: MTRDeviceController, params: MTROTASoftwareUpdateProviderClusterQueryImageParams) async throws -> MTROTASoftwareUpdateProviderClusterQueryImageResponseParams
```

```objc
- (void) handleQueryImageForNodeID:(NSNumber *) nodeID controller:(MTRDeviceController *) controller params:(MTROTASoftwareUpdateProviderClusterQueryImageParams *) params completion:(void (^)(MTROTASoftwareUpdateProviderClusterQueryImageResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrotaproviderdelegate/handlequeryimage(fornodeid:controller:params:completion:))*