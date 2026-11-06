# NoAvailableSeatsError

**Framework**: App Store Server API  
**Kind**: dictionary  
**Role**: Object

An error that indicates the subscription has no seats available to claim.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
object NoAvailableSeatsError
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

A request returns this error if you call the [`Claim Seat`](./claim-seat.md) endpoint when every seat in the subscription is claimed.

The number of claimed seats can exceed the number of seats in the subscription after it renews with fewer seats, because the App Store doesn’t unclaim seats when the subscription renews. In that case, call the [`Unclaim Seat`](./unclaim-seat.md) endpoint to release seats until the number of claimed seats is lower than the number of seats in the subscription. To get the seat counts and the claimed seats, call the [`Get Seat Info`](./get-seat-info.md) endpoint.

## Properties

- `errorCode` (int64): **Allowed Values**: `4000251`
- `errorMessage` (string): **Allowed Values**: `Invalid request. No available seats to claim on this subscription.`

## See Also

### Seat management errors
- [object AppTransactionIdNotFoundError](./apptransactionidnotfounderror.md)
  An error that indicates the app transaction identifier wasn’t found.
- [object BundleTransactionIdNotSupportedError](./bundletransactionidnotsupportederror.md)
  An error that indicates the group subscription endpoint doesn’t support the transaction identifier of a bundle.
- [object SeatClaimIdNotFoundError](./seatclaimidnotfounderror.md)
  An error that indicates the seat claim identifier wasn’t found.
- [object SubscriptionNotActiveError](./subscriptionnotactiveerror.md)
  An error that indicates the subscription isn’t active.
- [object TransactionNotDevManagedGroupError](./transactionnotdevmanagedgrouperror.md)
  An error that indicates the transaction isn’t for a subscription that uses developer-hosted invitations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/noavailableseatserror)*