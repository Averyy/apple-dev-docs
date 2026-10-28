# INBalanceAmount

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A balance associated with an account.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class INBalanceAmount
```

```objc
@interface INBalanceAmount : NSObject
```

## Overview

A balance reflects any credit or debit associated with the account. Balances may reflect an amount of money, frequent flier miles, or points accumulated toward rewards.

## Topics

### Initializing a Balance Amount Object
- [init(amount: NSDecimalNumber, currencyCode: String)](./inbalanceamount/init%28amount,currencycode%29.md)
  Initializes a balance amount with a monetary amount.
- [init?(amount: NSDecimalNumber, balanceType: INBalanceType)](./inbalanceamount/init%28amount,balancetype%29.md)
  Initializes a balance amount object with a customizable type of information.
### Getting the Balance Information
- [var amount: NSDecimalNumber?](./inbalanceamount/amount.md)
  The numerical amount associated with the balance.
- [var currencyCode: String?](./inbalanceamount/currencycode.md)
  The ISO 4217 currency code that applies to a monetary amount.
- [var balanceType: INBalanceType](./inbalanceamount/balancetype.md)
  The type associated with the balance.
- [enum INBalanceType](./inbalancetype.md)
  Constants indicating the meaning of a balance.
### Initializers
- [init?(coder: NSCoder)](./inbalanceamount/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Getting the Account Balance
- [var balance: INBalanceAmount?](./inpaymentaccount/balance.md)
  The primary balance associated with the account.
- [var secondaryBalance: INBalanceAmount?](./inpaymentaccount/secondarybalance.md)
  A secondary balance, if any, associated with the account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbalanceamount)*