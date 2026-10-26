# UIDataDetectorTypes

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that define the types of information to detect in text-based content.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
struct UIDataDetectorTypes
```

```c
enum UIDataDetectorTypes : NSUInteger;
```

## Topics

### Constants
- [static var phoneNumber: UIDataDetectorTypes](./uidatadetectortypes/phonenumber.md)
  An option to detect strings with the format of a phone number.
- [static var link: UIDataDetectorTypes](./uidatadetectortypes/link.md)
  An option to detect strings with the format of a URL.
- [static var address: UIDataDetectorTypes](./uidatadetectortypes/address.md)
  An option to detect strings with the format of an address.
- [static var calendarEvent: UIDataDetectorTypes](./uidatadetectortypes/calendarevent.md)
  An option to detect strings with the format of a calendar event.
- [static var shipmentTrackingNumber: UIDataDetectorTypes](./uidatadetectortypes/shipmenttrackingnumber.md)
  An option to detect strings with the format of a tracking number from a package delivery company.
- [static var flightNumber: UIDataDetectorTypes](./uidatadetectortypes/flightnumber.md)
  An option to detect strings with the format of a flight number from an airline.
- [static var lookupSuggestion: UIDataDetectorTypes](./uidatadetectortypes/lookupsuggestion.md)
  An option to detect strings with the format of information that a person might want to look up.
- [static var money: UIDataDetectorTypes](./uidatadetectortypes/money.md)
  An option to detect strings with the format of an amount of money.
- [static var physicalValue: UIDataDetectorTypes](./uidatadetectortypes/physicalvalue.md)
  An option to detect strings with the format of a physical value, such as length or temperature.
- [static var all: UIDataDetectorTypes](./uidatadetectortypes/all.md)
  An option to detect all available types of data.
- [UIDataDetectorTypeNone](./uidatadetectortypes/uidatadetectortypenone.md)
  An option to do no data detection.
### Initializers
- [init(rawValue: UInt)](./uidatadetectortypes/init%28rawvalue%29.md)
  Creates a data detector type with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Constants
- [UIWebView.NavigationType](./uiwebview/navigationtype.md)
  Constant indicating the user’s action.
- [UIWebView.PaginationBreakingMode](./uiwebview/paginationbreakingmode-swift.enum.md)
  The manner in which column- or page-breaking occurs.
- [UIWebView.PaginationMode](./uiwebview/paginationmode-swift.enum.md)
  The layout of content in the web view, which determines the direction that the pages flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatadetectortypes)*