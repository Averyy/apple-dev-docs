# transitionController(forDocumentURL:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Creates a transition controller that provides the standard system-loading and segue animations for the document browser.

**Availability**:
- iOS 11.0+ - Deprecated in 12.0
- iPadOS 11.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`transitionController(forDocumentAt:)`](./transitioncontroller%28fordocumentat%29.md) instead.

## Declaration

```swift
func transitionController(forDocumentURL documentURL: URL) -> UIDocumentBrowserTransitionController
```

```objc
- (UIDocumentBrowserTransitionController *) transitionControllerForDocumentURL:(NSURL *) documentURL;
```

#### Return Value

Returns a newly instantiated transition controller. Its [`loadingProgress`](../uidocumentbrowsertransitioncontroller/loadingprogress.md) and [`targetView`](../uidocumentbrowsertransitioncontroller/targetview.md) properties are both set to `nil`.

#### Discussion

For the animations to function properly, you must maintain a strong reference to the transition controller until all the animation sequences are complete.

For more about using the transition controller, see [`UIDocumentBrowserTransitionController`](../uidocumentbrowsertransitioncontroller.md).

## Parameters

- `documentURL`: The URL of a document. Only use URLs provided by the document browser (for example, URLs passed to the delegate’s [`documentBrowser(_:didRequestDocumentCreationWithHandler:)`](../uidocumentbrowserviewcontrollerdelegate/documentbrowser%28_,didrequestdocumentcreationwithhandler%29.md)method’s completion block).

## See Also

### Deprecated
- [init(forOpeningFilesWithContentTypes: [String]?)](./init%28foropeningfileswithcontenttypes%29.md)
  Initializes and returns a document browser view controller that can open the specified file types.
- [var recentDocumentsContentTypes: [String]](./recentdocumentscontenttypes.md)
  Content types for browsing recent documents.
- [var allowedContentTypes: [String]](./allowedcontenttypes.md)
  The document types that the browser can open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/transitioncontroller(fordocumenturl:))*