# subscribeAttributeManufacturingDate(with:subscriptionEstablished:reportHandler:)

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
func subscribeAttributeManufacturingDate(with params: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: @escaping (String?, (any Error)?) -> Void)
```

```objc
- (void) subscribeAttributeManufacturingDateWithParams:(MTRSubscribeParams *) params subscriptionEstablished:(MTRSubscriptionEstablishedHandler) subscriptionEstablished reportHandler:(void (^)(NSString *value, NSError *error)) reportHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbasicinformation/subscribeattributemanufacturingdate(with:subscriptionestablished:reporthandler:))*