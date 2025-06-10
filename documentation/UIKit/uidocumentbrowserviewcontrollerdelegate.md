# UIDocumentBrowserViewControllerDelegate

**Framework**: UIKit  
**Kind**: protocol

The protocol you implement to respond as the user interacts with the document browser.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
protocol UIDocumentBrowserViewControllerDelegate : NSObjectProtocol
```

## Mentions

- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md)
- [Adding custom actions and activities](adding-custom-actions-and-activities.md)
- [Customizing the browser](customizing-the-browser.md)

## Topics

### Creating new documents
- [func documentBrowser(UIDocumentBrowserViewController, didRequestDocumentCreationWithHandler: (URL?, UIDocumentBrowserViewController.ImportMode) -> Void)](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didrequestdocumentcreationwithhandler:).md)
  Asks the delegate to create a new document.
- [UIDocumentBrowserViewController.ImportMode](uidocumentbrowserviewcontroller/importmode.md)
  The document browser’s import modes.
- [func documentBrowser(UIDocumentBrowserViewController, didImportDocumentAt: URL, toDestinationURL: URL)](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didimportdocumentat:todestinationurl:).md)
  Tells the delegate that a document has been successfully imported.
- [func documentBrowser(UIDocumentBrowserViewController, failedToImportDocumentAt: URL, error: (any Error)?)](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:failedtoimportdocumentat:error:).md)
  Tells the delegate that the document browser failed to import the specified document.
### Selecting documents
- [func documentBrowser(UIDocumentBrowserViewController, didPickDocumentsAt: [URL])](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didpickdocumentsat:).md)
  Tells the delegate that the user has selected one or more documents.
### Working with the browser’s activity view
- [func documentBrowser(UIDocumentBrowserViewController, willPresent: UIActivityViewController)](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:willpresent:).md)
  Tells the delegate that the document browser will display an activity view.
- [func documentBrowser(UIDocumentBrowserViewController, applicationActivitiesForDocumentURLs: [URL]) -> [UIActivity]](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:applicationactivitiesfordocumenturls:).md)
  Asks the delegate for additional activities when displaying an activity view.
### Deprecated methods
- [func documentBrowser(UIDocumentBrowserViewController, didPickDocumentURLs: [URL])](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didpickdocumenturls:).md)
  Tells the delegate that the user has selected one or more documents.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md)
  A view controller for browsing and performing actions on documents that you store locally and in the cloud.
- [var delegate: (any UIDocumentBrowserViewControllerDelegate)?](uidocumentbrowserviewcontroller/delegate.md)
  The document browser’s delegate.
- [func importDocument(at: URL, nextToDocumentAt: URL, mode: UIDocumentBrowserViewController.ImportMode, completionHandler: (URL?, (any Error)?) -> Void)](uidocumentbrowserviewcontroller/importdocument(at:nexttodocumentat:mode:completionhandler:).md)
  Imports a document into the same location as an existing document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontrollerdelegate)*