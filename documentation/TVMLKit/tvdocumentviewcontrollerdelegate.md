# TVDocumentViewControllerDelegate

**Framework**: TVMLKit  
**Kind**: protocol  
**Role**: Protocol

Methods to manage updates, events, and errors from the document view controller.

**Availability**:
- tvOS 13.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
protocol TVDocumentViewControllerDelegate : NSObjectProtocol
```

```objc
@protocol TVDocumentViewControllerDelegate <NSObject>
```

## Topics

### Managing Document Updates
- [func documentViewControllerWillUpdate(TVDocumentViewController)](./tvdocumentviewcontrollerdelegate/documentviewcontrollerwillupdate%28_%29.md)
  Tells the delegate that the document will be updated.
- [func documentViewControllerDidUpdate(TVDocumentViewController)](./tvdocumentviewcontrollerdelegate/documentviewcontrollerdidupdate%28_%29.md)
  Tells the delegate that the document has been updated.
- [func documentViewController(TVDocumentViewController, didUpdateWithContext: [String : Any])](./tvdocumentviewcontrollerdelegate/documentviewcontroller%28_,didupdatewithcontext%29.md)
  Tells the delegate that the document has been updated with a specified context.
### Responding to Errors
- [func documentViewController(TVDocumentViewController, didFailUpdateWithError: any Error)](./tvdocumentviewcontrollerdelegate/documentviewcontroller%28_,didfailupdatewitherror%29.md)
  Tells the delegate that the document failed to update.
### Handling Events
- [func documentViewController(TVDocumentViewController, handleEvent: TVDocumentViewController.Event, with: TVViewElement) -> Bool](./tvdocumentviewcontrollerdelegate/documentviewcontroller%28_,handleevent,with%29.md)
  Handles events natively from document view controllers.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Managing Interactions with the Document
- [var delegate: (any TVDocumentViewControllerDelegate)?](./tvdocumentviewcontroller/delegate.md)
  The delegate for handling events in the document view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvdocumentviewcontrollerdelegate)*