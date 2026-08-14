# HKMetadataKeyMenstrualCycleStart

**Framework**: HealthKit  
**Kind**: var

A key that indicates whether the sample represents the start of a menstrual cycle. This metadata key is required for [`menstrualFlow`](hkcategorytypeidentifier/menstrualflow.md) category samples.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HKMetadataKeyMenstrualCycleStart: String
```

#### Discussion

Set this key’s value to [`true`](https://developer.apple.com/documentation/swift/true) if the sample represents the start of a menstrual cycle; otherwise, set it to [`false`](https://developer.apple.com/documentation/swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeymenstrualcyclestart)*