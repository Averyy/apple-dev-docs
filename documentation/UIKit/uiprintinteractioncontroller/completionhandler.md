# UIPrintInteractionController.CompletionHandler

**Framework**: UIKit  
**Kind**: typealias

A completion handler for responding to the completion of a print job or for handling printing errors.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
typealias CompletionHandler = (UIPrintInteractionController, Bool, (any Error)?) -> Void
```

#### Discussion

You implement this block as the final argument of [`present(animated:completionHandler:)`](uiprintinteractioncontroller/present(animated:completionhandler:).md), [`present(from:animated:completionHandler:)`](uiprintinteractioncontroller/present(from:animated:completionhandler:).md), or [`present(from:in:animated:completionHandler:)`](uiprintinteractioncontroller/present(from:in:animated:completionhandler:).md). When a print job concludes, you can reset any state set up for printing and do related housekeeping tasks. If the print job encountered an error, it is likely to be a programming error, so you might want to log the error for debugging purposes.

- **`printInteractionController`**: The shared instance of `UIPrintInteractionController` that is managing the print job.
- **`completed`**: A Boolean value that indicates whether the print job completed successfully.
- **`error`**: An instance of the [`NSError`](https://developer.apple.com/documentation/foundation/nserror) that contains information about the printing error. The printing domain is [`UIPrintErrorDomain`](uiprinterrordomain.md). The printing error codes are described in `UIKit Printing Error Codes`. If the print job completes successfully, this parameter is `nil`.

## See Also

- [func print(to: UIPrinter, completionHandler: UIPrintInteractionController.CompletionHandler?) -> Bool](uiprintinteractioncontroller/print(to:completionhandler:).md)
  Prints directly to the specified printer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/completionhandler)*