# documentInteractionController(_:didEndSendingToApplication:)

**Framework**: UIKit  
**Kind**: method

Called when a document interaction controller’s document has been handed off to the specified application.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentInteractionController(_ controller: UIDocumentInteractionController, didEndSendingToApplication application: String?)
```

#### Discussion

This method is called after the document information has been saved for the specified application.

## Parameters

- `controller`: The document interaction controller whose document is about to be opened.
- `application`: The bundle identifier of the application that is about to open the document. This value corresponds to the value in the   key of the application’s   file.

## See Also

- [func documentInteractionController(UIDocumentInteractionController, willBeginSendingToApplication: String?)](uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:willbeginsendingtoapplication:).md)
  Called when a document interaction controller’s document is about to be opened by the specified application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(_:didendsendingtoapplication:))*