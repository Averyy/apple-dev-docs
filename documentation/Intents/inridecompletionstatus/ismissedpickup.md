# isMissedPickup

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether someone canceled the ride because the user was never picked up.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var isMissedPickup: Bool { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, getter=isMissedPickup) BOOL missedPickup;
```

*macOS*

```objc
@property (atomic, readonly, getter=isMissedPickup) BOOL missedPickup;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when your ride service did not pick up of the user, otherise it is [`false`](../../Swift/false.md). The method you use to create an instance of this class automatically sets the value of this property.

## See Also

### Getting the Status Information
- [var isCompleted: Bool](./iscompleted.md)
  A Boolean value indicating whether the ride completed successfully.
- [var isCanceled: Bool](./iscanceled.md)
  A Boolean value indicating whether someone canceled the ride for any reason.
- [var isOutstanding: Bool](./isoutstanding.md)
  A Boolean indicating whether payment is still outstanding.
- [var paymentAmount: INCurrencyAmount?](./paymentamount.md)
  The amount paid or still outstanding for the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridecompletionstatus/ismissedpickup)*