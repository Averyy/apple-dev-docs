# completed(outstanding:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an instance of this class that indicates the ride completed successfully but still requires payment from the user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func completed(outstanding outstandingPaymentAmount: INCurrencyAmount) -> Self
```

```objc
+ (instancetype) completedWithOutstandingPaymentAmount:(INCurrencyAmount *) outstandingPaymentAmount;
```

## Return Value

An initialized [`INRideCompletionStatus`](../inridecompletionstatus.md) object.

## Discussion

Use this method when the ride completed successfully but the user has not yet provided full payment. This method sets the [`isCompleted`](./iscompleted.md) and [`isOutstanding`](./isoutstanding.md) properties of the returned object to [`true`](../../Swift/true.md), and it sets the [`isCanceled`](./iscanceled.md) and [`isMissedPickup`](./ismissedpickup.md) properties to [`false`](../../Swift/false.md). It also sets the [`paymentAmount`](./paymentamount.md) property to the value in the `outstandingPaymentAmount` parameter. Your app can use that amount later to handle the payment.

After creating the object, assign a value to the object’s [`completionUserActivity`](./completionuseractivity.md) property. Your user activity object should indicate that payment is still required in your app. Providing the user activity object lets SiriKit know that it should notify the user that your app needs to take additional steps.

## Parameters

- `outstandingPaymentAmount`: The amount of money owed by the user for the ride.

## See Also

### Creating a Ride Completion Status Object
- [class func completed() -> Self](./completed%28%29.md)
  Creates an instance of this class that indicates the ride completed successfully.
- [class func completed(settled: INCurrencyAmount) -> Self](./completed%28settled%29.md)
  Creates an instance of this class that indicates the ride completed successfully and with the specified cost.
- [class func completed(feedbackType: INRideFeedbackTypeOptions) -> Self](./completed%28feedbacktype%29.md)
  Creates an instance of this class that indicates the ride completed successfully but still requires feedback from the user.
- [class func canceledByService() -> Self](./canceledbyservice%28%29.md)
  Creates an instance of this class that indicates your service canceled the ride.
- [class func canceledByUser() -> Self](./canceledbyuser%28%29.md)
  Creates an instance of this class that indicates the user canceled the ride.
- [class func canceledMissedPickup() -> Self](./canceledmissedpickup%28%29.md)
  Creates an instance of this class that indicates someone canceled the ride because of a missed pickup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridecompletionstatus/completed(outstanding:))*