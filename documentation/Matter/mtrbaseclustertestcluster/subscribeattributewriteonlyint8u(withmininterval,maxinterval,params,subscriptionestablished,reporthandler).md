# subscribeAttributeWriteOnlyInt8u(withMinInterval:maxInterval:params:subscriptionEstablished:reportHandler:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.2+ - Deprecated in 16.4
- iPadOS 16.2+ - Deprecated in 16.4
- Mac Catalyst 16.2+ - Deprecated in 16.4
- macOS 13.1+ - Deprecated in 13.3
- tvOS 16.2+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.2+ - Deprecated in 9.4

> **Deprecated**: Please use subscribeAttributeWriteOnlyInt8uWithParams:subscriptionEstablished:

## Declaration

```swift
func subscribeAttributeWriteOnlyInt8u(withMinInterval minInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished subscriptionEstablishedHandler: MTRSubscriptionEstablishedHandler?, reportHandler: @escaping (NSNumber?, (any Error)?) -> Void)
```

```objc
- (void) subscribeAttributeWriteOnlyInt8uWithMinInterval:(NSNumber *) minInterval maxInterval:(NSNumber *) maxInterval params:(MTRSubscribeParams *) params subscriptionEstablished:(MTRSubscriptionEstablishedHandler) subscriptionEstablishedHandler reportHandler:(void (^)(NSNumber *value, NSError *error)) reportHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustertestcluster/subscribeattributewriteonlyint8u(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:))*