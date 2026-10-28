# tokenType

**Framework**: App Store Server Notifications  
**Kind**: typealias  
**Role**: Type

The type of an external purchase custom link token.

**Availability**:
- App Store Server Notifications 2.17+

## Declaration

```
string tokenType
```

## Possible Values

- `ACQUISITION`: A token type that indicates an initial acquisition.
- `SERVICES`: A token type that indicates usage of App Store services.
- `CORE_TECHNOLOGY`: A token type an app receives from the MarketplaceKit  [`token(for:)`](../MarketplaceKit/transactionreporting/token%28for%29.md) API.

## Mentions

- [App Store Server Notifications changelog](./app-store-server-notifications-changelog.md)

### Discussion

The token type field is present only for custom link tokens. For more information on tokens, see [Receiving and decoding external purchase tokens](../StoreKit/receiving-and-decoding-external-purchase-tokens.md).

## See Also

### External purchase token fields
- [type externalPurchaseId](./externalpurchaseid.md)
  The field of an external purchase token that uniquely identifies the token.
- [type tokenCreationDate](./tokencreationdate.md)
  The field of an external purchase token that contains the UNIX date, in milliseconds, when the system created the token.
- [type tokenExpirationDate](./tokenexpirationdate.md)
  The field of a custom link token that contains the UNIX date, in milliseconds, when the token expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/tokentype)*