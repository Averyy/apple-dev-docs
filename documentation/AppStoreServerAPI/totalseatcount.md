# totalSeatCount

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

The total number of seats in a group subscription that uses developer-hosted invitations.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
int32 totalSeatCount
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

The [`Get Seat Info`](./get-seat-info.md) endpoint returns this value in the [`GetSeatInfoResponse`](./getseatinforesponse.md).

## See Also

### Seat management
- [type seatClaimId](./seatclaimid.md)
  The identifier of a seat claim in a group subscription that uses developer-hosted invitations.
- [type availableSeatCount](./availableseatcount.md)
  The number of seats that are available to claim in a group subscription that uses developer-hosted invitations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/totalseatcount)*