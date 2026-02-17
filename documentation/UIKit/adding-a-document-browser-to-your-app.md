# Adding a document browser to your app

**Framework**: UIKit

Give people access to their local or remote documents from within your app.

#### Overview

When your app’s main purpose is browsing and working with documents, use a document browser view controller as the root of your app’s view hierarchy. When someone selects a document, you present its view controller modally from your document browser.

> ❗ **Important**:  Always assign [`UIDocumentBrowserViewController`](uidocumentbrowserviewcontroller.md) as your app’s root view controller. UIKit doesn’t support placing the document browser in a navigation controller, tab bar, split view, or modal presentation. If you want to present a document browser from another location in your view hierarchy, use a [`UIDocumentPickerViewController`](uidocumentpickerviewcontroller.md) instead.

The browser automatically gives people the option to share documents using the Share button or a drag-and-drop action. It also provides a standard interface for browsing and managing documents.

You set the type of documents that someone can select when the browser is first created. You can also set the browser’s appearance, modify its behaviors, and add custom actions.

## Topics

### Configuration
- [Setting up a document browser app](setting-up-a-document-browser-app.md)
  Add a document browser view controller to your app.
- [Presenting selected documents](presenting-selected-documents.md)
  Display user-selected documents over your browser view controller.
- [Enabling document sharing](enabling-document-sharing.md)
  Give users the ability to import and export documents from your app.
### Customization
- [Customizing the document browser](customizing-the-browser.md)
  Customize the document browser’s look and behavior.
- [Adding custom actions and activities](adding-custom-actions-and-activities.md)
  Add custom document browser actions, activities, and bar items.

## See Also

- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md)
  Add unique elements to your app’s document launch scene.
- [Providing access to directories](providing-access-to-directories.md)
  Use a document picker to access the content of a directory outside your app’s container.
- [Building an app with a document browser](building-an-app-with-a-document-browser.md)
  Provide access to on-device and cloud files by adding a document browser to your app.
- [Building a document browser app for custom file formats](building-a-document-browser-app-for-custom-file-formats.md)
  Implement a custom document file format to manage user interactions with files on different cloud storage providers.
- [class UIDocumentViewController](uidocumentviewcontroller.md)
  A view controller that manages and presents a document stored locally or in the cloud.
- [class UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md)
  A view controller for browsing and performing actions on documents that you store locally and in the cloud.
- [class UIDocumentPickerViewController](uidocumentpickerviewcontroller.md)
  A view controller that provides access to documents or destinations outside your app’s sandbox.
- [class UIDocumentInteractionController](uidocumentinteractioncontroller.md)
  A view controller that previews, opens, or prints files with a file format that your app can’t handle directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/adding-a-document-browser-to-your-app)*