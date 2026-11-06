# BundleTransactionIdNotSupportedError

**Framework**: App Store Server API  
**Kind**: dictionary  
**Role**: Object

An error that indicates the group subscription endpoint doesn’t support the transaction identifier of a bundle.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
object BundleTransactionIdNotSupportedError
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

A request returns this error if you call the [`Get Seat Info`](./get-seat-info.md), [`Claim Seat`](./claim-seat.md), [`Unclaim Seat`](./unclaim-seat.md), or [`Associate Seat`](./associate-seat.md) endpoint with the transaction identifier of a bundle.

## Properties

- `errorCode` (int64): **Allowed Values**: `4000241`
- `errorMessage` (string): **Allowed Values**: `Invalid request. Bundle transaction ids aren't supported by this endpoint.`

## See Also

### Seat management errors
- [object AppTransactionIdNotFoundError](./apptransactionidnotfounderror.md)
  An error that indicates the app transaction identifier wasn’t found.
- [object NoAvailableSeatsError](./noavailableseatserror.md)
  An error that indicates the subscription has no seats available to claim.
- [object SeatClaimIdNotFoundError](./seatclaimidnotfounderror.md)
  An error that indicates the seat claim identifier wasn’t found.
- [object SubscriptionNotActiveError](./subscriptionnotactiveerror.md)
  An error that indicates the subscription isn’t active.
- [object TransactionNotDevManagedGroupError](./transactionnotdevmanagedgrouperror.md)
  An error that indicates the transaction isn’t for a subscription that uses developer-hosted invitations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/bundletransactionidnotsupportederror)*