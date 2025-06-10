# NSPasteboard.DetectedValues

**Framework**: AppKit  
**Kind**: struct

A type that contains common types of data that the data detection system matches for a pasteboard.

**Availability**:
- macOS 15.4+

## Declaration

```swift
struct DetectedValues
```

## Topics

### Email and web values
- [var emailAddresses: [DDMatchEmailAddress]](nspasteboard/detectedvalues/emailaddresses.md)
  An array of email addresses that the data detection system identifies.
- [var links: [DDMatchLink]](nspasteboard/detectedvalues/links.md)
  An array of web links that the data detection system identifies.
- [var probableWebSearch: String](nspasteboard/detectedvalues/probablewebsearch.md)
  A string that the data detection system identifies as a probable web search item, suitable for implementing “Paste and Search”.
- [var probableWebURL: String](nspasteboard/detectedvalues/probableweburl.md)
  A string that the data detection system identifies as a probable web URL, suitable for implementing “Paste and Go”.
### Contact values
- [var phoneNumbers: [DDMatchPhoneNumber]](nspasteboard/detectedvalues/phonenumbers.md)
  An array of phone numbers that the data detection system identifies.
- [var postalAddresses: [DDMatchPostalAddress]](nspasteboard/detectedvalues/postaladdresses.md)
  An array of postal addresses that the data detection system identifies.
### Calendar values
- [var calendarEvents: [DDMatchCalendarEvent]](nspasteboard/detectedvalues/calendarevents.md)
  An array of calendar events that the data detection system identifies.
### Numeric values
- [var moneyAmounts: [DDMatchMoneyAmount]](nspasteboard/detectedvalues/moneyamounts.md)
  An array of money amounts and currencies that the data detection system identifies.
- [var number: Double?](nspasteboard/detectedvalues/number.md)
  A number that the data detection system identifies.
### Transportation-related values
- [var flightNumbers: [DDMatchFlightNumber]](nspasteboard/detectedvalues/flightnumbers.md)
  An array of flight numbers that the data detection system identifies.
- [var shipmentTrackingNumbers: [DDMatchShipmentTrackingNumber]](nspasteboard/detectedvalues/shipmenttrackingnumbers.md)
  An array of parcel tracking numbers and carriers that the data detection system identifies.
### Patterns
- [var patterns: Set<PartialKeyPath<NSPasteboard.DetectedValues>>](nspasteboard/detectedvalues/patterns.md)
  A set of key paths that represent patterns that the data detection system identifies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/detectedvalues)*