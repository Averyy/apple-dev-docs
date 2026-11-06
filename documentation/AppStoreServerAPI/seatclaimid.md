# seatClaimId

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

The identifier of a seat claim in a group subscription that uses developer-hosted invitations.

**Availability**:
- App Store Server API 1.23+

## Declaration

```
uuid seatClaimId
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Discussion

The [`Claim Seat`](./claim-seat.md) endpoint returns this UUID when you claim a seat. Store it with your record of the member who occupies the seat, and use it to call the [`Unclaim Seat`](./unclaim-seat.md) and [`Associate Seat`](./associate-seat.md) endpoints. This identifier belongs to a claim, not to a seat in the subscription. Every claim generates a new `seatClaimId`, even when you reassign a seat to another member.

To get the identifiers of the active seat claims in a subscription, call the [`Get Seat Info`](./get-seat-info.md) endpoint. When the App Store unclaims seats, the `UNCLAIM_SEATS` notification identifies them by this value. For more information, see [`unclaimSeatIds`](../AppStoreServerNotifications/unclaimseatids.md).

## See Also

### Seat data types
- [availableSeatCount](./getseatinforesponse/availableseatcount.md)
- [totalSeatCount](./getseatinforesponse/totalseatcount.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/seatclaimid)*