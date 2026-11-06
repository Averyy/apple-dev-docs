# Associate Seat

**Framework**: App Store Server API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Associate a customer with a claimed seat in a group subscription that uses developer-hosted invitations.

**Availability**:
- App Store Server API 1.23+

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

> ❗ **Important**:  This endpoint is only available in the sandbox environment.

Call this endpoint only for an active group subscription that uses developer-hosted invitations, where the [`invitationManagement`](./invitationmanagement.md) value in the purchaser’s transaction is `DEVELOPER`. Use it to tell the App Store which customer occupies a seat that you already claimed, when you learn the customer’s [`appTransactionId`](./apptransactionid.md) after the claim. Provide the `appTransactionId` in an [`AssociateSeatRequest`](./associateseatrequest.md).

If you know the customer’s `appTransactionId` when you claim the seat, include it in the [`ClaimSeatRequest`](./claimseatrequest.md) instead; you don’t need to call this endpoint.

Associating a customer with a seat doesn’t grant them access. You’re responsible for providing access to the subscription.

## Endpoint

`POST https://api.storekit-sandbox.apple.com/groups/v1/transactions/{originalTransactionId}/seats/{seatClaimId}/associate`

## Parameters

### Path Parameters

- `originalTransactionId` (originalTransactionId) *(required)*: The original transaction identifier of the group purchaser’s subscription.
- `seatClaimId` (seatClaimId) *(required)*: The identifier of the seat claim, which the [`Claim Seat`](./claim-seat.md) endpoint returns.

## Request Body

**Content-Type**: `application/json`  
**Type**: `AssociateSeatRequest`

The request body that contains the app transaction identifier of the customer who occupies the seat.

## Responses

- `200` OK: Request succeeded.
- `400` Bad Request (`(InvalidTransactionIdError | AppTransactionIdNotSupportedError | FamilyTransactionNotSupportedError | BundleTransactionIdNotSupportedError | TransactionNotDevManagedGroupError)`, `application/json`): Invalid request. See the error code for more information.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](./generating-json-web-tokens-for-api-requests.md).
- `403` Forbidden (`SubscriptionNotActiveError`, `application/json`): The subscription isn’t active.
- `404` Not Found (`(OriginalTransactionIdNotFoundError | AppTransactionIdNotFoundError | SeatClaimIdNotFoundError)`, `application/json`): The original transaction identifier, the app transaction identifier, or the seat claim identifier wasn’t found.
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
- [Unclaim Seat](./unclaim-seat.md)
  Release a claimed seat in a group subscription that uses developer-hosted invitations.
- [object AssociateSeatRequest](./associateseatrequest.md)
  The request body that contains the app transaction identifier of the customer who occupies a claimed seat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/associate-seat)*