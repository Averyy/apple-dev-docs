# DataDetector.Match.SemanticDetails

**Framework**: DataDetection  
**Kind**: enum  
**Role**: Enumeration

An enumeration of types of matches returned by the scanner.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum SemanticDetails
```

#### Discussion

The framework associates each value with an object that contains semantic information about the match.

## Topics

### Structures
- [DataDetector.Match.SemanticDetails.CalendarEvent](./semanticdetails/calendarevent.md)
  The values the framework returns that represent date components of a calendar event.
- [DataDetector.Match.SemanticDetails.EmailAddress](./semanticdetails/emailaddress.md)
  A match that the data detector determines represents an email address.
- [DataDetector.Match.SemanticDetails.FlightNumber](./semanticdetails/flightnumber.md)
  The values the framework returns that represent an airline code and a flight number.
- [DataDetector.Match.SemanticDetails.Link](./semanticdetails/link.md)
  The value the framework returns for a match of a link that contains a valid URL corresponding to the original link.
- [DataDetector.Match.SemanticDetails.Measurement](./semanticdetails/measurement.md)
  A match that the data detector determines represents a measurement.
- [DataDetector.Match.SemanticDetails.MoneyAmount](./semanticdetails/moneyamount.md)
  A match that the data detector determines represents an amount of money.
- [DataDetector.Match.SemanticDetails.PaymentIdentifier](./semanticdetails/paymentidentifier.md)
  A match that the data detector determines represents a payment identifier.
- [DataDetector.Match.SemanticDetails.PhoneNumber](./semanticdetails/phonenumber.md)
  A match that the data detector determines represents a phone number.
- [DataDetector.Match.SemanticDetails.PostalAddress](./semanticdetails/postaladdress.md)
  A match that the data detector determines represents a postal address.
- [DataDetector.Match.SemanticDetails.ShipmentTrackingNumber](./semanticdetails/shipmenttrackingnumber.md)
  A match that the data detector determines represents a shipment tracking number.
### Enumeration Cases
- [case calendarEvent(DataDetector.Match.SemanticDetails.CalendarEvent)](./semanticdetails/calendarevent%28_%29.md)
  A match that the data detector determines represents a calendar event.
- [case emailAddress(DataDetector.Match.SemanticDetails.EmailAddress)](./semanticdetails/emailaddress%28_%29.md)
  A match that the data detector determines represents an email address.
- [case flightNumber(DataDetector.Match.SemanticDetails.FlightNumber)](./semanticdetails/flightnumber%28_%29.md)
  A match that the data detector determines represents a flight number.
- [case link(DataDetector.Match.SemanticDetails.Link)](./semanticdetails/link%28_%29.md)
  A match that the data detector determines represents a link.
- [case measurement(DataDetector.Match.SemanticDetails.Measurement)](./semanticdetails/measurement%28_%29.md)
  A match that the data detector determines represents a measurement.
- [case moneyAmount(DataDetector.Match.SemanticDetails.MoneyAmount)](./semanticdetails/moneyamount%28_%29.md)
  A match that the data detector determines represents an amount of money.
- [case paymentIdentifier(DataDetector.Match.SemanticDetails.PaymentIdentifier)](./semanticdetails/paymentidentifier%28_%29.md)
  A match that the data detector determines represents a payment identifier.
- [case phoneNumber(DataDetector.Match.SemanticDetails.PhoneNumber)](./semanticdetails/phonenumber%28_%29.md)
  A match that the data detector determines represents a phone number.
- [case postalAddress(DataDetector.Match.SemanticDetails.PostalAddress)](./semanticdetails/postaladdress%28_%29.md)
  A match that the data detector determines represents a postal address.
- [case shipmentTrackingNumber(DataDetector.Match.SemanticDetails.ShipmentTrackingNumber)](./semanticdetails/shipmenttrackingnumber%28_%29.md)
  A match that the data detector determines represents a shipping tracking number.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Values that describe highlighting and semantic details of matches
- [DataDetector.Match.HighlightStyle](./highlightstyle.md)
  Values that suggest how to style a highlighted item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/match/semanticdetails)*