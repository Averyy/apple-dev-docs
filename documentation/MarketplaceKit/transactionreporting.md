# TransactionReporting

**Framework**: MarketplaceKit  
**Kind**: enum

An enumeration that provides token services for transaction reporting.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
enum TransactionReporting
```

## Mentions

- [Creating an alternative app marketplace](creating-an-alternative-app-marketplace.md)
- [Distributing your app on an alternative app marketplace](distributing-your-app-on-an-alternative-marketplace.md)
- [Reporting transactions for the Core Technology Commission](reporting-transactions-for-core-technology-commission.md)

#### Overview

Track any eligible purchases, related to your app, that you offer a person and report them to Apple using tokens provided by this enumeration. For more information, see [`Reporting transactions for the Core Technology Commission`](reporting-transactions-for-core-technology-commission.md).

## Topics

### Retrieving a token
- [static func token(for: TransactionReporting.TokenType) async throws -> String](transactionreporting/token(for:).md)
  Returns a token of the specified type.
### Specifying the token type
- [TransactionReporting.TokenType](transactionreporting/tokentype.md)
  The type of transaction reporting token.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Reporting transactions for the Core Technology Commission](reporting-transactions-for-core-technology-commission.md)
  Track any eligible purchases that you offer a person that relate to your app and report them to Apple using a token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/transactionreporting)*