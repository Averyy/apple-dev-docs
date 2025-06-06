# UIPasteboard.DetectedValues

**Framework**: UIKit  
**Kind**: struct

An object that contains common types of data that the data detection system matches for a pasteboard.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
struct DetectedValues
```

## Topics

### Detected patterns
- [var patterns: Set<PartialKeyPath<UIPasteboard.DetectedValues>>](uipasteboard/detectedvalues/patterns.md)
  A set of key paths that represent patterns that the data detection system identifies.
- [var probableWebSearch: String](uipasteboard/detectedvalues/probablewebsearch.md)
  A string that the data detection system identifies as a probable web search item.
- [var probableWebURL: String](uipasteboard/detectedvalues/probableweburl.md)
  A string that the data detection system identifies as a probable web URL.
### Detected values
- [var calendarEvents: [DDMatchCalendarEvent]](uipasteboard/detectedvalues/calendarevents.md)
  An array of calendar events that the data detection system identifies.
- [var emailAddresses: [DDMatchEmailAddress]](uipasteboard/detectedvalues/emailaddresses.md)
  An array of email addresses that the data detection system identifies.
- [var flightNumbers: [DDMatchFlightNumber]](uipasteboard/detectedvalues/flightnumbers.md)
  An array of flight numbers that the system data detection system identifies.
- [var links: [DDMatchLink]](uipasteboard/detectedvalues/links.md)
  An array of web links that the data detection system identifies.
- [var moneyAmounts: [DDMatchMoneyAmount]](uipasteboard/detectedvalues/moneyamounts.md)
  An array of money amounts and currencies that the data detection system identifies.
- [var number: Double?](uipasteboard/detectedvalues/number.md)
  A number that the data detection system identifies.
- [var phoneNumbers: [DDMatchPhoneNumber]](uipasteboard/detectedvalues/phonenumbers.md)
  An array of phone numbers that the data detection system identifies.
- [var postalAddresses: [DDMatchPostalAddress]](uipasteboard/detectedvalues/postaladdresses.md)
  An array of postal addresses that the data detection system identifies.
- [var shipmentTrackingNumbers: [DDMatchShipmentTrackingNumber]](uipasteboard/detectedvalues/shipmenttrackingnumbers.md)
  An array of parcel tracking numbers that the data detection system identifies.

## See Also

- [func detectPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, completionHandler: (Result<Set<PartialKeyPath<UIPasteboard.DetectedValues>>, any Error>) -> ())](uipasteboard/detectpatterns(for:completionhandler:)-23vwn.md)
  Requests that the data detection system identify the patterns that you specify for the pasteboard, and provide the patterns that it matches to your closure.
- [func detectedPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> Set<PartialKeyPath<UIPasteboard.DetectedValues>>](uipasteboard/detectedpatterns(for:).md)
  Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard, and return the patterns that it matches.
- [func detectPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?, completionHandler: (Result<[Set<PartialKeyPath<UIPasteboard.DetectedValues>>], any Error>) -> ())](uipasteboard/detectpatterns(for:initemset:completionhandler:)-7ubl1.md)
  Requests that the data detection system identify the patterns that you specify for the pasteboard items, and provide the patterns that it matches to your closure.
- [func detectedPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?) async throws -> [Set<PartialKeyPath<UIPasteboard.DetectedValues>>]](uipasteboard/detectedpatterns(for:initemset:).md)
  Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard items, and return the patterns that it matches.
- [func detectValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, completionHandler: (Result<UIPasteboard.DetectedValues, any Error>) -> ())](uipasteboard/detectvalues(for:completionhandler:)-6adre.md)
  Requests that the data detection system identify the types of data that you specify for the pasteboard, and provide the values that it matches to your closure.
- [func detectedValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> UIPasteboard.DetectedValues](uipasteboard/detectedvalues(for:).md)
  Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard, and return the values that it matches.
- [func detectValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?, completionHandler: (Result<[UIPasteboard.DetectedValues], any Error>) -> ())](uipasteboard/detectvalues(for:initemset:completionhandler:)-pm9l.md)
  Requests that the data detection system identify the types of data that you specify for the pasteboard items, and provide the values that it matches to your closure.
- [func detectedValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?) async throws -> [UIPasteboard.DetectedValues]](uipasteboard/detectedvalues(for:initemset:).md)
  Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard item, and return the values that it matches for each pasteboard.
- [UIPasteboard.DetectionPattern](uipasteboard/detectionpattern.md)
  An object that represents a pattern to detect for the pasteboard, such as a URL, text, or a number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/detectedvalues)*