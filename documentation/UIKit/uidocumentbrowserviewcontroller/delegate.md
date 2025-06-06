# delegate

**Framework**: UIKit  
**Kind**: property

The document browser’s delegate.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIDocumentBrowserViewControllerDelegate)? { get set }
```

#### Discussion

The delegate object must implement the [`UIDocumentBrowserViewControllerDelegate`](uidocumentbrowserviewcontrollerdelegate.md) protocol.

## See Also

- [protocol UIDocumentBrowserViewControllerDelegate](uidocumentbrowserviewcontrollerdelegate.md)
  The protocol you implement to respond as the user interacts with the document browser.
- [func importDocument(at: URL, nextToDocumentAt: URL, mode: UIDocumentBrowserViewController.ImportMode, completionHandler: (URL?, (any Error)?) -> Void)](uidocumentbrowserviewcontroller/importdocument(at:nexttodocumentat:mode:completionhandler:).md)
  Imports a document into the same location as an existing document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/delegate)*