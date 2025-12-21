# DataDetection

**Framework**: DataDetection  
**Kind**: module

Access and utilize common types of data that the data detection system matches.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

#### Overview

Data detection methods in other frameworks detect common types of data represented in text, and return  DataDetection framework classes that provide semantic meaning for matches. Get relevant, domain-specific information from matches of the following types:

- Calendar events
- Email addresses
- Flight numbers
- Web links
- Amounts of money, with currencies
- Phone numbers
- Postal addresses
- Shipment tracking numbers

Use functions, such as those in [`UIPasteboard`](https://developer.apple.com/documentation/UIKit/UIPasteboard), to detect the types of data that you specify in a particular context. For example, find email addresses in a pasteboard using [`detectValues(for:completionHandler:)`](https://developer.apple.com/documentation/UIKit/UIPasteboard/detectValues(for:completionHandler:)-6adre) as this example shows:

```swift
UIPasteboard.general.detectValues(for: [\.emailAddresses]) { [self] result in
    switch result {
    case .success(let detectedValues):
        guard let firstEmailAddressMatch = detectedValues.emailAddresses.first else {
            return
        }
        let newEmailAddress = firstEmailAddressMatch.emailAddress
        let newLabel = firstEmailAddressMatch.label
        addNewEmail(for: contact, address: newEmailAddress, label: newLabel)
    case .failure(let error):
        print("Error detecting email addresses: \(error.localizedDescription)")
    }
}
```

Then, inspect and use the data from objects that the data detection system returns.

## Topics

### Matched strings
- [class DDMatch](ddmatch.md)
  A base class for common types of data that the data detection system matches.
- [enum DataDetector](datadetector.md)
  An extension to the string protocol that scans strings for semantic entities, such as email addresses, phone numbers, URLs, and flight information.
### Matched data types
- [class DDMatchCalendarEvent](ddmatchcalendarevent.md)
  An object that represents a calendar date or date range that the data detection system matches.
- [class DDMatchEmailAddress](ddmatchemailaddress.md)
  An object that contains an email address that the data detection system matches.
- [class DDMatchFlightNumber](ddmatchflightnumber.md)
  An object that contains a flight number that the data detection system matches.
- [class DDMatchLink](ddmatchlink.md)
  An object that contains a web link that the data detection system matches.
- [class DDMatchMoneyAmount](ddmatchmoneyamount.md)
  An object that contains an amount of money that the data detection system matches.
- [class DDMatchPhoneNumber](ddmatchphonenumber.md)
  An object that contains a phone number that the data detection system matches.
- [class DDMatchPostalAddress](ddmatchpostaladdress.md)
  An object that contains a postal address that the data detection system matches.
- [class DDMatchShipmentTrackingNumber](ddmatchshipmenttrackingnumber.md)
  An object that contains parcel tracking information that the data detection system matches.
### Pasteboard detectors
- [func detectPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, completionHandler: (Result<Set<PartialKeyPath<UIPasteboard.DetectedValues>>, any Error>) -> ())](../UIKit/UIPasteboard/detectPatterns(for:completionHandler:)-23vwn.md)
  Requests that the data detection system identify the patterns that you specify for the pasteboard, and provide the patterns that it matches to your closure.
- [func detectedPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> Set<PartialKeyPath<UIPasteboard.DetectedValues>>](../UIKit/UIPasteboard/detectedPatterns(for:).md)
  Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard, and return the patterns that it matches.
- [func detectPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?, completionHandler: (Result<[Set<PartialKeyPath<UIPasteboard.DetectedValues>>], any Error>) -> ())](../UIKit/UIPasteboard/detectPatterns(for:inItemSet:completionHandler:)-7ubl1.md)
  Requests that the data detection system identify the patterns that you specify for the pasteboard items, and provide the patterns that it matches to your closure.
- [func detectedPatterns(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?) async throws -> [Set<PartialKeyPath<UIPasteboard.DetectedValues>>]](../UIKit/UIPasteboard/detectedPatterns(for:inItemSet:).md)
  Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard items, and return the patterns that it matches.
- [func detectValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, completionHandler: (Result<UIPasteboard.DetectedValues, any Error>) -> ())](../UIKit/UIPasteboard/detectValues(for:completionHandler:)-6adre.md)
  Requests that the data detection system identify the types of data that you specify for the pasteboard, and provide the values that it matches to your closure.
- [func detectedValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> UIPasteboard.DetectedValues](../UIKit/UIPasteboard/detectedValues(for:).md)
  Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard, and return the values that it matches.
- [func detectValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?, completionHandler: (Result<[UIPasteboard.DetectedValues], any Error>) -> ())](../UIKit/UIPasteboard/detectValues(for:inItemSet:completionHandler:)-pm9l.md)
  Requests that the data detection system identify the types of data that you specify for the pasteboard items, and provide the values that it matches to your closure.
- [func detectedValues(for: Set<PartialKeyPath<UIPasteboard.DetectedValues>>, inItemSet: IndexSet?) async throws -> [UIPasteboard.DetectedValues]](../UIKit/UIPasteboard/detectedValues(for:inItemSet:).md)
  Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard item, and return the values that it matches for each pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/DataDetection)*