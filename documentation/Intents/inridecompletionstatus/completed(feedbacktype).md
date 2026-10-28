# completed(feedbackType:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an instance of this class that indicates the ride completed successfully but still requires feedback from the user.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func completed(feedbackType: INRideFeedbackTypeOptions = []) -> Self
```

```objc
+ (instancetype) completedWithOutstandingFeedbackType:(INRideFeedbackTypeOptions) feedbackType;
```

## Return Value

An initialized [`INRideCompletionStatus`](../inridecompletionstatus.md) object.

## Discussion

Use this method when the ride completed successfully and you want the user to provide a tip or feedback about the ride. This method sets the `isCompleted` and [`isOutstanding`](./isoutstanding.md) properties of the returned object to [`true`](../../Swift/true.md), and it sets the [`isCanceled`](./iscanceled.md) and [`isMissedPickup`](./ismissedpickup.md) properties to [`false`](../../Swift/false.md). If you ask the user to specify a tip, assign values to the [`defaultTippingOptions`](./defaulttippingoptions.md) property representing proposed tip amounts.

If your Intents extension supports the [`INSendRideFeedbackIntent`](../insendridefeedbackintent.md), SiriKit delivers that intent when feedback from the last ride is still needed. If you don’t support the intent, you can still assign a value to the [`completionUserActivity`](./completionuseractivity.md) property to allow the collection of feedback from your app.

## Parameters

- `feedbackType`: The type of feedback you want from the user. You can ask the user to provide feedback on the driver, leave a tip, or both.

## See Also

### Creating a Ride Completion Status Object
- [class func completed() -> Self](./completed%28%29.md)
  Creates an instance of this class that indicates the ride completed successfully.
- [class func completed(settled: INCurrencyAmount) -> Self](./completed%28settled%29.md)
  Creates an instance of this class that indicates the ride completed successfully and with the specified cost.
- [class func completed(outstanding: INCurrencyAmount) -> Self](./completed%28outstanding%29.md)
  Creates an instance of this class that indicates the ride completed successfully but still requires payment from the user.
- [class func canceledByService() -> Self](./canceledbyservice%28%29.md)
  Creates an instance of this class that indicates your service canceled the ride.
- [class func canceledByUser() -> Self](./canceledbyuser%28%29.md)
  Creates an instance of this class that indicates the user canceled the ride.
- [class func canceledMissedPickup() -> Self](./canceledmissedpickup%28%29.md)
  Creates an instance of this class that indicates someone canceled the ride because of a missed pickup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridecompletionstatus/completed(feedbacktype:))*