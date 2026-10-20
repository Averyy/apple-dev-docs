# documentPickerWasCancelled(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user canceled the document picker.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentPickerWasCancelled(_ controller: UIDocumentPickerViewController)
```

```objc
- (void) documentPickerWasCancelled:(UIDocumentPickerViewController *) controller;
```

## Mentions

- [Providing access to directories](../providing-access-to-directories.md)

## Parameters

- `controller`: The document picker that called this method.

## See Also

### Responding to user actions
- [func documentPicker(UIDocumentPickerViewController, didPickDocumentsAt: [URL])](./documentpicker%28_,didpickdocumentsat%29.md)
  Tells the delegate that the user has selected one or more documents.
- [func documentPicker(UIDocumentPickerViewController, didPickDocumentAt: URL)](./documentpicker%28_,didpickdocumentat%29.md)
  Tells the delegate that the user has selected a document or a destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerdelegate/documentpickerwascancelled(_:))*