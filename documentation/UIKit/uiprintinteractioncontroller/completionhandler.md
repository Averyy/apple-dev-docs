# UIPrintInteractionController.CompletionHandler

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

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

```c
typedef void (^)(UIPrintInteractionController *, _Bool, NSError *) UIPrintInteractionCompletionHandler;
```

## Discussion

You implement this block as the final argument of [`present(animated:completionHandler:)`](./present%28animated,completionhandler%29.md), [`present(from:animated:completionHandler:)`](./present%28from,animated,completionhandler%29.md), or [`present(from:in:animated:completionHandler:)`](./present%28from,in,animated,completionhandler%29.md). When a print job concludes, you can reset any state set up for printing and do related housekeeping tasks. If the print job encountered an error, it is likely to be a programming error, so you might want to log the error for debugging purposes.

- **`printInteractionController`**: The shared instance of `UIPrintInteractionController` that is managing the print job.
- **`completed`**: A Boolean value that indicates whether the print job completed successfully.
- **`error`**: An instance of the [`NSError`](../../Foundation/nserror.md) that contains information about the printing error. The printing domain is [`UIPrintErrorDomain`](../uiprinterrordomain.md). The printing error codes are described in `UIKit Printing Error Codes`. If the print job completes successfully, this parameter is `nil`.

## See Also

### Printing directly to a printer
- [func print(to: UIPrinter, completionHandler: UIPrintInteractionController.CompletionHandler?) -> Bool](./print%28to,completionhandler%29.md)
  Prints directly to the specified printer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/completionhandler)*