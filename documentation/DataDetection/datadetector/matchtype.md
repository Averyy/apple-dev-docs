# DataDetector.MatchType

**Framework**: DataDetection  
**Kind**: struct  
**Role**: Structure

A set of types of matches that the system can find in a string.

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
struct MatchType
```

## Discussion

> **Note**: The framework may either not support or only partially support some types in certain languages.

## Topics

### Supported match types
- [static let all: DataDetector.MatchType](./matchtype/all.md)
  A set of types that includes all publicly useable types.
- [static let calendarEvent: DataDetector.MatchType](./matchtype/calendarevent.md)
  The type that represents calendar events, such as dates and times, or date and time ranges.
- [static let emailAddress: DataDetector.MatchType](./matchtype/emailaddress.md)
  The type that represents email addresses.
- [static let flightNumber: DataDetector.MatchType](./matchtype/flightnumber.md)
  The type that represents flight numbers.
- [static let link: DataDetector.MatchType](./matchtype/link.md)
  The type that represents links, not limited to web links.
- [static let measurement: DataDetector.MatchType](./matchtype/measurement.md)
  The type that represents measurements, such as distances and weights.
- [static let moneyAmount: DataDetector.MatchType](./matchtype/moneyamount.md)
  The type that represents monetary amounts.
- [static let paymentIdentifier: DataDetector.MatchType](./matchtype/paymentidentifier.md)
  The type that represents payment identifiers, such as Universal Payments Interface (UPI) identifiers.
- [static let phoneNumber: DataDetector.MatchType](./matchtype/phonenumber.md)
  The type that represents phone numbers.
- [static let postalAddress: DataDetector.MatchType](./matchtype/postaladdress.md)
  The type that represents postal addresses.
- [static let shipmentTrackingNumber: DataDetector.MatchType](./matchtype/shipmenttrackingnumber.md)
  The type that represents shipment tracking numbers.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Structures
- [DataDetector.Match](./match.md)
  A representation of a match that includes common properties and an enumeration that represents the match type and its specific semantic components.
- [DataDetector.Options](./options.md)
  A set of options you can use to refine the behavior of text scanning, and better interpret the semantic domain of the matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/matchtype)*