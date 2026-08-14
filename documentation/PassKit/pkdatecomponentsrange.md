# PKDateComponentsRange

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that specifies the start and end dates for a range of time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class PKDateComponentsRange
```

#### Overview

Create a [`PKDateComponentsRange`](pkdatecomponentsrange.md) with date components that are valid dates and have a calendar. The [`PKDateComponentsRange`](pkdatecomponentsrange.md) class supports time zones in date components, and exact times are optional.

Provide a specific time and time zone in the date components to display a correct pickup time regardless of the user’s current time zone.

## Topics

### Creating a Date Range
- [init?(start: DateComponents, end: DateComponents)](pkdatecomponentsrange/init(start:end:).md)
  Creates a new time range with the start and end dates and times that you specify.
### Reading the Start and End Dates
- [var startDateComponents: DateComponents](pkdatecomponentsrange/startdatecomponents.md)
  The start date and time of the range.
- [var endDateComponents: DateComponents](pkdatecomponentsrange/enddatecomponents.md)
  The end date and time of the range.
### Initializers
- [init?(coder: NSCoder)](pkdatecomponentsrange/init(coder:).md)
- [init?(startDateComponents: DateComponents, endDateComponents: DateComponents)](pkdatecomponentsrange/init(startdatecomponents:enddatecomponents:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [var detail: String?](pkshippingmethod/detail.md)
  A user-readable description of the shipping method.
- [var dateComponentsRange: PKDateComponentsRange?](pkshippingmethod/datecomponentsrange.md)
  An expected range of delivery or shipping dates for a package, or the time range when an item is available for pickup.
- [var identifier: String?](pkshippingmethod/identifier.md)
  A unique identifier for the shipping method, used by the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdatecomponentsrange)*