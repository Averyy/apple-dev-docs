# DataDetector.Match.SemanticDetails

**Framework**: DataDetection  
**Kind**: enum

An enumeration of types of matches returned by the scanner.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
enum SemanticDetails
```

#### Discussion

The framework associates each value with an object that contains semantic information about the match.

## Topics

### Structures
- [DataDetector.Match.SemanticDetails.CalendarEvent](datadetector/match/semanticdetails/calendarevent.md)
  The values the framework returns that represent date components of a calendar event.
- [DataDetector.Match.SemanticDetails.EmailAddress](datadetector/match/semanticdetails/emailaddress.md)
  A match that the data detector determines represents an email address.
- [DataDetector.Match.SemanticDetails.FlightNumber](datadetector/match/semanticdetails/flightnumber.md)
  The values the framework returns that represent an airline code and a flight number.
- [DataDetector.Match.SemanticDetails.Link](datadetector/match/semanticdetails/link.md)
  The value the framework returns for a match of a link that contains a valid URL corresponding to the original link.
- [DataDetector.Match.SemanticDetails.Measurement](datadetector/match/semanticdetails/measurement.md)
  A match that the data detector determines represents a measurement.
- [DataDetector.Match.SemanticDetails.MoneyAmount](datadetector/match/semanticdetails/moneyamount.md)
  A match that the data detector determines represents an amount of money.
- [DataDetector.Match.SemanticDetails.PaymentIdentifier](datadetector/match/semanticdetails/paymentidentifier.md)
  A match that the data detector determines represents a payment identifier.
- [DataDetector.Match.SemanticDetails.PhoneNumber](datadetector/match/semanticdetails/phonenumber.md)
  A match that the data detector determines represents a phone number.
- [DataDetector.Match.SemanticDetails.PostalAddress](datadetector/match/semanticdetails/postaladdress.md)
  A match that the data detector determines represents a postal address.
- [DataDetector.Match.SemanticDetails.ShipmentTrackingNumber](datadetector/match/semanticdetails/shipmenttrackingnumber.md)
  A match that the data detector determines represents a shipment tracking number.
### Enumeration Cases
- [case calendarEvent(DataDetector.Match.SemanticDetails.CalendarEvent)](datadetector/match/semanticdetails/calendarevent(_:).md)
  A match that the data detector determines represents a calendar event.
- [case emailAddress(DataDetector.Match.SemanticDetails.EmailAddress)](datadetector/match/semanticdetails/emailaddress(_:).md)
  A match that the data detector determines represents an email address.
- [case flightNumber(DataDetector.Match.SemanticDetails.FlightNumber)](datadetector/match/semanticdetails/flightnumber(_:).md)
  A match that the data detector determines represents a flight number.
- [case link(DataDetector.Match.SemanticDetails.Link)](datadetector/match/semanticdetails/link(_:).md)
  A match that the data detector determines represents a link.
- [case measurement(DataDetector.Match.SemanticDetails.Measurement)](datadetector/match/semanticdetails/measurement(_:).md)
  A match that the data detector determines represents a measurement.
- [case moneyAmount(DataDetector.Match.SemanticDetails.MoneyAmount)](datadetector/match/semanticdetails/moneyamount(_:).md)
  A match that the data detector determines represents an amount of money.
- [case paymentIdentifier(DataDetector.Match.SemanticDetails.PaymentIdentifier)](datadetector/match/semanticdetails/paymentidentifier(_:).md)
  A match that the data detector determines represents a payment identifier.
- [case phoneNumber(DataDetector.Match.SemanticDetails.PhoneNumber)](datadetector/match/semanticdetails/phonenumber(_:).md)
  A match that the data detector determines represents a phone number.
- [case postalAddress(DataDetector.Match.SemanticDetails.PostalAddress)](datadetector/match/semanticdetails/postaladdress(_:).md)
  A match that the data detector determines represents a postal address.
- [case shipmentTrackingNumber(DataDetector.Match.SemanticDetails.ShipmentTrackingNumber)](datadetector/match/semanticdetails/shipmenttrackingnumber(_:).md)
  A match that the data detector determines represents a shipping tracking number.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [DataDetector.Match.HighlightStyle](datadetector/match/highlightstyle.md)
  Values that suggest how to style a highlighted item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/match/semanticdetails)*