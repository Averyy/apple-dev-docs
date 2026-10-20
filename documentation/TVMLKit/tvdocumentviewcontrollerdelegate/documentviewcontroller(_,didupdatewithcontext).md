# documentViewController(_:didUpdateWithContext:)

**Framework**: TVMLKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the document has been updated with a specified context.

**Availability**:
- tvOS 13.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
optional func documentViewController(_ documentViewController: TVDocumentViewController, didUpdateWithContext context: [String : Any])
```

```objc
- (void) documentViewController:(TVDocumentViewController *) documentViewController didUpdateWithContext:(NSDictionary<NSString *,id> *) context;
```

## See Also

### Managing Document Updates
- [func documentViewControllerWillUpdate(TVDocumentViewController)](./documentviewcontrollerwillupdate%28_%29.md)
  Tells the delegate that the document will be updated.
- [func documentViewControllerDidUpdate(TVDocumentViewController)](./documentviewcontrollerdidupdate%28_%29.md)
  Tells the delegate that the document has been updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvdocumentviewcontrollerdelegate/documentviewcontroller(_:didupdatewithcontext:))*