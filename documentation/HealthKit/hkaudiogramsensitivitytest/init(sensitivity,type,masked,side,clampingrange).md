# init(sensitivity:type:masked:side:clampingRange:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.1+
- watchOS 11.1+

## Declaration

```swift
init(sensitivity: HKQuantity, type: HKAudiogramConductionType, masked: Bool, side: HKAudiogramSensitivityTestSide, clampingRange: HKAudiogramSensitivityPointClampingRange?) throws
```

```objc
- (instancetype) initWithSensitivity:(HKQuantity *) sensitivity type:(HKAudiogramConductionType) type masked:(BOOL) masked side:(HKAudiogramSensitivityTestSide) side clampingRange:(HKAudiogramSensitivityPointClampingRange *) clampingRange error:(NSError **) errorOut;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsensitivitytest/init(sensitivity:type:masked:side:clampingrange:))*