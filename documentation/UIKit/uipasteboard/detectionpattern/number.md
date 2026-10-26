# number

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A pattern that indicates the pasteboard contains a string that consists of a numeric value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
static let number: UIPasteboard.DetectionPattern
```

```c
extern UIPasteboardDetectionPattern const UIPasteboardDetectionPatternNumber;
```

#### Discussion

When you include this pattern in calls to [`detectValues(for:inItemSet:completionHandler:)`](../detectvalues%28for,initemset,completionhandler%29-pm9l.md) or [`detectValues(for:completionHandler:)`](../detectvalues%28for,completionhandler%29-6adre.md) — [`detectValuesForPatterns:inItemSet:completionHandler:`](../detectvaluesforpatterns_initemset_completionhandler_.md) or [`detectValuesForPatterns:completionHandler:`](../detectvaluesforpatterns_completionhandler_.md) in Objective-C — and the pasteboard detects a number, it reports the value as an [`NSNumber`](../../../Foundation/nsnumber.md).

## See Also

### Detecting common patterns
- [static let probableWebSearch: UIPasteboard.DetectionPattern](./probablewebsearch.md)
  A pattern that indicates the pasteboard contains a string suitable for use as a web search term.
- [static let probableWebURL: UIPasteboard.DetectionPattern](./probableweburl.md)
  A pattern that indicates the pasteboard contains a string that consists of a URL.
- [UIPasteboardDetectionPatternCalendarEvent](../../uipasteboarddetectionpatterncalendarevent.md)
  A pattern that indicates the pasteboard detects a string that contains a calendar event.
- [UIPasteboardDetectionPatternEmailAddress](../../uipasteboarddetectionpatternemailaddress.md)
  A pattern that indicates the pasteboard detects a string that contains an email address.
- [UIPasteboardDetectionPatternFlightNumber](../../uipasteboarddetectionpatternflightnumber.md)
  A pattern that indicates the pasteboard detects a string that contains a flight number.
- [UIPasteboardDetectionPatternLink](../../uipasteboarddetectionpatternlink.md)
  A pattern that indicates the pasteboard detects of a string that contains a URL.
- [UIPasteboardDetectionPatternMoneyAmount](../../uipasteboarddetectionpatternmoneyamount.md)
  A pattern that indicates the pasteboard detects a string that contains an amount of money.
- [UIPasteboardDetectionPatternPhoneNumber](../../uipasteboarddetectionpatternphonenumber.md)
  A pattern that indicates the pasteboard detects a string that contains a phone number.
- [UIPasteboardDetectionPatternPostalAddress](../../uipasteboarddetectionpatternpostaladdress.md)
  A pattern that indicates the pasteboard detects a string that contains a postal address.
- [UIPasteboardDetectionPatternShipmentTrackingNumber](../../uipasteboarddetectionpatternshipmenttrackingnumber.md)
  A pattern that indicates the pasteboard detects a string that contains a parcel tracking number and carrier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/detectionpattern/number)*