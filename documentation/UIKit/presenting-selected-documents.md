# Presenting selected documents

**Framework**: UIKit  
**Role**: Article

Display user-selected documents over your browser view controller.

## Overview

When the user selects one or more documents in the browser view controller, the system calls your delegate’s [`documentBrowser(_:didPickDocumentURLs:)`](./uidocumentbrowserviewcontrollerdelegate/documentbrowser%28_,didpickdocumenturls%29.md) method.

### Display documents with document view controllers

In your implementation of the [`documentBrowser(_:didPickDocumentURLs:)`](./uidocumentbrowserviewcontrollerdelegate/documentbrowser%28_,didpickdocumenturls%29.md) method, modally present a view controller to display the selected documents by calling the browser’s [`present(_:animated:completion:)`](./uiviewcontroller/present%28_,animated,completion%29.md) method.

The document view should fill the entire screen, but it can have its own split view controller, navigation controller, or tab controller, as appropriate. It remains onscreen as long as the user is interacting with the documents. To return to the browser, dismiss the document view controller.

## See Also

### Configuration
- [Setting up a document browser app](./setting-up-a-document-browser-app.md)
  Add a document browser view controller to your app.
- [Enabling document sharing](./enabling-document-sharing.md)
  Give users the ability to import and export documents from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/presenting-selected-documents)*