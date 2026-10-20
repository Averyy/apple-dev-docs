# init(frequency:tests:)

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
convenience init(frequency: HKQuantity, tests: [HKAudiogramSensitivityTest]) throws
```

```objc
+ (instancetype) sensitivityPointWithFrequency:(HKQuantity *) frequency tests:(NSArray<HKAudiogramSensitivityTest *> *) tests error:(NSError **) errorOut;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsensitivitypoint/init(frequency:tests:))*