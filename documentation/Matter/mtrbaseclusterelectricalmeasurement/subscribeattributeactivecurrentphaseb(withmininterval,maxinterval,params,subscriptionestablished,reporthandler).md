# subscribeAttributeActiveCurrentPhaseB(withMinInterval:maxInterval:params:subscriptionEstablished:reportHandler:)

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

> **Deprecated**: Please use subscribeAttributeActiveCurrentPhaseBWithParams:subscriptionEstablished:

## Declaration

```swift
func subscribeAttributeActiveCurrentPhaseB(withMinInterval minInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished subscriptionEstablishedHandler: MTRSubscriptionEstablishedHandler?, reportHandler: @escaping (NSNumber?, (any Error)?) -> Void)
```

```objc
- (void) subscribeAttributeActiveCurrentPhaseBWithMinInterval:(NSNumber *) minInterval maxInterval:(NSNumber *) maxInterval params:(MTRSubscribeParams *) params subscriptionEstablished:(MTRSubscriptionEstablishedHandler) subscriptionEstablishedHandler reportHandler:(void (^)(NSNumber *value, NSError *error)) reportHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterelectricalmeasurement/subscribeattributeactivecurrentphaseb(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:))*