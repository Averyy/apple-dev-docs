# medicationDoseEventType

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The data type that identified the samples that store medication dose event data.

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
var medicationDoseEventType: HKMedicationDoseEventType { get }
```

```objc
@property (copy, readonly) HKMedicationDoseEventType * medicationDoseEventType;
```

#### Discussion

You use this type when creating queries or filtering results by sample type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmedicationdoseevent/medicationdoseeventtype)*