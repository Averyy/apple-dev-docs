# DDMatchCalendarEvent

**Framework**: DataDetection  
**Kind**: class

An object that represents a calendar date or date range that the data detection system matches.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class DDMatchCalendarEvent
```

#### Overview

The DataDetection framework returns a calendar event match in a `DDMatchCalendarEvent` object, which has only a beginning date, only an end date, or both a beginning date and an end date.

## Topics

### Getting event details
- [var isAllDay: Bool](ddmatchcalendarevent/isallday.md)
  A Boolean value that indicates whether the event is an all-day event.
- [var endDate: Date?](ddmatchcalendarevent/enddate.md)
  A date that represents the end of the event.
- [var endTimeZone: TimeZone?](ddmatchcalendarevent/endtimezone.md)
  The time zone for the event’s end date.
- [var startDate: Date?](ddmatchcalendarevent/startdate.md)
  A date that represents the start of the event.
- [var startTimeZone: TimeZone?](ddmatchcalendarevent/starttimezone.md)
  The time zone for the event’s start date.

## Relationships

### Inherits From
- [DDMatch](ddmatch.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class DDMatchEmailAddress](ddmatchemailaddress.md)
  An object that contains an email address that the data detection system matches.
- [class DDMatchFlightNumber](ddmatchflightnumber.md)
  An object that contains a flight number that the data detection system matches.
- [class DDMatchLink](ddmatchlink.md)
  An object that contains a web link that the data detection system matches.
- [class DDMatchMoneyAmount](ddmatchmoneyamount.md)
  An object that contains an amount of money that the data detection system matches.
- [class DDMatchPhoneNumber](ddmatchphonenumber.md)
  An object that contains a phone number that the data detection system matches.
- [class DDMatchPostalAddress](ddmatchpostaladdress.md)
  An object that contains a postal address that the data detection system matches.
- [class DDMatchShipmentTrackingNumber](ddmatchshipmenttrackingnumber.md)
  An object that contains parcel tracking information that the data detection system matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/ddmatchcalendarevent)*