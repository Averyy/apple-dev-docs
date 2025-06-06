# UIDataDetectorTypes

**Framework**: UIKit  
**Kind**: struct

Constants that define the types of information to detect in text-based content.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
struct UIDataDetectorTypes
```

## Topics

### Constants
- [static var phoneNumber: UIDataDetectorTypes](uidatadetectortypes/phonenumber.md)
  An option to detect strings with the format of a phone number.
- [static var link: UIDataDetectorTypes](uidatadetectortypes/link.md)
  An option to detect strings with the format of a URL.
- [static var address: UIDataDetectorTypes](uidatadetectortypes/address.md)
  An option to detect strings with the format of an address.
- [static var calendarEvent: UIDataDetectorTypes](uidatadetectortypes/calendarevent.md)
  An option to detect strings with the format of a calendar event.
- [static var shipmentTrackingNumber: UIDataDetectorTypes](uidatadetectortypes/shipmenttrackingnumber.md)
  An option to detect strings with the format of a tracking number from a package delivery company.
- [static var flightNumber: UIDataDetectorTypes](uidatadetectortypes/flightnumber.md)
  An option to detect strings with the format of a flight number from an airline.
- [static var lookupSuggestion: UIDataDetectorTypes](uidatadetectortypes/lookupsuggestion.md)
  An option to detect strings with the format of information that a person might want to look up.
- [static var money: UIDataDetectorTypes](uidatadetectortypes/money.md)
  An option to detect strings with the format of an amount of money.
- [static var physicalValue: UIDataDetectorTypes](uidatadetectortypes/physicalvalue.md)
  An option to detect strings with the format of a physical value, such as length or temperature.
- [static var all: UIDataDetectorTypes](uidatadetectortypes/all.md)
  An option to detect all available types of data.
### Initializers
- [init(rawValue: UInt)](uidatadetectortypes/init(rawvalue:).md)
  Creates a data detector type with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var dataDetectorTypes: UIDataDetectorTypes](uitextview/datadetectortypes.md)
  The types of data that convert to tappable URLs in the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatadetectortypes)*