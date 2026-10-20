# subscribeAttributeProductAppearance(with:subscriptionEstablished:reportHandler:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func subscribeAttributeProductAppearance(with params: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: @escaping (MTRBasicInformationClusterProductAppearanceStruct?, (any Error)?) -> Void)
```

```objc
- (void) subscribeAttributeProductAppearanceWithParams:(MTRSubscribeParams *) params subscriptionEstablished:(MTRSubscriptionEstablishedHandler) subscriptionEstablished reportHandler:(void (^)(MTRBasicInformationClusterProductAppearanceStruct *value, NSError *error)) reportHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbasicinformation/subscribeattributeproductappearance(with:subscriptionestablished:reporthandler:))*