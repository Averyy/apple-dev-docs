# balance

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The primary balance associated with the account.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
@NSCopying
var balance: INBalanceAmount? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INBalanceAmount * balance;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INBalanceAmount * balance;
```

## See Also

### Getting the Account Balance
- [var secondaryBalance: INBalanceAmount?](./secondarybalance.md)
  A secondary balance, if any, associated with the account.
- [class INBalanceAmount](../inbalanceamount.md)
  A balance associated with an account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentaccount/balance)*