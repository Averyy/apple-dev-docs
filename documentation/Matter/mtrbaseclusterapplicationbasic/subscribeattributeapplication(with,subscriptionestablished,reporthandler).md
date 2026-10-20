# subscribeAttributeApplication(with:subscriptionEstablished:reportHandler:)

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
func subscribeAttributeApplication(with params: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: @escaping (MTRApplicationBasicClusterApplicationStruct?, (any Error)?) -> Void)
```

```objc
- (void) subscribeAttributeApplicationWithParams:(MTRSubscribeParams *) params subscriptionEstablished:(MTRSubscriptionEstablishedHandler) subscriptionEstablished reportHandler:(void (^)(MTRApplicationBasicClusterApplicationStruct *value, NSError *error)) reportHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterapplicationbasic/subscribeattributeapplication(with:subscriptionestablished:reporthandler:))*