# transitionController(forDocumentURL:)

**Framework**: UIKit  
**Kind**: method

Creates a transition controller that provides the standard system-loading and segue animations for the document browser.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func transitionController(forDocumentURL documentURL: URL) -> UIDocumentBrowserTransitionController
```

#### Return Value

Returns a newly instantiated transition controller. Its [`loadingProgress`](uidocumentbrowsertransitioncontroller/loadingprogress.md) and [`targetView`](uidocumentbrowsertransitioncontroller/targetview.md) properties are both set to `nil`.

#### Discussion

For the animations to function properly, you must maintain a strong reference to the transition controller until all the animation sequences are complete.

For more about using the transition controller, see [`UIDocumentBrowserTransitionController`](uidocumentbrowsertransitioncontroller.md).

## Parameters

- `documentURL`: The URL of a document. Only use URLs provided by the document browser (for example, URLs passed to the delegate’s  method’s completion block).

## See Also

- [init(forOpeningFilesWithContentTypes: [String]?)](uidocumentbrowserviewcontroller/init(foropeningfileswithcontenttypes:).md)
  Initializes and returns a document browser view controller that can open the specified file types.
- [var recentDocumentsContentTypes: [String]](uidocumentbrowserviewcontroller/recentdocumentscontenttypes.md)
  Content types for browsing recent documents.
- [var allowedContentTypes: [String]](uidocumentbrowserviewcontroller/allowedcontenttypes.md)
  The document types that the browser can open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/transitioncontroller(fordocumenturl:))*