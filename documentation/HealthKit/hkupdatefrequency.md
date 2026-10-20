# HKUpdateFrequency

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum HKUpdateFrequency : NSInteger;
```

#### Overview

For more information, see [`HKObserverQuery`](./hkobserverquery.md).

## Topics

### Constants
- [HKUpdateFrequency.immediate](./hkupdatefrequency/immediate.md)
  The system launches your app every time it detects a change.
- [HKUpdateFrequency.hourly](./hkupdatefrequency/hourly.md)
  The system launches your app at most once an hour in response to changes.
- [HKUpdateFrequency.daily](./hkupdatefrequency/daily.md)
  The system launches your app at most once a day in response to changes.
- [HKUpdateFrequency.weekly](./hkupdatefrequency/weekly.md)
  The system launches your app at most once per week in response to changes.
### Initializers
- [init?(rawValue: Int)](./hkupdatefrequency/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing background delivery
- [func enableBackgroundDelivery(for: HKObjectType, frequency: HKUpdateFrequency, withCompletion: (Bool, (any Error)?) -> Void)](./hkhealthstore/enablebackgrounddelivery%28for,frequency,withcompletion%29.md)
  Enables the delivery of updates to an app running in the background.
- [com.apple.developer.healthkit.background-delivery](../BundleResources/entitlements/com.apple.developer.healthkit.background-delivery.md)
  A Boolean value that indicates whether observer queries receive updates while running in the background.
- [func disableBackgroundDelivery(for: HKObjectType, withCompletion: (Bool, (any Error)?) -> Void)](./hkhealthstore/disablebackgrounddelivery%28for,withcompletion%29.md)
  Disables background deliveries of update notifications for the specified data type.
- [func disableAllBackgroundDelivery(completion: (Bool, (any Error)?) -> Void)](./hkhealthstore/disableallbackgrounddelivery%28completion%29.md)
  Disables all background deliveries of update notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkupdatefrequency)*