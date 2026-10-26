# Pasteboard detection patterns

**Framework**: AppKit  
**Role**: API Collection

Common types of data that the data detection system matches for a pasteboard.

## Topics

### Email and web values
- [var emailAddresses: [DDMatchEmailAddress]](./nspasteboard/detectedvalues/emailaddresses.md)
  An array of email addresses that the data detection system identifies.
- [var links: [DDMatchLink]](./nspasteboard/detectedvalues/links.md)
  An array of web links that the data detection system identifies.
- [var probableWebSearch: String](./nspasteboard/detectedvalues/probablewebsearch.md)
  A string that the data detection system identifies as a probable web search item, suitable for implementing “Paste and Search”.
- [var probableWebURL: String](./nspasteboard/detectedvalues/probableweburl.md)
  A string that the data detection system identifies as a probable web URL, suitable for implementing “Paste and Go”.
- [NSPasteboardDetectionPatternEmailAddress](./nspasteboarddetectionpatternemailaddress.md)
  A pattern that indicates the pasteboard detects a string that contains an email address.
- [NSPasteboardDetectionPatternLink](./nspasteboarddetectionpatternlink.md)
  A pattern that indicates the pasteboard detects a string that contains a URL.
- [NSPasteboardDetectionPatternProbableWebSearch](./nspasteboarddetectionpatternprobablewebsearch.md)
  A pattern that indicates the pasteboard detects a string suitable for use as a web search term.
- [NSPasteboardDetectionPatternProbableWebURL](./nspasteboarddetectionpatternprobableweburl.md)
  A pattern that indicates the pasteboard detects a string that consists of a web URL.
### Contact values
- [var phoneNumbers: [DDMatchPhoneNumber]](./nspasteboard/detectedvalues/phonenumbers.md)
  An array of phone numbers that the data detection system identifies.
- [var postalAddresses: [DDMatchPostalAddress]](./nspasteboard/detectedvalues/postaladdresses.md)
  An array of postal addresses that the data detection system identifies.
- [NSPasteboardDetectionPatternPhoneNumber](./nspasteboarddetectionpatternphonenumber.md)
  A pattern that indicates the pasteboard detects a string that contains a phone number.
- [NSPasteboardDetectionPatternPostalAddress](./nspasteboarddetectionpatternpostaladdress.md)
  A pattern that indicates the pasteboard detects a string that contains a postal address.
### Calendar values
- [var calendarEvents: [DDMatchCalendarEvent]](./nspasteboard/detectedvalues/calendarevents.md)
  An array of calendar events that the data detection system identifies.
- [NSPasteboardDetectionPatternCalendarEvent](./nspasteboarddetectionpatterncalendarevent.md)
  A pattern that indicates the pasteboard detects a string that contains a calendar event.
### Numeric values
- [var moneyAmounts: [DDMatchMoneyAmount]](./nspasteboard/detectedvalues/moneyamounts.md)
  An array of money amounts and currencies that the data detection system identifies.
- [var number: Double?](./nspasteboard/detectedvalues/number.md)
  A number that the data detection system identifies.
- [NSPasteboardDetectionPatternMoneyAmount](./nspasteboarddetectionpatternmoneyamount.md)
  A pattern that indicates the pasteboard detects a string that contains an amount of money.
- [NSPasteboardDetectionPatternNumber](./nspasteboarddetectionpatternnumber.md)
  A pattern that indicates the pasteboard detects a string that consists of a numeric value.
### Transportation-related values
- [var flightNumbers: [DDMatchFlightNumber]](./nspasteboard/detectedvalues/flightnumbers.md)
  An array of flight numbers that the data detection system identifies.
- [var shipmentTrackingNumbers: [DDMatchShipmentTrackingNumber]](./nspasteboard/detectedvalues/shipmenttrackingnumbers.md)
  An array of parcel tracking numbers and carriers that the data detection system identifies.
- [NSPasteboardDetectionPatternFlightNumber](./nspasteboarddetectionpatternflightnumber.md)
  A pattern that indicates the pasteboard detects a string that contains a flight number.
- [NSPasteboardDetectionPatternShipmentTrackingNumber](./nspasteboarddetectionpatternshipmenttrackingnumber.md)
  A pattern that indicates the pasteboard detects a string that contains a parcel tracking number and carrier.
### Patterns
- [var patterns: Set<PartialKeyPath<NSPasteboard.DetectedValues>>](./nspasteboard/detectedvalues/patterns.md)
  A set of key paths that represent patterns that the data detection system identifies.
### Pattern type
- [NSPasteboard.DetectedValues](./nspasteboard/detectedvalues.md)
  A type that contains common types of data that the data detection system matches for a pasteboard.
- [NSPasteboardDetectionPattern](./nspasteboarddetectionpattern.md)
  A pattern to detect on the pasteboard, such as a URL, text, or a number.

## See Also

### Detecting patterns and metadata in pasteboard items
- [func detectedPatterns(for: Set<PartialKeyPath<NSPasteboard.DetectedValues>>) async throws -> Set<PartialKeyPath<NSPasteboard.DetectedValues>>](./nspasteboard/detectedpatterns%28for%29.md)
  Determines whether the first pasteboard item matches the specified patterns, without notifying the person using the app.
- [func detectedValues(for: Set<PartialKeyPath<NSPasteboard.DetectedValues>>) async throws -> NSPasteboard.DetectedValues](./nspasteboard/detectedvalues%28for%29.md)
  Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [NSPasteboard.DetectedValues](./nspasteboard/detectedvalues.md)
  A type that contains common types of data that the data detection system matches for a pasteboard.
- [func detectedMetadata(for: Set<PartialKeyPath<NSPasteboard.DetectedMetadata>>) async throws -> NSPasteboard.DetectedMetadata](./nspasteboard/detectedmetadata%28for%29.md)
  Determines available metadata from the specified metadata types for the first pasteboard item, without notifying the person using the app.
- [NSPasteboard.DetectedMetadata](./nspasteboard/detectedmetadata.md)
  An object that contains common types of metadata that the data detection system matches for a pasteboard.
- [Pasteboard detection metadata types](./nspasteboard-detection-metadata-types.md)
  Common types of metadata that the data detection system matches for a pasteboard.
- [- detectPatternsForPatterns:completionHandler:](./nspasteboard/detectpatternsforpatterns_completionhandler_.md)
  Determines whether the first pasteboard item matches the specified patterns, without notifying the person using the app.
- [- detectValuesForPatterns:completionHandler:](./nspasteboard/detectvaluesforpatterns_completionhandler_.md)
  Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [- detectMetadataForTypes:completionHandler:](./nspasteboard/detectmetadatafortypes_completionhandler_.md)
  Determines available metadata from the specified metadata types for the first pasteboard item, without notifying the person using the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard-detection-patterns)*