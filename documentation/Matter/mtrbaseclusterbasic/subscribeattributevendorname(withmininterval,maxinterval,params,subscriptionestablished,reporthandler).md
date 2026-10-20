# subscribeAttributeVendorName(withMinInterval:maxInterval:params:subscriptionEstablished:reportHandler:)

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

> **Deprecated**: Please use subscribeAttributeVendorNameWithParams:subscriptionEstablished:

## Declaration

```swift
func subscribeAttributeVendorName(withMinInterval minInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished subscriptionEstablishedHandler: MTRSubscriptionEstablishedHandler?, reportHandler: @escaping (String?, (any Error)?) -> Void)
```

```objc
- (void) subscribeAttributeVendorNameWithMinInterval:(NSNumber *) minInterval maxInterval:(NSNumber *) maxInterval params:(MTRSubscribeParams *) params subscriptionEstablished:(MTRSubscriptionEstablishedHandler) subscriptionEstablishedHandler reportHandler:(void (^)(NSString *value, NSError *error)) reportHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbasic/subscribeattributevendorname(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:))*