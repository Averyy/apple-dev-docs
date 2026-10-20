# documentBrowser(_:didImportDocumentAt:toDestinationURL:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) documentBrowser:(UIDocumentBrowserViewController *) controller didImportDocumentAtURL:(NSURL *) sourceURL toDestinationURL:(NSURL *) destinationURL;
```

## Mentions

- [Enabling document sharing](../enabling-document-sharing.md)

#### Discussion

To open the document as soon as it’s imported:

1. Open a new [`UIDocument`](../uidocument.md) subclass for the document (or use a file presenter and file coordination to access the document).
2. Create a view controller to display the document.
3. Present that view controller modally.

## Parameters

- `controller`: The document browser that performed the import action.
- `sourceURL`: The document’s original URL.
- `destinationURL`: The document’s URL after the import.

## See Also

### Creating new documents
- [func documentBrowser(UIDocumentBrowserViewController, didRequestDocumentCreationWithHandler: (URL?, UIDocumentBrowserViewController.ImportMode) -> Void)](./documentbrowser%28_,didrequestdocumentcreationwithhandler%29.md)
  Asks the delegate to create a new document.
- [UIDocumentBrowserViewController.ImportMode](../uidocumentbrowserviewcontroller/importmode.md)
  The document browser’s import modes.
- [func documentBrowser(UIDocumentBrowserViewController, failedToImportDocumentAt: URL, error: (any Error)?)](./documentbrowser%28_,failedtoimportdocumentat,error%29.md)
  Tells the delegate that the document browser failed to import the specified document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didimportdocumentat:todestinationurl:))*