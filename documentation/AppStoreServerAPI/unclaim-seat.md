# Unclaim Seat

**Framework**: App Store Server API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Release a claimed seat in a group subscription that uses developer-hosted invitations.

**Availability**:
- App Store Server API 1.23+

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

> ❗ **Important**:  This endpoint is only available in the sandbox environment.

Call this endpoint only for an active group subscription that uses developer-hosted invitations, where the [`invitationManagement`](./invitationmanagement.md) value in the purchaser’s transaction is `DEVELOPER`. Unclaim a seat when a member leaves the group or the group purchaser removes them, and revoke that member’s access in your system. If the number of claimed seats is then lower than the [`totalSeatCount`](./totalseatcount.md), a seat becomes available to claim.

When the group purchaser reduces the number of seats, the change takes effect at the next renewal date. Outside of a refund, the number of seats doesn’t go down during a subscription period. The App Store doesn’t unclaim any seats when the subscription renews. If the number of claimed seats exceeds the number of seats in the subscription after it renews, call this endpoint to release the excess seats.

When you receive a `DID_CHANGE_RENEWAL_PREF` notification with a `subtype` of `DECREASE_QUANTITY`, compare its [`renewalQuantity`](./renewalquantity.md) with the number of claimed seats. If more seats are claimed than renew, ask the group purchaser before the renewal date which members to remove, and then unclaim those seats on or after the renewal date.

To get the identifiers of the active seat claims, call the [`Get Seat Info`](./get-seat-info.md) endpoint.

The App Store can unclaim seats in response to a customer event. When it does, you receive an `UNCLAIM_SEATS` notification that identifies the seats. For more information, see [`unclaimInfo`](../AppStoreServerNotifications/unclaiminfo.md).

## Endpoint

`DELETE https://api.storekit-sandbox.apple.com/groups/v1/transactions/{originalTransactionId}/seats/{seatClaimId}`

## Parameters

### Path Parameters

- `originalTransactionId` (originalTransactionId) *(required)*: The original transaction identifier of the group purchaser’s subscription.
- `seatClaimId` (seatClaimId) *(required)*: The identifier of the seat claim, which the [`Claim Seat`](./claim-seat.md) endpoint returns.

## Responses

- `200` OK: Request succeeded.
- `400` Bad Request (`(InvalidTransactionIdError | AppTransactionIdNotSupportedError | FamilyTransactionNotSupportedError | BundleTransactionIdNotSupportedError | TransactionNotDevManagedGroupError)`, `application/json`): Invalid request. See the error code for more information.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](./generating-json-web-tokens-for-api-requests.md).
- `403` Forbidden (`SubscriptionNotActiveError`, `application/json`): The subscription isn’t active.
- `404` Not Found (`(OriginalTransactionIdNotFoundError | SeatClaimIdNotFoundError)`, `application/json`): The original transaction identifier or the seat claim identifier wasn’t found.
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit.
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`): Server error. Try again later.

## See Also

### Seat management
- [Get Seat Info](./get-seat-info.md)
  Get the seat counts and the seat claims of a group subscription that uses developer-hosted invitations.
- [object GetSeatInfoResponse](./getseatinforesponse.md)
  A response that contains the seat counts and the seat claims of a group subscription that uses developer-hosted invitations.
- [Claim Seat](./claim-seat.md)
  Claim a seat for a customer in a group subscription that uses developer-hosted invitations.
- [object ClaimSeatRequest](./claimseatrequest.md)
  The request body that contains the information to claim a seat in a group subscription that uses developer-hosted invitations.
- [object ClaimSeatResponse](./claimseatresponse.md)
  A response that contains the identifier of a seat claim.
- [Associate Seat](./associate-seat.md)
  Associate a customer with a claimed seat in a group subscription that uses developer-hosted invitations.
- [object AssociateSeatRequest](./associateseatrequest.md)
  The request body that contains the app transaction identifier of the customer who occupies a claimed seat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/unclaim-seat)*