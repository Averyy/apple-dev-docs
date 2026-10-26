# secondaryBalance

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A secondary balance, if any, associated with the account.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
@NSCopying
var secondaryBalance: INBalanceAmount? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INBalanceAmount * secondaryBalance;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INBalanceAmount * secondaryBalance;
```

#### Discussion

A secondary balance might represent something other than a monetary debit or credit. For example, it might represent reward points or frequent flier miles.

## See Also

### Getting the Account Balance
- [var balance: INBalanceAmount?](./balance.md)
  The primary balance associated with the account.
- [class INBalanceAmount](../inbalanceamount.md)
  A balance associated with an account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentaccount/secondarybalance)*