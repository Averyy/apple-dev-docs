# UIPrinterPickerController.CompletionHandler

**Framework**: UIKit  
**Kind**: typealias

The completion handler to execute when dismissing a printer picker controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
typealias CompletionHandler = (UIPrinterPickerController, Bool, (any Error)?) -> Void
```

#### Discussion

A printer picker completion handler takes the following parameters:

- **printerPickerController**: The printer picker controller object that is being dismissed. This parameter contains information about the selected printer, if any.
- **userDidSelect**: [`true`](https://developer.apple.com/documentation/swift/true) if the user selected a printer or [`false`](https://developer.apple.com/documentation/swift/false) if the user canceled the selection process. When this parameter is [`true`](https://developer.apple.com/documentation/swift/true), use the `printerPickerController` object to retrieve the selected printer object.
- **error**: An [`NSError`](https://developer.apple.com/documentation/foundation/nserror) object if there was a problem with the printer picker or `nil` if a printer was selected or the user canceled the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/completionhandler)*