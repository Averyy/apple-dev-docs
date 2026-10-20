# pairDevice(_:onboardingPayload:)

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

> **Deprecated**: Please use setupCommissioningSessionWithPayload:newNodeID:error:

## Declaration

```swift
func pairDevice(_ deviceID: UInt64, onboardingPayload: String) throws
```

```objc
- (BOOL) pairDevice:(uint64_t) deviceID onboardingPayload:(NSString *) onboardingPayload error:(NSError **) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontroller/pairdevice(_:onboardingpayload:))*