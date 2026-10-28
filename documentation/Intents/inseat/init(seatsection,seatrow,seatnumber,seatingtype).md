# init(seatSection:seatRow:seatNumber:seatingType:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a new seat object containing the required seat information.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(seatSection: String?, seatRow: String?, seatNumber: String?, seatingType: String?)
```

```objc
- (instancetype) initWithSeatSection:(NSString *) seatSection seatRow:(NSString *) seatRow seatNumber:(NSString *) seatNumber seatingType:(NSString *) seatingType;
```

## Discussion

Create a new seat object when the reservation includes a seat assignment, such as for a flight or train reservation.

## Parameters

- `seatSection`: The seat’s section.
- `seatRow`: The seat’s row.
- `seatNumber`: The seat’s number.
- `seatingType`: The seat’s type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inseat/init(seatsection:seatrow:seatnumber:seatingtype:))*