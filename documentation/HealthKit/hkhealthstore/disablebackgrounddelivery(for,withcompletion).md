# disableBackgroundDelivery(for:withCompletion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Disables background deliveries of update notifications for the specified data type.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
func disableBackgroundDelivery(for type: HKObjectType, withCompletion completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func disableBackgroundDelivery(for type: HKObjectType) async throws
```

```objc
- (void) disableBackgroundDeliveryForType:(HKObjectType *) type withCompletion:(void (^)(BOOL success, NSError *error)) completion;
```

## Discussion

Call this method to prevent your app from receiving any additional update notifications about the specified data type while in the background. This method operates asynchronously. As soon as the background delivery is disabled, this method calls its completion handler on a background queue.

## Parameters

- `type`: The type of data. This object can be any concrete subclass of the [`HKObjectType`](../hkobjecttype.md) class (any of the classes [`HKCharacteristicType`](../hkcharacteristictype.md) , [`HKQuantityType`](../hkquantitytype.md), [`HKCategoryType`](../hkcategorytype.md), [`HKWorkoutType`](../hkworkouttype.md) or [`HKCorrelationType`](../hkcorrelationtype.md)).
- `completion`: A block that this method calls as soon as the background delivery is disabled. This block is passed the following parameters:

  - **success**: A Boolean value. This parameter contains [`true`](../../Swift/true.md) if the background delivery was successfully disabled; otherwise, [`false`](../../Swift/false.md).
  - **error**: An error object. If an error occurred, this object contains information about the error; otherwise, it is set to `nil`.

## See Also

### Related Documentation
- [class HKObserverQuery](../hkobserverquery.md)
  A long-running query that monitors the HealthKit store and updates your app when the HealthKit store saves or deletes a matching sample.
### Managing background delivery
- [func enableBackgroundDelivery(for: HKObjectType, frequency: HKUpdateFrequency, withCompletion: (Bool, (any Error)?) -> Void)](./enablebackgrounddelivery%28for,frequency,withcompletion%29.md)
  Enables the delivery of updates to an app running in the background.
- [com.apple.developer.healthkit.background-delivery](../../BundleResources/entitlements/com.apple.developer.healthkit.background-delivery.md)
  A Boolean value that indicates whether observer queries receive updates while running in the background.
- [enum HKUpdateFrequency](../hkupdatefrequency.md)
  Constants that determine how often the system launches your app in response to changes to HealthKit data.
- [func disableAllBackgroundDelivery(completion: (Bool, (any Error)?) -> Void)](./disableallbackgrounddelivery%28completion%29.md)
  Disables all background deliveries of update notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/disablebackgrounddelivery(for:withcompletion:))*