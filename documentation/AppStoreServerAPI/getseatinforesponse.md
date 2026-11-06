# GetSeatInfoResponse

**Framework**: App Store Server API  
**Kind**: dictionary  
**Role**: Object

A response that contains the seat counts and the seat claims of a group subscription that uses developer-hosted invitations.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
object GetSeatInfoResponse
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

This response contains information that you request by calling the [`Get Seat Info`](./get-seat-info.md) endpoint.

Each value in the `assignedSeatClaimIds` array is a [`seatClaimId`](./seatclaimid.md) that the [`Claim Seat`](./claim-seat.md) endpoint returned. The array can contain more identifiers than the `totalSeatCount`, if the subscription renews with fewer seats than are claimed.

## Topics

### Seat data types
- [type seatClaimId](./seatclaimid.md)
  The identifier of a seat claim in a group subscription that uses developer-hosted invitations.
- [availableSeatCount](./getseatinforesponse/availableseatcount.md)
- [totalSeatCount](./getseatinforesponse/totalseatcount.md)

## Properties

- `availableSeatCount` (availableSeatCount): The number of seats that are available to claim.
- `totalSeatCount` (totalSeatCount): The total number of seats in the subscription.
- `assignedSeatClaimIds` ([seatClaimId]): An array of the identifiers of the active seat claims.

## See Also

### Seat management
- [Get Seat Info](./get-seat-info.md)
  Get the seat counts and the seat claims of a group subscription that uses developer-hosted invitations.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/getseatinforesponse)*