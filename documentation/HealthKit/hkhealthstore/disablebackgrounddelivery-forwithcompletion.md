# disableBackgroundDelivery(for:withCompletion:)

**Framework**: HealthKit  
**Kind**: method

Disables background deliveries of update notifications for the specified data type.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func disableBackgroundDelivery(for type: HKObjectType) async throws
```

#### Discussion

Call this method to prevent your app from receiving any additional update notifications about the specified data type while in the background. This method operates asynchronously. As soon as the background delivery is disabled, this method calls its completion handler on a background queue.

## Parameters

- `type`: The type of data. This object can be any concrete subclass of the   class (any of the classes   ,  ,  ,   or  ).
- `completion`: A block that this method calls as soon as the background delivery is disabled. This block is passed the following parameters:

## See Also

- [class HKObserverQuery](hkobserverquery.md)
  A long-running query that monitors the HealthKit store and updates your app when the HealthKit store saves or deletes a matching sample.
- [func enableBackgroundDelivery(for: HKObjectType, frequency: HKUpdateFrequency, withCompletion: (Bool, (any Error)?) -> Void)](hkhealthstore/enablebackgrounddelivery(for:frequency:withcompletion:).md)
  Enables the delivery of updates to an app running in the background.
- [com.apple.developer.healthkit.background-delivery](../BundleResources/Entitlements/com.apple.developer.healthkit.background-delivery.md)
  A Boolean value that indicates whether observer queries receive updates while running in the background.
- [enum HKUpdateFrequency](hkupdatefrequency.md)
  Constants that determine how often the system launches your app in response to changes to HealthKit data.
- [func disableAllBackgroundDelivery(completion: (Bool, (any Error)?) -> Void)](hkhealthstore/disableallbackgrounddelivery(completion:).md)
  Disables all background deliveries of update notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/disablebackgrounddelivery(for:withcompletion:))*