# isCanceled

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether someone canceled the ride for any reason.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var isCanceled: Bool { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, getter=isCanceled) BOOL canceled;
```

*macOS*

```objc
@property (atomic, readonly, getter=isCanceled) BOOL canceled;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when someone canceled the ride. It is [`false`](../../Swift/false.md) when the user was successfully picked up. The method you use to create an instance of this class automatically sets the value of this property.

## See Also

### Getting the Status Information
- [var isCompleted: Bool](./iscompleted.md)
  A Boolean value indicating whether the ride completed successfully.
- [var isMissedPickup: Bool](./ismissedpickup.md)
  A Boolean value indicating whether someone canceled the ride because the user was never picked up.
- [var isOutstanding: Bool](./isoutstanding.md)
  A Boolean indicating whether payment is still outstanding.
- [var paymentAmount: INCurrencyAmount?](./paymentamount.md)
  The amount paid or still outstanding for the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridecompletionstatus/iscanceled)*