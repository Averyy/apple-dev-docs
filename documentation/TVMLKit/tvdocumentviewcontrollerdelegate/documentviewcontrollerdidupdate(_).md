# documentViewControllerDidUpdate(_:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the document has been updated.

**Availability**:
- tvOS 13.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
optional func documentViewControllerDidUpdate(_ documentViewController: TVDocumentViewController)
```

```objc
- (void) documentViewControllerDidUpdate:(TVDocumentViewController *) documentViewController;
```

## See Also

### Managing Document Updates
- [func documentViewControllerWillUpdate(TVDocumentViewController)](./documentviewcontrollerwillupdate%28_%29.md)
  Tells the delegate that the document will be updated.
- [func documentViewController(TVDocumentViewController, didUpdateWithContext: [String : Any])](./documentviewcontroller%28_,didupdatewithcontext%29.md)
  Tells the delegate that the document has been updated with a specified context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvdocumentviewcontrollerdelegate/documentviewcontrollerdidupdate(_:))*