# subscribeAttributeRmsExtremeUnderVoltage(withMinInterval:maxInterval:params:subscriptionEstablished:reportHandler:)

**Framework**: Matter  
**Kind**: method

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
func subscribeAttributeRmsExtremeUnderVoltage(withMinInterval minInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, subscriptionEstablished subscriptionEstablishedHandler: MTRSubscriptionEstablishedHandler?, reportHandler: @escaping (NSNumber?, (any Error)?) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterelectricalmeasurement/subscribeattributermsextremeundervoltage(withmininterval:maxinterval:params:subscriptionestablished:reporthandler:))*