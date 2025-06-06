# documentBrowser(_:didImportDocumentAt:toDestinationURL:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that a document has been successfully imported.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func documentBrowser(_ controller: UIDocumentBrowserViewController, didImportDocumentAt sourceURL: URL, toDestinationURL destinationURL: URL)
```

## Mentions

- [Enabling document sharing](enabling-document-sharing.md)

#### Discussion

To open the document as soon as it’s imported:

1. Open a new [`UIDocument`](uidocument.md) subclass for the document (or use a file presenter and file coordination to access the document).
2. Create a view controller to display the document.
3. Present that view controller modally.

## Parameters

- `controller`: The document browser that performed the import action.
- `sourceURL`: The document’s original URL.
- `destinationURL`: The document’s URL after the import.

## See Also

- [func documentBrowser(UIDocumentBrowserViewController, didRequestDocumentCreationWithHandler: (URL?, UIDocumentBrowserViewController.ImportMode) -> Void)](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didrequestdocumentcreationwithhandler:).md)
  Asks the delegate to create a new document.
- [UIDocumentBrowserViewController.ImportMode](uidocumentbrowserviewcontroller/importmode.md)
  The document browser’s import modes.
- [func documentBrowser(UIDocumentBrowserViewController, failedToImportDocumentAt: URL, error: (any Error)?)](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:failedtoimportdocumentat:error:).md)
  Tells the delegate that the document browser failed to import the specified document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didimportdocumentat:todestinationurl:))*