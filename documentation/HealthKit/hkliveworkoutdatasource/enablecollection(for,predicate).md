# enableCollection(for:predicate:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Begins automatically calculating statistics for samples that match the quantity type and predicate.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS
- watchOS 5.0+

## Declaration

```swift
func enableCollection(for quantityType: HKQuantityType, predicate: NSPredicate?)
```

```objc
- (void) enableCollectionForType:(HKQuantityType *) quantityType predicate:(NSPredicate *) predicate;
```

## Mentions

- [Dividing a HealthKit workout into activities](../dividing-a-healthkit-workout-into-activities.md)

## See Also

### Calculating statistics
- [func disableCollection(for: HKQuantityType)](./disablecollection%28for%29.md)
  Stops automatically calculating statistics for the quantity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutdatasource/enablecollection(for:predicate:))*