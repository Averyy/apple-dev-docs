# printerDestinations(for:)

**Framework**: UIKit  
**Kind**: method

Searches for a printer destination that matches the print-job attributes.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func printerDestinations(for printInfo: UIPrintInfo) -> [UIPrinterDestination]
```

#### Return Value

A printer or printers that fulfill the printing options in `printInfo`.

#### Discussion

This method inspects the [`UIPrintInfo`](uiprintinfo.md) record to determine which printers to display to the user.

## Parameters

- `printInfo`: The characteristics of a print job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintserviceextension/printerdestinations(for:))*