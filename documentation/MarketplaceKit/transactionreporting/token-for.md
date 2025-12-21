# token(for:)

**Framework**: MarketplaceKit  
**Kind**: method

Returns a token of the specified type.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
static func token(for tokenType: TransactionReporting.TokenType) async throws -> String
```

## Mentions

- [Reporting transactions for the Core Technology Commission](reporting-transactions-for-core-technology-commission.md)

#### Return Value

JSON data in a Base64URL-encoded string.

#### Discussion

When you pass a token type, this method returns a token.

For example, passing the [`coreTechnology`](transactionreporting/tokentype/coretechnology.md) token type, returns a token for reporting a potential purchase related to your app.

> **Note**: A [`MarketplaceKitError`](marketplacekiterror.md), if the app doesn’t meet qualifications for transaction reporting. For example, if the [`current`](appdistributor/current.md) distributor isn’t [`AppDistributor.marketplace(_:)`](appdistributor/marketplace(_:).md) or [`AppDistributor.web`](appdistributor/web.md).

## Parameters

- `tokenType`: The type of token to generate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/transactionreporting/token(for:))*