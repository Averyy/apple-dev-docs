# cancelRequest(with:completion:)

**Framework**: Matter  
**Kind**: method

Command CancelRequest

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
func cancelRequest(with params: MTRDeviceEnergyManagementClusterCancelRequestParams?) async throws
```

#### Discussion

Allows a client to request cancellation of a previous adjustment request in a StartTimeAdjustRequest, ModifyForecastRequest or RequestConstraintBasedForecast command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdeviceenergymanagement/cancelrequest(with:completion:))*