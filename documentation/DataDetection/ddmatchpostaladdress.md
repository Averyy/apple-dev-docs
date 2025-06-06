# DDMatchPostalAddress

**Framework**: DataDetection  
**Kind**: class

An object that contains a postal address that the data detection system matches.

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
class DDMatchPostalAddress
```

#### Overview

The DataDetection framework returns a postal address match in a `DDMatchPostalAddress` object, which optionally contains the matching parts of a postal address: street, city, state, postal code, and country.

## Topics

### Getting postal address information
- [var street: String?](ddmatchpostaladdress/street.md)
  The street name in a postal address.
- [var city: String?](ddmatchpostaladdress/city.md)
  The city name in a postal address.
- [var state: String?](ddmatchpostaladdress/state.md)
  The state name in a postal address.
- [var postalCode: String?](ddmatchpostaladdress/postalcode.md)
  The postal code in a postal address.
- [var country: String?](ddmatchpostaladdress/country.md)
  The country or region name in a postal address.

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
- [class DDMatchShipmentTrackingNumber](ddmatchshipmenttrackingnumber.md)
  An object that contains parcel tracking information that the data detection system matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/ddmatchpostaladdress)*