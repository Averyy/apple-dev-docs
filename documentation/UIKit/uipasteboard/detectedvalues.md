# UIPasteboard.DetectedValues

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

An object that contains common types of data that the data detection system matches for a pasteboard.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS

## Declaration

```swift
struct DetectedValues
```

## Topics

### Detected patterns
- [var patterns: Set<PartialKeyPath<UIPasteboard.DetectedValues>>](./detectedvalues/patterns.md)
  A set of key paths that represent patterns that the data detection system identifies.
- [var probableWebSearch: String](./detectedvalues/probablewebsearch.md)
  A string that the data detection system identifies as a probable web search item.
- [var probableWebURL: String](./detectedvalues/probableweburl.md)
  A string that the data detection system identifies as a probable web URL.
### Detected values
- [var calendarEvents: [DDMatchCalendarEvent]](./detectedvalues/calendarevents.md)
  An array of calendar events that the data detection system identifies.
- [var emailAddresses: [DDMatchEmailAddress]](./detectedvalues/emailaddresses.md)
  An array of email addresses that the data detection system identifies.
- [var flightNumbers: [DDMatchFlightNumber]](./detectedvalues/flightnumbers.md)
  An array of flight numbers that the system data detection system identifies.
- [var links: [DDMatchLink]](./detectedvalues/links.md)
  An array of web links that the data detection system identifies.
- [var moneyAmounts: [DDMatchMoneyAmount]](./detectedvalues/moneyamounts.md)
  An array of money amounts and currencies that the data detection system identifies.
- [var number: Double?](./detectedvalues/number.md)
  A number that the data detection system identifies.
- [var phoneNumbers: [DDMatchPhoneNumber]](./detectedvalues/phonenumbers.md)
  An array of phone numbers that the data detection system identifies.
- [var postalAddresses: [DDMatchPostalAddress]](./detectedvalues/postaladdresses.md)
  An array of postal addresses that the data detection system identifies.
- [var shipmentTrackingNumbers: [DDMatchShipmentTrackingNumber]](./detectedvalues/shipmenttrackingnumbers.md)
  An array of parcel tracking numbers that the data detection system identifies.

## See Also

### Detecting patterns of content in pasteboard items
- [func detectedPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> Set<PartialKeyPath<UIPasteboard.DetectedValues>>](./detectedpatterns%28for%29.md)
  Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard, and return the patterns that it matches.
- [func detectedPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?) async throws -> [Set<PartialKeyPath<UIPasteboard.DetectedValues>>]](./detectedpatterns%28for,initemset%29.md)
  Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard items, and return the patterns that it matches.
- [func detectedValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> UIPasteboard.DetectedValues](./detectedvalues%28for%29.md)
  Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard, and return the values that it matches.
- [func detectValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?, completionHandler: (Result<[UIPasteboard.DetectedValues], any Error>) -> ())](./detectvalues%28for,initemset,completionhandler%29-pm9l.md)
  Requests that the data detection system identify the types of data that you specify for the pasteboard items, and provide the values that it matches to your closure.
- [func detectedValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?) async throws -> [UIPasteboard.DetectedValues]](./detectedvalues%28for,initemset%29.md)
  Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard item, and return the values that it matches for each pasteboard.
- [UIPasteboard.DetectionPattern](./detectionpattern.md)
  An object that represents a pattern to detect for the pasteboard, such as a URL, text, or a number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/detectedvalues)*