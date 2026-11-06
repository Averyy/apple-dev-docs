# SubscriptionNotActiveError

**Framework**: App Store Server API  
**Kind**: dictionary  
**Role**: Object

An error that indicates the subscription isn’t active.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
object SubscriptionNotActiveError
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

A request returns this error if you call the [`Get Seat Info`](./get-seat-info.md), [`Claim Seat`](./claim-seat.md), [`Unclaim Seat`](./unclaim-seat.md), or [`Associate Seat`](./associate-seat.md) endpoint for a subscription that isn’t active.

## Properties

- `errorCode` (int64): **Allowed Values**: `4030039`
- `errorMessage` (string): **Allowed Values**: `The subscription must be active for the requested operation.`

## See Also

### Seat management errors
- [object AppTransactionIdNotFoundError](./apptransactionidnotfounderror.md)
  An error that indicates the app transaction identifier wasn’t found.
- [object BundleTransactionIdNotSupportedError](./bundletransactionidnotsupportederror.md)
  An error that indicates the group subscription endpoint doesn’t support the transaction identifier of a bundle.
- [object NoAvailableSeatsError](./noavailableseatserror.md)
  An error that indicates the subscription has no seats available to claim.
- [object SeatClaimIdNotFoundError](./seatclaimidnotfounderror.md)
  An error that indicates the seat claim identifier wasn’t found.
- [object TransactionNotDevManagedGroupError](./transactionnotdevmanagedgrouperror.md)
  An error that indicates the transaction isn’t for a subscription that uses developer-hosted invitations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/subscriptionnotactiveerror)*