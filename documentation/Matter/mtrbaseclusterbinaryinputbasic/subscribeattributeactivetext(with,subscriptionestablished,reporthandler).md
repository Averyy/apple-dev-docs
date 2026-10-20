# subscribeAttributeActiveText(with:subscriptionEstablished:reportHandler:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.4+ - Deprecated in 18.2
- iPadOS 16.4+ - Deprecated in 18.2
- Mac Catalyst 16.4+ - Deprecated in 18.2
- macOS 13.3+ - Deprecated in 15.2
- tvOS 16.4+ - Deprecated in 18.2
- visionOS 1.0+ - Deprecated in 2.2
- watchOS 9.4+ - Deprecated in 11.2

> **Deprecated**: This attribute is deprecated

## Declaration

```swift
func subscribeAttributeActiveText(with params: MTRSubscribeParams, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, reportHandler: @escaping (String?, (any Error)?) -> Void)
```

```objc
- (void) subscribeAttributeActiveTextWithParams:(MTRSubscribeParams *) params subscriptionEstablished:(MTRSubscriptionEstablishedHandler) subscriptionEstablished reportHandler:(void (^)(NSString *value, NSError *error)) reportHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbinaryinputbasic/subscribeattributeactivetext(with:subscriptionestablished:reporthandler:))*