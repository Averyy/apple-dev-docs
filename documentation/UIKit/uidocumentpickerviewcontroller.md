# UIDocumentPickerViewController

**Framework**: UIKit  
**Kind**: class

A view controller that provides access to documents or destinations outside your app’s sandbox.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDocumentPickerViewController
```

## Mentions

- [Providing access to directories](providing-access-to-directories.md)

#### Overview

Use a document picker view controller to select a document to open or export, and optionally copy. Don’t copy the document if you can avoid it. The document picker operates in two modes:

- Open a document. The user selects a document. The document picker provides access to the document, and the user can edit the document in place. Optionally, you can specify that the document picker makes a copy of the document, leaving the original unchanged.
- Export a local document. The user selects a destination. The document picker moves the document, and the user can access it and edit it in place. Optionally, you can specify that the document picker makes a copy of the document, leaving the original unchanged.

##### Work with External Documents

Both the open and export operations grant access to documents outside your app’s sandbox. This access gives users an unprecedented amount of flexibility when working with their documents. However, it also adds a layer of complexity to your file handling. External documents have the following additional requirements:

- The open and move operations provide security-scoped URLs for all external documents. Call the [`startAccessingSecurityScopedResource()`](https://developer.apple.com/documentation/Foundation/NSURL/startAccessingSecurityScopedResource()) method to access or bookmark these documents, and the [`stopAccessingSecurityScopedResource()`](https://developer.apple.com/documentation/Foundation/NSURL/stopAccessingSecurityScopedResource()) method to release them. If you’re using a `UIDocument` subclass to manage your document, it automatically manages the security-scoped URL for you.
- Always use file coordinators (see [`NSFileCoordinator`](https://developer.apple.com/documentation/Foundation/NSFileCoordinator)) to read and write to external documents.
- Always use a file presenter (see [`NSFilePresenter`](https://developer.apple.com/documentation/Foundation/NSFilePresenter)) when displaying the contents of an external document.
- Don’t save URLs that the open and move operations provide. You can, however, save a bookmark to these URLs after calling [`startAccessingSecurityScopedResource()`](https://developer.apple.com/documentation/Foundation/NSURL/startAccessingSecurityScopedResource()) to ensure you have access. Call the [`bookmarkData(options:includingResourceValuesForKeys:relativeTo:)`](https://developer.apple.com/documentation/Foundation/NSURL/bookmarkData(options:includingResourceValuesForKeys:relativeTo:)) method and pass in the [`withSecurityScope`](https://developer.apple.com/documentation/Foundation/NSURL/BookmarkCreationOptions/withSecurityScope) option, creating a bookmark that contains a security-scoped URL.

For more information about working with external documents, see [`Providing access to directories`](providing-access-to-directories.md) and [`Adding a document browser to your app`](adding-a-document-browser-to-your-app.md).

## Topics

### Creating a document picker
- [init?(coder: NSCoder)](uidocumentpickerviewcontroller/init(coder:).md)
  Returns an initialized object from data in a specified unarchiver.
- [convenience init(forExporting: [URL])](uidocumentpickerviewcontroller/init(forexporting:).md)
  Creates and returns a document picker that can export the types of documents you specify.
- [init(forExporting: [URL], asCopy: Bool)](uidocumentpickerviewcontroller/init(forexporting:ascopy:).md)
  Creates and returns a document picker that can export or copy the types of documents you specify.
- [convenience init(forOpeningContentTypes: [UTType])](uidocumentpickerviewcontroller/init(foropeningcontenttypes:).md)
  Creates and returns a document picker that can open the types of documents you specify.
- [init(forOpeningContentTypes: [UTType], asCopy: Bool)](uidocumentpickerviewcontroller/init(foropeningcontenttypes:ascopy:).md)
  Creates and returns a document picker that can open or copy the types of documents you specify.
### Getting the user-selected document
- [var delegate: (any UIDocumentPickerDelegate)?](uidocumentpickerviewcontroller/delegate.md)
  An object that acts as the delegate of the view controller.
- [protocol UIDocumentPickerDelegate](uidocumentpickerdelegate.md)
  A set of methods for tracking when the user selects a document or destination, or cancels the operation.
- [var allowsMultipleSelection: Bool](uidocumentpickerviewcontroller/allowsmultipleselection.md)
  A Boolean value that determines whether the user can select more than one document at a time.
- [var directoryURL: URL?](uidocumentpickerviewcontroller/directoryurl.md)
  The initial directory that the document picker displays.
### Configuring a document picker
- [var shouldShowFileExtensions: Bool](uidocumentpickerviewcontroller/shouldshowfileextensions.md)
  A Boolean value that determines whether the browser always shows file extensions.
- [var documentPickerMode: UIDocumentPickerMode](uidocumentpickerviewcontroller/documentpickermode.md)
  The type of file transfer operation that the document picker uses.
- [enum UIDocumentPickerMode](uidocumentpickermode.md)
  Modes that define the type of file transfer operation that the document picker uses.
### Deprecated
- [init(documentTypes: [String], in: UIDocumentPickerMode)](uidocumentpickerviewcontroller/init(documenttypes:in:).md)
  Creates and returns a document picker that can open or copy the specified file types.
- [init(url: URL, in: UIDocumentPickerMode)](uidocumentpickerviewcontroller/init(url:in:).md)
  Initializes and returns a document picker that can export or copy the specified document.
- [init(urls: [URL], in: UIDocumentPickerMode)](uidocumentpickerviewcontroller/init(urls:in:).md)
  Creates and returns a document picker that can export or move the specified documents.

## Relationships

### Inherits From
- [UIViewController](uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIStateRestoring](uistaterestoring.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

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
- [class UIDocumentInteractionController](uidocumentinteractioncontroller.md)
  A view controller that previews, opens, or prints files with a file format that your app can’t handle directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller)*