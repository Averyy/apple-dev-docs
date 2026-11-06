# AssociateSeatRequest

**Framework**: App Store Server API  
**Kind**: dictionary  
**Role**: Object

The request body that contains the app transaction identifier of the customer who occupies a claimed seat.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
object AssociateSeatRequest
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

This is the request body for the [`Associate Seat`](./associate-seat.md) endpoint.

## Properties

- `appTransactionId` (appTransactionId) *(required)*: **Required**. The app transaction identifier of the customer who occupies the seat.

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
- [Associate Seat](./associate-seat.md)
  Associate a customer with a claimed seat in a group subscription that uses developer-hosted invitations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/associateseatrequest)*