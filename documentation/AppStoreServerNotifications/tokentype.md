# tokenType

**Framework**: App Store Server Notifications  
**Kind**: typealias

The type of an external purchase custom link token.

**Availability**:
- App Store Server Notifications 2.17+

## Declaration

```swift
string tokenType
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)

##### Discussion

The token type field is present only for custom link tokens. For more information on tokens, see [`Receiving and decoding external purchase tokens`](https://developer.apple.com/documentation/StoreKit/receiving-and-decoding-external-purchase-tokens).

## See Also

- [type externalPurchaseId](externalpurchaseid.md)
  The field of an external purchase token that uniquely identifies the token.
- [type tokenCreationDate](tokencreationdate.md)
  The field of an external purchase token that contains the UNIX date, in milliseconds, when the system created the token.
- [type tokenExpirationDate](tokenexpirationdate.md)
  The field of a custom link token that contains the UNIX date, in milliseconds, when the token expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/tokentype)*