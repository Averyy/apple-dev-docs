# Claim Seat

**Framework**: App Store Server API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Claim a seat for a customer in a group subscription that uses developer-hosted invitations.

**Availability**:
- App Store Server API 1.23+

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

> ❗ **Important**:  This endpoint is only available in the sandbox environment.

Call this endpoint only for an active group subscription that uses developer-hosted invitations, where the [`invitationManagement`](./invitationmanagement.md) value in the purchaser’s transaction is `DEVELOPER`. Members of these groups don’t receive transactions, so your server keeps the record of who has access. Claim a seat for each member other than the purchaser to tell the App Store that the seat is occupied.

When a customer accepts an invitation to join a group in your app, call this endpoint with a [`ClaimSeatRequest`](./claimseatrequest.md). The response, [`ClaimSeatResponse`](./claimseatresponse.md), contains a [`seatClaimId`](./seatclaimid.md) that identifies the seat claim. Store the `seatClaimId` with your record of the member. You need it to unclaim or associate the seat, and the App Store uses it to identify seats that it unclaims.

### Make claims safe to repeat

The `requestIdentifier` in the request makes the claim safe to repeat. Generate a new `requestIdentifier` for each claim, and save it before you call this endpoint. If a request fails or times out, call the endpoint again with the same `requestIdentifier`. If the original request claimed a seat, the App Store returns that `seatClaimId`, rather than claiming another seat. A request with a new `requestIdentifier` claims a new seat.

### Associate the customer with the seat

If you know the [`appTransactionId`](./apptransactionid.md) of the customer who occupies the seat when you claim it, include it in the request. The App Store associates the customer with the seat as part of the claim. If you learn the `appTransactionId` after you claim the seat, call the [`Associate Seat`](./associate-seat.md) endpoint instead.

### Claim seats only when seats are available

You can claim a seat only when the subscription has a seat available. If it doesn’t, the endpoint returns a [`NoAvailableSeatsError`](./noavailableseatserror.md). To get the number of available seats, call the [`Get Seat Info`](./get-seat-info.md) endpoint.

If the group purchaser reduces the number of seats, the App Store doesn’t unclaim any seats when the subscription renews, so the number of claimed seats can exceed the number of seats in the subscription. Call the [`Unclaim Seat`](./unclaim-seat.md) endpoint to release seats until the number of claimed seats is lower than the number of seats in the subscription, and then claim new seats.

## Endpoint

`POST https://api.storekit-sandbox.apple.com/groups/v1/transactions/{originalTransactionId}/seats`

## Parameters

### Path Parameters

- `originalTransactionId` (originalTransactionId) *(required)*: The original transaction identifier of the group purchaser’s subscription.

## Request Body

**Content-Type**: `application/json`  
**Type**: `ClaimSeatRequest`

The request body that contains a request identifier, and optionally, the app transaction identifier of the customer who occupies the seat.

## Responses

- `200` OK (`ClaimSeatResponse`, `application/json`): Request succeeded.
- `400` Bad Request (`(InvalidTransactionIdError | InvalidRequestIdentifierError | AppTransactionIdNotSupportedError | FamilyTransactionNotSupportedError | BundleTransactionIdNotSupportedError | NoAvailableSeatsError | TransactionNotDevManagedGroupError)`, `application/json`): Invalid request. See the error code for more information.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](./generating-json-web-tokens-for-api-requests.md).
- `403` Forbidden (`SubscriptionNotActiveError`, `application/json`): The subscription isn’t active.
- `404` Not Found (`(OriginalTransactionIdNotFoundError | AppTransactionIdNotFoundError)`, `application/json`): The original transaction identifier or the app transaction identifier wasn’t found.
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit.
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`): Server error. Try again later.

## See Also

### Seat management
- [Get Seat Info](./get-seat-info.md)
  Get the seat counts and the seat claims of a group subscription that uses developer-hosted invitations.
- [object GetSeatInfoResponse](./getseatinforesponse.md)
  A response that contains the seat counts and the seat claims of a group subscription that uses developer-hosted invitations.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/claim-seat)*