# selectedPrinter

**Framework**: UIKit  
**Kind**: property

The selected printer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var selectedPrinter: UIPrinter? { get }
```

#### Discussion

The value of this property is set to the picker you specified at creation time initially. When the picker is dismissed, the value is updated to reflect the printer that the user selected, if any. If the user cancels the picker without selecting a printer, the value of this property does not change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/selectedprinter)*