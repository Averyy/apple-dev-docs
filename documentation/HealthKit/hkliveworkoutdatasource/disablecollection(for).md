# disableCollection(for:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Stops automatically calculating statistics for the quantity type.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS
- watchOS 5.0+

## Declaration

```swift
func disableCollection(for quantityType: HKQuantityType)
```

```objc
- (void) disableCollectionForType:(HKQuantityType *) quantityType;
```

## Mentions

- [Dividing a HealthKit workout into activities](../dividing-a-healthkit-workout-into-activities.md)

## See Also

### Calculating statistics
- [func enableCollection(for: HKQuantityType, predicate: NSPredicate?)](./enablecollection%28for,predicate%29.md)
  Begins automatically calculating statistics for samples that match the quantity type and predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutdatasource/disablecollection(for:))*