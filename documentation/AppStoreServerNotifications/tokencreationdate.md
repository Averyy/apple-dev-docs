# tokenCreationDate

**Framework**: App Store Server Notifications  
**Kind**: typealias  
**Role**: Type

The field of an external purchase token that contains the UNIX date, in milliseconds, when the system created the token.

**Availability**:
- App Store Server Notifications 2.10+

## Declaration

```
timestamp tokenCreationDate
```

## Mentions

- [App Store Server Notifications changelog](./app-store-server-notifications-changelog.md)

#### Discussion

This field represents the date when the system created the [`externalPurchaseToken`](./externalpurchasetoken.md).

## See Also

### External purchase token fields
- [type externalPurchaseId](./externalpurchaseid.md)
  The field of an external purchase token that uniquely identifies the token.
- [type tokenExpirationDate](./tokenexpirationdate.md)
  The field of a custom link token that contains the UNIX date, in milliseconds, when the token expires.
- [type tokenType](./tokentype.md)
  The type of an external purchase custom link token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/tokencreationdate)*