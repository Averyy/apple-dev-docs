# ClaimSeatRequest

**Framework**: App Store Server API  
**Kind**: dictionary  
**Role**: Object

The request body that contains the information to claim a seat in a group subscription that uses developer-hosted invitations.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
object ClaimSeatRequest
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

This is the request body for the [`Claim Seat`](./claim-seat.md) endpoint.

Generate a new [`requestIdentifier`](./claimseatrequest/requestidentifier.md) for each claim, and save it before you call the endpoint. If the request fails or times out, retry it with the same `requestIdentifier`. If the original request claimed a seat, the endpoint returns that [`seatClaimId`](./seatclaimid.md) instead of claiming a second seat.

If you include the [`appTransactionId`](./claimseatrequest/apptransactionid.md), the App Store associates the customer with the seat as part of the claim. If you learn the `appTransactionId` later, call the [`Associate Seat`](./associate-seat.md) endpoint.

## Properties

- `requestIdentifier` (requestIdentifier) *(required)*: **Required**. A unique identifier you generate for the claim, which makes the request safe to repeat.

  **Maximum Length**: `128`
- `appTransactionId` (appTransactionId): The app transaction identifier of the customer who occupies the seat. Include this value if you know it when you claim the seat.

## See Also

### Seat management
- [Get Seat Info](./get-seat-info.md)
  Get the seat counts and the seat claims of a group subscription that uses developer-hosted invitations.
- [object GetSeatInfoResponse](./getseatinforesponse.md)
  A response that contains the seat counts and the seat claims of a group subscription that uses developer-hosted invitations.
- [Claim Seat](./claim-seat.md)
  Claim a seat for a customer in a group subscription that uses developer-hosted invitations.
- [object ClaimSeatResponse](./claimseatresponse.md)
  A response that contains the identifier of a seat claim.
- [Unclaim Seat](./unclaim-seat.md)
  Release a claimed seat in a group subscription that uses developer-hosted invitations.
- [Associate Seat](./associate-seat.md)
  Associate a customer with a claimed seat in a group subscription that uses developer-hosted invitations.
- [object AssociateSeatRequest](./associateseatrequest.md)
  The request body that contains the app transaction identifier of the customer who occupies a claimed seat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/claimseatrequest)*