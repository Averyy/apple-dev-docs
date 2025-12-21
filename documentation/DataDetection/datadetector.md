# DataDetector

**Framework**: DataDetection  
**Kind**: enum

An extension to the string protocol that scans strings for semantic entities, such as email addresses, phone numbers, URLs, and flight information.

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
enum DataDetector
```

## Topics

### Methods that scan strings for known content types
- [func dataDetectorMatches(DataDetector.MatchType, options: DataDetector.Options) -> some AsyncSequence<DataDetector.Match, Never>
](../Swift/StringProtocol/dataDetectorMatches(_:options:).md)
  Searches for known data types in a string or a substring.
### Structures
- [DataDetector.Match](datadetector/match.md)
  A representation of a match that includes common properties and an enumeration that represents the match type and its specific semantic components.
- [DataDetector.MatchType](datadetector/matchtype.md)
  A set of types of matches that the system can find in a string.
- [DataDetector.Options](datadetector/options.md)
  A set of options you can use to refine the behavior of text scanning, and better interpret the semantic domain of the matches.
### Known entity types
- [static let all: DataDetector.MatchType](datadetector/matchtype/all.md)
  A set of types that includes all publicly useable types.
- [static let link: DataDetector.MatchType](datadetector/matchtype/link.md)
  The type that represents links, not limited to web links.
- [static let emailAddress: DataDetector.MatchType](datadetector/matchtype/emailaddress.md)
  The type that represents email addresses.
- [static let phoneNumber: DataDetector.MatchType](datadetector/matchtype/phonenumber.md)
  The type that represents phone numbers.
- [static let postalAddress: DataDetector.MatchType](datadetector/matchtype/postaladdress.md)
  The type that represents postal addresses.
- [static let calendarEvent: DataDetector.MatchType](datadetector/matchtype/calendarevent.md)
  The type that represents calendar events, such as dates and times, or date and time ranges.
- [static let moneyAmount: DataDetector.MatchType](datadetector/matchtype/moneyamount.md)
  The type that represents monetary amounts.
- [static let measurement: DataDetector.MatchType](datadetector/matchtype/measurement.md)
  The type that represents measurements, such as distances and weights.
- [static let flightNumber: DataDetector.MatchType](datadetector/matchtype/flightnumber.md)
  The type that represents flight numbers.
- [static let shipmentTrackingNumber: DataDetector.MatchType](datadetector/matchtype/shipmenttrackingnumber.md)
  The type that represents shipment tracking numbers.
- [static let paymentIdentifier: DataDetector.MatchType](datadetector/matchtype/paymentidentifier.md)
  The type that represents payment identifiers, such as Universal Payments Interface (UPI) identifiers.

## See Also

- [class DDMatch](ddmatch.md)
  A base class for common types of data that the data detection system matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector)*