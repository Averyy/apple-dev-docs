# startTimeAdjustRequest(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command StartTimeAdjustRequest

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
func startTimeAdjustRequest(with params: MTRDeviceEnergyManagementClusterStartTimeAdjustRequestParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func startTimeAdjustRequest(with params: MTRDeviceEnergyManagementClusterStartTimeAdjustRequestParams) async throws
```

```objc
- (void) startTimeAdjustRequestWithParams:(MTRDeviceEnergyManagementClusterStartTimeAdjustRequestParams *) params completion:(MTRStatusCompletion) completion;
```

## Discussion

Allows a client to adjust the start time of a Forecast sequence that has not yet started operation (i.e. where the current Forecast StartTime is in the future).


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdeviceenergymanagement/starttimeadjustrequest(with:completion:))*