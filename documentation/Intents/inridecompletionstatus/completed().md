# completed()

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an instance of this class that indicates the ride completed successfully.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func completed() -> Self
```

```objc
+ (instancetype) completed;
```

## Return Value

An initialized [`INRideCompletionStatus`](../inridecompletionstatus.md) object.

## Discussion

This method sets the [`isCompleted`](./iscompleted.md) property of the returned object to [`true`](../../Swift/true.md), and it sets the [`isCanceled`](./iscanceled.md), [`isMissedPickup`](./ismissedpickup.md), and [`isOutstanding`](./isoutstanding.md) properties to [`false`](../../Swift/false.md).

## See Also

### Creating a Ride Completion Status Object
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
- [class func canceledMissedPickup() -> Self](./canceledmissedpickup%28%29.md)
  Creates an instance of this class that indicates someone canceled the ride because of a missed pickup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridecompletionstatus/completed())*