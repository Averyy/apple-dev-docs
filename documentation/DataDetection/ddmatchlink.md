# DDMatchLink

**Framework**: DataDetection  
**Kind**: class  
**Role**: Class

An object that contains a web link that the data detection system matches.

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
class DDMatchLink
```

```objc
@interface DDMatchLink : DDMatch
```

#### Overview

The DataDetection framework returns a link match in a `DDMatchLink` object, which contains a [`URL`](../Foundation/url.md).

## Topics

### Getting link information
- [var url: URL](./ddmatchlink/url.md)
  An address for a web resource, such as a webpage or image.

## Relationships

### Inherits From
- [DDMatch](./ddmatch.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Matched data types
- [class DDMatchCalendarEvent](./ddmatchcalendarevent.md)
  An object that represents a calendar date or date range that the data detection system matches.
- [class DDMatchEmailAddress](./ddmatchemailaddress.md)
  An object that contains an email address that the data detection system matches.
- [class DDMatchFlightNumber](./ddmatchflightnumber.md)
  An object that contains a flight number that the data detection system matches.
- [class DDMatchMoneyAmount](./ddmatchmoneyamount.md)
  An object that contains an amount of money that the data detection system matches.
- [class DDMatchPhoneNumber](./ddmatchphonenumber.md)
  An object that contains a phone number that the data detection system matches.
- [class DDMatchPostalAddress](./ddmatchpostaladdress.md)
  An object that contains a postal address that the data detection system matches.
- [class DDMatchShipmentTrackingNumber](./ddmatchshipmenttrackingnumber.md)
  An object that contains parcel tracking information that the data detection system matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/ddmatchlink)*