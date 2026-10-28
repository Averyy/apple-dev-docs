# pauseRequest(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command PauseRequest

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
func pauseRequest(with params: MTRDeviceEnergyManagementClusterPauseRequestParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func pauseRequest(with params: MTRDeviceEnergyManagementClusterPauseRequestParams) async throws
```

```objc
- (void) pauseRequestWithParams:(MTRDeviceEnergyManagementClusterPauseRequestParams *) params completion:(MTRStatusCompletion) completion;
```

## Discussion

Allows a client to temporarily pause an operation and reduce the ESAs energy demand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdeviceenergymanagement/pauserequest(with:completion:))*