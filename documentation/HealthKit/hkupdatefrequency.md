# HKUpdateFrequency

**Framework**: HealthKit  
**Kind**: enum

Constants that determine how often the system launches your app in response to changes to HealthKit data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum HKUpdateFrequency
```

#### Overview

For more information, see [`HKObserverQuery`](hkobserverquery.md).

## Topics

### Constants
- [HKUpdateFrequency.immediate](hkupdatefrequency/immediate.md)
  The system launches your app every time it detects a change.
- [HKUpdateFrequency.hourly](hkupdatefrequency/hourly.md)
  The system launches your app at most once an hour in response to changes.
- [HKUpdateFrequency.daily](hkupdatefrequency/daily.md)
  The system launches your app at most once a day in response to changes.
- [HKUpdateFrequency.weekly](hkupdatefrequency/weekly.md)
  The system launches your app at most once per week in response to changes.
### Initializers
- [init?(rawValue: Int)](hkupdatefrequency/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func enableBackgroundDelivery(for: HKObjectType, frequency: HKUpdateFrequency, withCompletion: (Bool, (any Error)?) -> Void)](hkhealthstore/enablebackgrounddelivery(for:frequency:withcompletion:).md)
  Enables the delivery of updates to an app running in the background.
- [com.apple.developer.healthkit.background-delivery](../BundleResources/Entitlements/com.apple.developer.healthkit.background-delivery.md)
  A Boolean value that indicates whether observer queries receive updates while running in the background.
- [func disableBackgroundDelivery(for: HKObjectType, withCompletion: (Bool, (any Error)?) -> Void)](hkhealthstore/disablebackgrounddelivery(for:withcompletion:).md)
  Disables background deliveries of update notifications for the specified data type.
- [func disableAllBackgroundDelivery(completion: (Bool, (any Error)?) -> Void)](hkhealthstore/disableallbackgrounddelivery(completion:).md)
  Disables all background deliveries of update notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkupdatefrequency)*