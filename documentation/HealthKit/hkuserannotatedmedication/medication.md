# medication

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A reference to the specific medication a person is tracking.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@NSCopying
var medication: HKMedicationConcept { get }
```

```objc
@property (nonatomic, copy, readonly) HKMedicationConcept * medication;
```

## Discussion

This concept’s identifier is directly associated with the logged dose events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkuserannotatedmedication/medication)*