# TransactionNotDevManagedGroupError

**Framework**: App Store Server API  
**Kind**: dictionary  
**Role**: Object

An error that indicates the transaction isn’t for a subscription that uses developer-hosted invitations.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
object TransactionNotDevManagedGroupError
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

A request returns this error if you call the [`Get Seat Info`](./get-seat-info.md), [`Claim Seat`](./claim-seat.md), [`Unclaim Seat`](./unclaim-seat.md), or [`Associate Seat`](./associate-seat.md) endpoint with an original transaction identifier for a subscription that doesn’t use developer-hosted invitations. This includes a multiseat subscription with an [`invitationManagement`](./invitationmanagement.md) value of `APPLE`, and a subscription that isn’t a multiseat purchase.

Before you call these endpoints, check that the [`TransactionMultiSeatInfo`](./transactionmultiseatinfo.md) in the latest transaction for the subscription has an `invitationManagement` value of `DEVELOPER`.

## Properties

- `errorCode` (int64): **Allowed Values**: `4000273`
- `errorMessage` (string): **Allowed Values**: `Invalid request. The transaction doesn't represent a developer-managed group subscription.`

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
- [object SubscriptionNotActiveError](./subscriptionnotactiveerror.md)
  An error that indicates the subscription isn’t active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/transactionnotdevmanagedgrouperror)*