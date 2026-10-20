# computePaseVerifier(_:iterations:salt:)

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

> **Deprecated**: Please use computePASEVerifierForSetupPasscode:iterations:salt:error:

## Declaration

```swift
func computePaseVerifier(_ setupPincode: UInt32, iterations: UInt32, salt: Data) -> Data?
```

```objc
- (NSData *) computePaseVerifier:(uint32_t) setupPincode iterations:(uint32_t) iterations salt:(NSData *) salt;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontroller/computepaseverifier(_:iterations:salt:))*