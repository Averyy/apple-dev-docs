# availableSeatCount

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

The number of seats that are available to claim in a group subscription that uses developer-hosted invitations.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
int32 availableSeatCount
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

The [`Get Seat Info`](./get-seat-info.md) endpoint returns this value in the [`GetSeatInfoResponse`](./getseatinforesponse.md). If no seats are available, the [`Claim Seat`](./claim-seat.md) endpoint returns a [`NoAvailableSeatsError`](./noavailableseatserror.md).

## See Also

### Seat management
- [type seatClaimId](./seatclaimid.md)
  The identifier of a seat claim in a group subscription that uses developer-hosted invitations.
- [type totalSeatCount](./totalseatcount.md)
  The total number of seats in a group subscription that uses developer-hosted invitations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/availableseatcount)*