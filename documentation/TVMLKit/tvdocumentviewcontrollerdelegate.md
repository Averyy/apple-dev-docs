# TVDocumentViewControllerDelegate

**Framework**: TVMLKit  
**Kind**: protocol

Methods to manage updates, events, and errors from the document view controller.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
protocol TVDocumentViewControllerDelegate : NSObjectProtocol
```

## Topics

### Managing Document Updates
- [func documentViewControllerWillUpdate(TVDocumentViewController)](tvdocumentviewcontrollerdelegate/documentviewcontrollerwillupdate(_:).md)
  Tells the delegate that the document will be updated.
- [func documentViewControllerDidUpdate(TVDocumentViewController)](tvdocumentviewcontrollerdelegate/documentviewcontrollerdidupdate(_:).md)
  Tells the delegate that the document has been updated.
- [func documentViewController(TVDocumentViewController, didUpdateWithContext: [String : Any])](tvdocumentviewcontrollerdelegate/documentviewcontroller(_:didupdatewithcontext:).md)
  Tells the delegate that the document has been updated with a specified context.
### Responding to Errors
- [func documentViewController(TVDocumentViewController, didFailUpdateWithError: any Error)](tvdocumentviewcontrollerdelegate/documentviewcontroller(_:didfailupdatewitherror:).md)
  Tells the delegate that the document failed to update.
### Handling Events
- [func documentViewController(TVDocumentViewController, handleEvent: TVDocumentViewController.Event, with: TVViewElement) -> Bool](tvdocumentviewcontrollerdelegate/documentviewcontroller(_:handleevent:with:).md)
  Handles events natively from document view controllers.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any TVDocumentViewControllerDelegate)?](tvdocumentviewcontroller/delegate.md)
  The delegate for handling events in the document view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvdocumentviewcontrollerdelegate)*