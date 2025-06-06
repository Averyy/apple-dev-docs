# init(initiallySelectedPrinter:)

**Framework**: UIKit  
**Kind**: init

Creates and returns a printer picker with an initially selected printer object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(initiallySelectedPrinter printer: UIPrinter?)
```

#### Return Value

An initialized printer picker controller object.

#### Discussion

After creating a printer picker controller, assign your delegate as needed and present the controller.

## Parameters

- `printer`: A printer object to select initially. Specify   if you do not want to display a selected printer initially.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/init(initiallyselectedprinter:))*