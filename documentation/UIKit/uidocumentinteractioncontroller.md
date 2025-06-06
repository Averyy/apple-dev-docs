# UIDocumentInteractionController

**Framework**: UIKit  
**Kind**: class

A view controller that previews, opens, or prints files with a file format that your app can’t handle directly.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDocumentInteractionController
```

#### Overview

Use this class to present an appropriate user interface for previewing, opening, copying, or printing a specified file. For example, an email program might use this class to allow the user to preview attachments and open them in other apps.

After presenting its user interface, a document interaction controller handles all interactions needed to support file preview and menu display.

You can also use the delegate to participate in interactions occurring within the presented interface. For example, the delegate is notified when a file is about to be handed off to another application for opening. For a complete description of the methods you can implement in your delegate, see [`UIDocumentInteractionControllerDelegate`](uidocumentinteractioncontrollerdelegate.md).

## Topics

### Creating the document interaction controller
- [init(url: URL)](uidocumentinteractioncontroller/init(url:).md)
  Creates a document interaction controller with the specified URL.
### Handling document-related interactions
- [var delegate: (any UIDocumentInteractionControllerDelegate)?](uidocumentinteractioncontroller/delegate.md)
  The delegate you want to receive document interaction notifications.
- [protocol UIDocumentInteractionControllerDelegate](uidocumentinteractioncontrollerdelegate.md)
  A set of methods you can implement to respond to messages from a document interaction controller.
### Presenting and dismissing a document preview
- [func presentPreview(animated: Bool) -> Bool](uidocumentinteractioncontroller/presentpreview(animated:).md)
  Displays a full-screen preview of the target document.
- [func dismissPreview(animated: Bool)](uidocumentinteractioncontroller/dismisspreview(animated:).md)
  Dismisses the currently active document preview.
### Presenting and dismissing menus
- [func presentOptionsMenu(from: CGRect, in: UIView, animated: Bool) -> Bool](uidocumentinteractioncontroller/presentoptionsmenu(from:in:animated:).md)
  Displays an options menu and anchors it to the specified location in the view.
- [func presentOptionsMenu(from: UIBarButtonItem, animated: Bool) -> Bool](uidocumentinteractioncontroller/presentoptionsmenu(from:animated:).md)
  Displays an options menu and anchors it to the specified bar button item.
- [func presentOpenInMenu(from: CGRect, in: UIView, animated: Bool) -> Bool](uidocumentinteractioncontroller/presentopeninmenu(from:in:animated:).md)
  Displays a menu for opening the document and anchors that menu to the specified view.
- [func presentOpenInMenu(from: UIBarButtonItem, animated: Bool) -> Bool](uidocumentinteractioncontroller/presentopeninmenu(from:animated:).md)
  Displays a menu for opening the document and anchors that menu to the specified bar button item.
- [func dismissMenu(animated: Bool)](uidocumentinteractioncontroller/dismissmenu(animated:).md)
  Dismisses the currently active menu.
### Accessing the target document’s attributes
- [var url: URL?](uidocumentinteractioncontroller/url.md)
  The URL identifying the target file on the local filesystem.
- [var uti: String?](uidocumentinteractioncontroller/uti.md)
  The type of the target file.
- [var name: String?](uidocumentinteractioncontroller/name.md)
  The name of the target file.
- [var icons: [UIImage]](uidocumentinteractioncontroller/icons.md)
  The images associated with the target file.
- [var annotation: Any?](uidocumentinteractioncontroller/annotation.md)
  Custom property list information for the target file.
### Accessing the controller attributes
- [var gestureRecognizers: [UIGestureRecognizer]](uidocumentinteractioncontroller/gesturerecognizers.md)
  The system-supplied gesture recognizers for presenting a document interaction controller.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIActionSheetDelegate](uiactionsheetdelegate.md)

## See Also

- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md)
  Add unique elements to your app’s document launch scene.
- [Adding a document browser to your app](adding-a-document-browser-to-your-app.md)
  Give users access to their local or remote documents from within your app.
- [Providing access to directories](providing-access-to-directories.md)
  Use a document picker to access the content of a directory outside your app’s container.
- [Building a document browser-based app](building-a-document-browser-based-app.md)
  Use a document browser to provide access to the user’s text files.
- [Building a document browser app for custom file formats](building-a-document-browser-app-for-custom-file-formats.md)
  Implement a custom document file format to manage user interactions with files on different cloud storage providers.
- [class UIDocumentViewController](uidocumentviewcontroller.md)
  A view controller that manages and presents a document stored locally or in the cloud.
- [class UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md)
  A view controller for browsing and performing actions on documents that you store locally and in the cloud.
- [class UIDocumentPickerViewController](uidocumentpickerviewcontroller.md)
  A view controller that provides access to documents or destinations outside your app’s sandbox.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller)*