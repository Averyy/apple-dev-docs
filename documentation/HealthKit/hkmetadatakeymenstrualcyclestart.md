# HKMetadataKeyMenstrualCycleStart

**Framework**: HealthKit  
**Kind**: var  
**Role**: Global Variable

A key that indicates whether the sample represents the start of a menstrual cycle. This metadata key is required for [`menstrualFlow`](./hkcategorytypeidentifier/menstrualflow.md) category samples.

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

```c
extern NSString * const HKMetadataKeyMenstrualCycleStart;
```

#### Discussion

Set this key’s value to [`true`](../Swift/true.md) if the sample represents the start of a menstrual cycle; otherwise, set it to [`false`](../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeymenstrualcyclestart)*