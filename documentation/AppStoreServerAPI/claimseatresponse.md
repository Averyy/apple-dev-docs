# ClaimSeatResponse

**Framework**: App Store Server API  
**Kind**: dictionary  
**Role**: Object

A response that contains the identifier of a seat claim.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
object ClaimSeatResponse
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

This response contains the `seatClaimId` of the claim you make by calling the [`Claim Seat`](./claim-seat.md) endpoint. This identifier belongs to a claim, not to a seat in the subscription. Every claim generates a new `seatClaimId`, even when you reassign a seat to another member.

Store the `seatClaimId` with your record of the member who occupies the seat. Use it to call the [`Unclaim Seat`](./unclaim-seat.md) and [`Associate Seat`](./associate-seat.md) endpoints.

## Properties

- `seatClaimId` (seatClaimId): The identifier of the seat claim that the request created.

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
- [Unclaim Seat](./unclaim-seat.md)
  Release a claimed seat in a group subscription that uses developer-hosted invitations.
- [Associate Seat](./associate-seat.md)
  Associate a customer with a claimed seat in a group subscription that uses developer-hosted invitations.
- [object AssociateSeatRequest](./associateseatrequest.md)
  The request body that contains the app transaction identifier of the customer who occupies a claimed seat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/claimseatresponse)*