# print(to:completionHandler:)

**Framework**: UIKit  
**Kind**: method

Prints directly to the specified printer.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func print(to printer: UIPrinter, completionHandler completion: UIPrintInteractionController.CompletionHandler? = nil) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if printing was successful or [`false`](https://developer.apple.com/documentation/swift/false) if there was a problem.

#### Discussion

This method starts the print job and displays the printing progress indicator to the user. This method associates the current printing information (available in the [`printInfo`](uiprintinteractioncontroller/printinfo.md) property) with the job but disables duplex printing. Upon completion of the print job, the print interaction controller executes the block in the `completion` parameter.

## Parameters

- `printer`: The printer to use for printing. You can obtain a list of available printers using a   object.
- `completion`: The block to execute when the print operation finishes.

## See Also

- [UIPrintInteractionController.CompletionHandler](uiprintinteractioncontroller/completionhandler.md)
  A completion handler for responding to the completion of a print job or for handling printing errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/print(to:completionhandler:))*