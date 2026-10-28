# UIPasteboardDetectionPatternEmailAddress

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

A pattern that indicates the pasteboard detects a string that contains an email address.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```c
extern UIPasteboardDetectionPattern const UIPasteboardDetectionPatternEmailAddress;
```

## Discussion

When you include this pattern in calls to [`detectValuesForPatterns:inItemSet:completionHandler:`](./uipasteboard/detectvaluesforpatterns_initemset_completionhandler_.md) or [`detectValuesForPatterns:completionHandler:`](./uipasteboard/detectvaluesforpatterns_completionhandler_.md) and the pasteboard detects a string that contains an email address, the system reports the value as an array of [`NSString`](../Foundation/nsstring.md). You can return the detected results in a paste operation with `UIPasteboardDetectionResultEmailAddress`, which contains a semantic representation of the email address and label values.

## See Also

### Detecting common patterns
- [UIPasteboardDetectionPatternCalendarEvent](./uipasteboarddetectionpatterncalendarevent.md)
  A pattern that indicates the pasteboard detects a string that contains a calendar event.
- [UIPasteboardDetectionPatternFlightNumber](./uipasteboarddetectionpatternflightnumber.md)
  A pattern that indicates the pasteboard detects a string that contains a flight number.
- [UIPasteboardDetectionPatternLink](./uipasteboarddetectionpatternlink.md)
  A pattern that indicates the pasteboard detects of a string that contains a URL.
- [UIPasteboardDetectionPatternMoneyAmount](./uipasteboarddetectionpatternmoneyamount.md)
  A pattern that indicates the pasteboard detects a string that contains an amount of money.
- [static let number: UIPasteboard.DetectionPattern](./uipasteboard/detectionpattern/number.md)
  A pattern that indicates the pasteboard contains a string that consists of a numeric value.
- [UIPasteboardDetectionPatternPhoneNumber](./uipasteboarddetectionpatternphonenumber.md)
  A pattern that indicates the pasteboard detects a string that contains a phone number.
- [UIPasteboardDetectionPatternPostalAddress](./uipasteboarddetectionpatternpostaladdress.md)
  A pattern that indicates the pasteboard detects a string that contains a postal address.
- [static let probableWebSearch: UIPasteboard.DetectionPattern](./uipasteboard/detectionpattern/probablewebsearch.md)
  A pattern that indicates the pasteboard contains a string suitable for use as a web search term.
- [static let probableWebURL: UIPasteboard.DetectionPattern](./uipasteboard/detectionpattern/probableweburl.md)
  A pattern that indicates the pasteboard contains a string that consists of a URL.
- [UIPasteboardDetectionPatternShipmentTrackingNumber](./uipasteboarddetectionpatternshipmenttrackingnumber.md)
  A pattern that indicates the pasteboard detects a string that contains a parcel tracking number and carrier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboarddetectionpatternemailaddress)*