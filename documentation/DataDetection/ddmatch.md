# DDMatch

**Framework**: DataDetection  
**Kind**: class

A base class for common types of data that the data detection system matches.

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
class DDMatch
```

#### Overview

The DataDetection framework returns results in objects that are subclasses of `DDMatch`, which are specific to the type of matching data. Each object contains the matched string.

## Topics

### Getting matches
- [var matchedString: String](ddmatch/matchedstring.md)
  A substring that the data detection system identifies from an original string as a common type of data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [DDMatchCalendarEvent](ddmatchcalendarevent.md)
- [DDMatchEmailAddress](ddmatchemailaddress.md)
- [DDMatchFlightNumber](ddmatchflightnumber.md)
- [DDMatchLink](ddmatchlink.md)
- [DDMatchMoneyAmount](ddmatchmoneyamount.md)
- [DDMatchPhoneNumber](ddmatchphonenumber.md)
- [DDMatchPostalAddress](ddmatchpostaladdress.md)
- [DDMatchShipmentTrackingNumber](ddmatchshipmenttrackingnumber.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/ddmatch)*