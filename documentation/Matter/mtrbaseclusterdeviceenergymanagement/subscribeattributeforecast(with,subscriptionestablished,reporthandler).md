# subscribeAttributeForecast(with:subscriptionEstablished:reportHandler:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

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
func subscribeAttributeForecast(with params: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: @escaping (MTRDeviceEnergyManagementClusterForecastStruct?, (any Error)?) -> Void)
```

```objc
- (void) subscribeAttributeForecastWithParams:(MTRSubscribeParams *) params subscriptionEstablished:(MTRSubscriptionEstablishedHandler) subscriptionEstablished reportHandler:(void (^)(MTRDeviceEnergyManagementClusterForecastStruct *value, NSError *error)) reportHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdeviceenergymanagement/subscribeattributeforecast(with:subscriptionestablished:reporthandler:))*