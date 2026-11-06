# Get Seat Info

**Framework**: App Store Server API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the seat counts and the seat claims of a group subscription that uses developer-hosted invitations.

**Availability**:
- App Store Server API 1.23+

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

> ❗ **Important**:  This endpoint is only available in the sandbox environment.

Call this endpoint only for an active group subscription that uses developer-hosted invitations, where the [`invitationManagement`](./invitationmanagement.md) value in the purchaser’s transaction is `DEVELOPER`. Your app hosts the invitations to these subscriptions, and you claim a seat for each member by calling the [`Claim Seat`](./claim-seat.md) endpoint.

The response, [`GetSeatInfoResponse`](./getseatinforesponse.md), contains:

- The total number of seats in the subscription, [`totalSeatCount`](./totalseatcount.md).
- The number of seats that are available to claim, [`availableSeatCount`](./availableseatcount.md).
- The identifiers of the active seat claims, in the `assignedSeatClaimIds` array.

The first seat always belongs to the group purchaser, so it’s never available to claim.

Use this endpoint to show the number of available seats in your invitation experience, and to recover the [`seatClaimId`](./seatclaimid.md) of a claimed seat if your records don’t contain it.

If the group purchaser reduces the number of seats, the App Store doesn’t unclaim any seats when the subscription renews. As a result, the number of claimed seats can be greater than `totalSeatCount`. To release seats, call the [`Unclaim Seat`](./unclaim-seat.md) endpoint, which describes how to handle a smaller group at renewal.

## Endpoint

`GET https://api.storekit-sandbox.apple.com/groups/v1/transactions/{originalTransactionId}/seats`

## Parameters

### Path Parameters

- `originalTransactionId` (originalTransactionId) *(required)*: The original transaction identifier of the group purchaser’s subscription.

## Responses

- `200` OK (`GetSeatInfoResponse`, `application/json`): Request succeeded.
- `400` Bad Request (`(InvalidTransactionIdError | AppTransactionIdNotSupportedError | FamilyTransactionNotSupportedError | BundleTransactionIdNotSupportedError | TransactionNotDevManagedGroupError)`, `application/json`): Invalid request. See the error code for more information.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](./generating-json-web-tokens-for-api-requests.md).
- `403` Forbidden (`SubscriptionNotActiveError`, `application/json`): The subscription isn’t active.
- `404` Not Found (`OriginalTransactionIdNotFoundError`, `application/json`): The original transaction identifier wasn’t found.
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit.
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`): Server error. Try again later.

## See Also

### Seat management
- [object GetSeatInfoResponse](./getseatinforesponse.md)
  A response that contains the seat counts and the seat claims of a group subscription that uses developer-hosted invitations.
- [Claim Seat](./claim-seat.md)
  Claim a seat for a customer in a group subscription that uses developer-hosted invitations.
- [object ClaimSeatRequest](./claimseatrequest.md)
  The request body that contains the information to claim a seat in a group subscription that uses developer-hosted invitations.
- [object ClaimSeatResponse](./claimseatresponse.md)
  A response that contains the identifier of a seat claim.
- [Unclaim Seat](./unclaim-seat.md)
  Release a claimed seat in a group subscription that uses developer-hosted invitations.
- [Associate Seat](./associate-seat.md)
  Associate a customer with a claimed seat in a group subscription that uses developer-hosted invitations.
- [object AssociateSeatRequest](./associateseatrequest.md)
  The request body that contains the app transaction identifier of the customer who occupies a claimed seat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/get-seat-info)*