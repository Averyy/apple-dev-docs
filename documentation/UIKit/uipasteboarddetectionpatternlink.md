# UIPasteboardDetectionPatternLink

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

A pattern that indicates the pasteboard detects of a string that contains a URL.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```c
extern UIPasteboardDetectionPattern const UIPasteboardDetectionPatternLink;
```

#### Discussion

When you include this pattern in calls to [`detectValuesForPatterns:inItemSet:completionHandler:`](./uipasteboard/detectvaluesforpatterns_initemset_completionhandler_.md) or [`detectValuesForPatterns:completionHandler:`](./uipasteboard/detectvaluesforpatterns_completionhandler_.md) and the pasteboard detects a string that contains a website link, the system reports the value as an [`NSURL`](../Foundation/nsurl.md). You can return the detected results in a paste operation with `UIPasteboardDetectionResultLink`, which contains a semantic representation of the website link values.

## See Also

### Detecting common patterns
- [UIPasteboardDetectionPatternCalendarEvent](./uipasteboarddetectionpatterncalendarevent.md)
  A pattern that indicates the pasteboard detects a string that contains a calendar event.
- [UIPasteboardDetectionPatternEmailAddress](./uipasteboarddetectionpatternemailaddress.md)
  A pattern that indicates the pasteboard detects a string that contains an email address.
- [UIPasteboardDetectionPatternFlightNumber](./uipasteboarddetectionpatternflightnumber.md)
  A pattern that indicates the pasteboard detects a string that contains a flight number.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboarddetectionpatternlink)*