# disableAllBackgroundDelivery(completion:)

**Framework**: HealthKit  
**Kind**: method

Disables all background deliveries of update notifications.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func disableAllBackgroundDelivery() async throws
```

#### Discussion

Call this method to prevent your app from receiving any additional update notifications while in the background. This method operates asynchronously. As soon as the background deliveries are disabled, this method calls its completion handler on a background queue.

## Parameters

- `completion`: A block that this method calls as soon as the background deliveries are disabled. This block is passed the following parameters:

## See Also

- [class HKObserverQuery](hkobserverquery.md)
  A long-running query that monitors the HealthKit store and updates your app when the HealthKit store saves or deletes a matching sample.
- [func enableBackgroundDelivery(for: HKObjectType, frequency: HKUpdateFrequency, withCompletion: (Bool, (any Error)?) -> Void)](hkhealthstore/enablebackgrounddelivery(for:frequency:withcompletion:).md)
  Enables the delivery of updates to an app running in the background.
- [com.apple.developer.healthkit.background-delivery](../BundleResources/Entitlements/com.apple.developer.healthkit.background-delivery.md)
  A Boolean value that indicates whether observer queries receive updates while running in the background.
- [enum HKUpdateFrequency](hkupdatefrequency.md)
  Constants that determine how often the system launches your app in response to changes to HealthKit data.
- [func disableBackgroundDelivery(for: HKObjectType, withCompletion: (Bool, (any Error)?) -> Void)](hkhealthstore/disablebackgrounddelivery(for:withcompletion:).md)
  Disables background deliveries of update notifications for the specified data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/disableallbackgrounddelivery(completion:))*