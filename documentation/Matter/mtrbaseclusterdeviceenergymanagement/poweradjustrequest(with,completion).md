# powerAdjustRequest(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command PowerAdjustRequest

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
func powerAdjustRequest(with params: MTRDeviceEnergyManagementClusterPowerAdjustRequestParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func powerAdjustRequest(with params: MTRDeviceEnergyManagementClusterPowerAdjustRequestParams) async throws
```

```objc
- (void) powerAdjustRequestWithParams:(MTRDeviceEnergyManagementClusterPowerAdjustRequestParams *) params completion:(MTRStatusCompletion) completion;
```

## Discussion

Allows a client to request an adjustment in the power consumption of an ESA for a specified duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdeviceenergymanagement/poweradjustrequest(with:completion:))*