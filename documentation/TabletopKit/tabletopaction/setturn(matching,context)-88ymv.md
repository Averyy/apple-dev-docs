# setTurn(matching:context:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func setTurn(matching seatIDs: [TableSeatIdentifier], context: UInt64 = 0) -> Self
```

Available when `Self` is `SetTurnAction`.

## See Also

### Taking turns
- [static func setTurn(forSeat: some TableSeat, context: UInt64) -> Self](./setturn%28forseat,context%29.md)
- [static func setTurn(forSeats: some Sequence, context: UInt64) -> Self](./setturn%28forseats,context%29-3msxi.md)
- [static func setTurn(forSeats: some Sequence<any TableSeat>, context: UInt64) -> Self](./setturn%28forseats,context%29-4sgng.md)
- [static func setTurn(matching: TableSeatIdentifier, context: UInt64) -> Self](./setturn%28matching,context%29-6mq07.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopaction/setturn(matching:context:)-88ymv)*