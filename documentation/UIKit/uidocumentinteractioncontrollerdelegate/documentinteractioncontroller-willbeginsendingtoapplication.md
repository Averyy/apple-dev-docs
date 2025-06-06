# documentInteractionController(_:willBeginSendingToApplication:)

**Framework**: UIKit  
**Kind**: method

Called when a document interaction controller’s document is about to be opened by the specified application.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentInteractionController(_ controller: UIDocumentInteractionController, willBeginSendingToApplication application: String?)
```

#### Discussion

This method is called when the user chooses to open a document, which could occur from within a document preview. When a document is passed to another application, the contents of the document interaction controller’s [`annotation`](uidocumentinteractioncontroller/annotation.md) property are passed with it. You can use this method to configure the contents of that property or prepare your own application for handing off the document.

## Parameters

- `controller`: The document interaction controller whose document is about to be opened.
- `application`: The bundle identifier of the application that is about to open the document. This value corresponds to the value in the   key of the application’s   file.

## See Also

- [func documentInteractionController(UIDocumentInteractionController, didEndSendingToApplication: String?)](uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:didendsendingtoapplication:).md)
  Called when a document interaction controller’s document has been handed off to the specified application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:willbeginsendingtoapplication:))*