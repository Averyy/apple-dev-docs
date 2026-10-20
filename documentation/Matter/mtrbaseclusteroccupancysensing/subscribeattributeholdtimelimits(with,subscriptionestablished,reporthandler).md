# subscribeAttributeHoldTimeLimits(with:subscriptionEstablished:reportHandler:)

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
func subscribeAttributeHoldTimeLimits(with params: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: @escaping (MTROccupancySensingClusterHoldTimeLimitsStruct?, (any Error)?) -> Void)
```

```objc
- (void) subscribeAttributeHoldTimeLimitsWithParams:(MTRSubscribeParams *) params subscriptionEstablished:(MTRSubscriptionEstablishedHandler) subscriptionEstablished reportHandler:(void (^)(MTROccupancySensingClusterHoldTimeLimitsStruct *value, NSError *error)) reportHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteroccupancysensing/subscribeattributeholdtimelimits(with:subscriptionestablished:reporthandler:))*