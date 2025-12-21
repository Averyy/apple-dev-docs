# enableCollection(for:predicate:)

**Framework**: HealthKit  
**Kind**: method

Begins automatically calculating statistics for samples that match the quantity type and predicate.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS ?+
- watchOS 5.0+

## Declaration

```swift
func enableCollection(for quantityType: HKQuantityType, predicate: NSPredicate?)
```

## Mentions

- [Dividing a HealthKit workout into activities](dividing-a-healthkit-workout-into-activities.md)

## See Also

- [func disableCollection(for: HKQuantityType)](hkliveworkoutdatasource/disablecollection(for:).md)
  Stops automatically calculating statistics for the quantity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutdatasource/enablecollection(for:predicate:))*