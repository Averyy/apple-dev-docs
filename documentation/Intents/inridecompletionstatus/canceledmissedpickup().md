# canceledMissedPickup()

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an instance of this class that indicates someone canceled the ride because of a missed pickup.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func canceledMissedPickup() -> Self
```

```objc
+ (instancetype) canceledMissedPickup;
```

## Return Value

An initialized [`INRideCompletionStatus`](../inridecompletionstatus.md) object.

## Discussion

Use this method when a missed pickup caused the cancellation of the ride. This method sets the [`isCanceled`](./iscanceled.md) and [`isMissedPickup`](./ismissedpickup.md) properties of the returned object to [`true`](../../Swift/true.md), and it sets the [`isCompleted`](./iscompleted.md) and [`isOutstanding`](./isoutstanding.md) properties to [`false`](../../Swift/false.md).

## See Also

### Creating a Ride Completion Status Object
- [class func completed() -> Self](./completed%28%29.md)
  Creates an instance of this class that indicates the ride completed successfully.
- [class func completed(settled: INCurrencyAmount) -> Self](./completed%28settled%29.md)
  Creates an instance of this class that indicates the ride completed successfully and with the specified cost.
- [class func completed(outstanding: INCurrencyAmount) -> Self](./completed%28outstanding%29.md)
  Creates an instance of this class that indicates the ride completed successfully but still requires payment from the user.
- [class func completed(feedbackType: INRideFeedbackTypeOptions) -> Self](./completed%28feedbacktype%29.md)
  Creates an instance of this class that indicates the ride completed successfully but still requires feedback from the user.
- [class func canceledByService() -> Self](./canceledbyservice%28%29.md)
  Creates an instance of this class that indicates your service canceled the ride.
- [class func canceledByUser() -> Self](./canceledbyuser%28%29.md)
  Creates an instance of this class that indicates the user canceled the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridecompletionstatus/canceledmissedpickup())*