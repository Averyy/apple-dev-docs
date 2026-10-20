# HKAppleSleepingBreathingDisturbancesClassification

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum HKAppleSleepingBreathingDisturbancesClassification
```

```c
enum HKAppleSleepingBreathingDisturbancesClassification : NSInteger;
```

## Topics

### Enumeration Cases
- [HKAppleSleepingBreathingDisturbancesClassification.elevated](./hkapplesleepingbreathingdisturbancesclassification/elevated.md)
- [HKAppleSleepingBreathingDisturbancesClassification.notElevated](./hkapplesleepingbreathingdisturbancesclassification/notelevated.md)
### Instance Properties
- [var minimum: HKQuantity](./hkapplesleepingbreathingdisturbancesclassification/minimum.md)
### Initializers
- [init?(classifying: HKQuantity)](./hkapplesleepingbreathingdisturbancesclassification/init%28classifying%29.md)
- [init?(rawValue: Int)](./hkapplesleepingbreathingdisturbancesclassification/init%28rawvalue%29.md)
### Default Implementations
- [CaseIterable Implementations](./hkapplesleepingbreathingdisturbancesclassification/caseiterable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [CaseIterable](../Swift/caseiterable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Mindfulness and sleep
- [static let mindfulSession: HKCategoryTypeIdentifier](./hkcategorytypeidentifier/mindfulsession.md)
  A category sample type for recording a mindful session.
- [static let sleepAnalysis: HKCategoryTypeIdentifier](./hkcategorytypeidentifier/sleepanalysis.md)
  A category sample type for sleep analysis information.
- [static let appleSleepingWristTemperature: HKQuantityTypeIdentifier](./hkquantitytypeidentifier/applesleepingwristtemperature.md)
  A quantity sample type that records the wrist temperature during sleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkapplesleepingbreathingdisturbancesclassification)*