# cancelPowerAdjustRequest(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command CancelPowerAdjustRequest

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
func cancelPowerAdjustRequest(with params: MTRDeviceEnergyManagementClusterCancelPowerAdjustRequestParams?, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func cancelPowerAdjustRequest(with params: MTRDeviceEnergyManagementClusterCancelPowerAdjustRequestParams?) async throws
```

```objc
- (void) cancelPowerAdjustRequestWithParams:(MTRDeviceEnergyManagementClusterCancelPowerAdjustRequestParams *) params completion:(MTRStatusCompletion) completion;
```

#### Discussion

Allows a client to cancel an ongoing PowerAdjustmentRequest operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdeviceenergymanagement/cancelpoweradjustrequest(with:completion:))*