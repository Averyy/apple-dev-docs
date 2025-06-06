# DDMatchEmailAddress

**Framework**: DataDetection  
**Kind**: class

An object that contains an email address that the data detection system matches.

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
class DDMatchEmailAddress
```

#### Overview

The DataDetection framework returns an email match in a `DDMatchEmailAddress` object, which includes an email address, and optionally a label that categorizes the email address.

## Topics

### Getting email information
- [var emailAddress: String](ddmatchemailaddress/emailaddress.md)
  A string that represents an email address.
- [var label: String?](ddmatchemailaddress/label.md)
  A string that categorizes an email address, such as Home or Work.

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

- [class DDMatchCalendarEvent](ddmatchcalendarevent.md)
  An object that represents a calendar date or date range that the data detection system matches.
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

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/ddmatchemailaddress)*