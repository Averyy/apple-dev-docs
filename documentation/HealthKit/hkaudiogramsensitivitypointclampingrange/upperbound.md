# upperBound

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.1+
- watchOS 11.1+

## Declaration

```swift
@NSCopying
var upperBound: HKQuantity? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) HKQuantity * upperBound;
```

## Discussion

The upper bound of the clamping range, if any, in dBHL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsensitivitypointclampingrange/upperbound)*