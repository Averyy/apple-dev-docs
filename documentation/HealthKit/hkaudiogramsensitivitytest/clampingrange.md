# clampingRange

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
var clampingRange: HKAudiogramSensitivityPointClampingRange? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) HKAudiogramSensitivityPointClampingRange * clampingRange;
```

#### Discussion

If present, indicates that the range within which the sensitivity point should be clamped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsensitivitytest/clampingrange)*