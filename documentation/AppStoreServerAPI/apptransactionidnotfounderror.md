# AppTransactionIdNotFoundError

**Framework**: App Store Server API  
**Kind**: dictionary  
**Role**: Object

An error that indicates the app transaction identifier wasn’t found.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
object AppTransactionIdNotFoundError
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

A request returns this error if you call the [`Claim Seat`](./claim-seat.md) or [`Associate Seat`](./associate-seat.md) endpoint with an [`appTransactionId`](./apptransactionid.md) that the App Store can’t find. Check that the value is the customer’s app transaction identifier for your app, in the same environment as the request.

## Properties

- `errorCode` (int64): **Allowed Values**: `4040023`
- `errorMessage` (string): **Allowed Values**: `App transaction id not found.`

## See Also

### Seat management errors
- [object BundleTransactionIdNotSupportedError](./bundletransactionidnotsupportederror.md)
  An error that indicates the group subscription endpoint doesn’t support the transaction identifier of a bundle.
- [object NoAvailableSeatsError](./noavailableseatserror.md)
  An error that indicates the subscription has no seats available to claim.
- [object SeatClaimIdNotFoundError](./seatclaimidnotfounderror.md)
  An error that indicates the seat claim identifier wasn’t found.
- [object SubscriptionNotActiveError](./subscriptionnotactiveerror.md)
  An error that indicates the subscription isn’t active.
- [object TransactionNotDevManagedGroupError](./transactionnotdevmanagedgrouperror.md)
  An error that indicates the transaction isn’t for a subscription that uses developer-hosted invitations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/apptransactionidnotfounderror)*