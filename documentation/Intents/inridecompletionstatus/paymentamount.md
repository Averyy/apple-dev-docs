# paymentAmount

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The amount paid or still outstanding for the ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var paymentAmount: INCurrencyAmount? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nullable) INCurrencyAmount * paymentAmount;
```

*macOS*

```objc
@property (atomic, strong, readonly, nullable) INCurrencyAmount * paymentAmount;
```

#### Discussion

When you use the [`completed(settled:)`](./completed%28settled%29.md) method to create instances of this class, this property stores the final amount paid by the user for the ride. When you use the [`completed(outstanding:)`](./completed%28outstanding%29.md) method to create instances of this class, this property stores any unpaid costs that your app and must settle.

Use the [`isOutstanding`](./isoutstanding.md) property to determine if the user still needs to pay the amount in this property.

## See Also

### Getting the Status Information
- [var isCompleted: Bool](./iscompleted.md)
  A Boolean value indicating whether the ride completed successfully.
- [var isCanceled: Bool](./iscanceled.md)
  A Boolean value indicating whether someone canceled the ride for any reason.
- [var isMissedPickup: Bool](./ismissedpickup.md)
  A Boolean value indicating whether someone canceled the ride because the user was never picked up.
- [var isOutstanding: Bool](./isoutstanding.md)
  A Boolean indicating whether payment is still outstanding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridecompletionstatus/paymentamount)*