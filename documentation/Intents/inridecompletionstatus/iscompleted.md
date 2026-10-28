# isCompleted

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the ride completed successfully.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var isCompleted: Bool { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, getter=isCompleted) BOOL completed;
```

*macOS*

```objc
@property (atomic, readonly, getter=isCompleted) BOOL completed;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when your service completed the ride successfully, otherwise it is [`false`](../../Swift/false.md). The method you use to create an instance of this class automatically sets the value of this property.

## See Also

### Getting the Status Information
- [var isCanceled: Bool](./iscanceled.md)
  A Boolean value indicating whether someone canceled the ride for any reason.
- [var isMissedPickup: Bool](./ismissedpickup.md)
  A Boolean value indicating whether someone canceled the ride because the user was never picked up.
- [var isOutstanding: Bool](./isoutstanding.md)
  A Boolean indicating whether payment is still outstanding.
- [var paymentAmount: INCurrencyAmount?](./paymentamount.md)
  The amount paid or still outstanding for the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridecompletionstatus/iscompleted)*