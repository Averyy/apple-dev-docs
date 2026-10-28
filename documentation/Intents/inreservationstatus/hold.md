# INReservationStatus.hold

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The reservation is on hold.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case hold
```

```c
INReservationStatusHold
```

## Discussion

Use this status when the app is reserving the reservation time for the user, but the user hasn’t made the reservation.

## See Also

### Reservation Status
- [INReservationStatus.unknown](./unknown.md)
  The current reservation is unknown.
- [INReservationStatus.canceled](./canceled.md)
  The user or business canceled the reservation.
- [INReservationStatus.pending](./pending.md)
  The reservation confirmation is pending.
- [INReservationStatus.confirmed](./confirmed.md)
  The reservation is confirmed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inreservationstatus/hold)*