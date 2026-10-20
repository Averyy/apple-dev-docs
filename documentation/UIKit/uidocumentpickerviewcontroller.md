# UIDocumentPickerViewController

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIDocumentPickerViewController : UIViewController
```

## Mentions

- [Providing access to directories](./providing-access-to-directories.md)

#### Overview

Use a document picker view controller to select a document to open or export, and optionally copy. Don’t copy the document if you can avoid it. The document picker operates in two modes:

- Open a document. The user selects a document. The document picker provides access to the document, and the user can edit the document in place. Optionally, you can specify that the document picker makes a copy of the document, leaving the original unchanged.
- Export a local document. The user selects a destination. The document picker moves the document, and the user can access it and edit it in place. Optionally, you can specify that the document picker makes a copy of the document, leaving the original unchanged.

##### Work with external documents

Both the open and export operations grant access to documents outside your app’s sandbox. This access gives users an unprecedented amount of flexibility when working with their documents. However, it also adds a layer of complexity to your file handling. External documents have the following additional requirements:

- The open and move operations provide security-scoped URLs for all external documents. Call the [`startAccessingSecurityScopedResource()`](../Foundation/nsurl/startaccessingsecurityscopedresource%28%29.md) method to access or bookmark these documents, and the [`stopAccessingSecurityScopedResource()`](../Foundation/nsurl/stopaccessingsecurityscopedresource%28%29.md) method to release them. If you’re using a `UIDocument` subclass to manage your document, it automatically manages the security-scoped URL for you.
- Always use file coordinators (see [`NSFileCoordinator`](../Foundation/nsfilecoordinator.md)) to read and write to external documents.
- Always use a file presenter (see [`NSFilePresenter`](../Foundation/nsfilepresenter.md)) when displaying the contents of an external document.
- Don’t save URLs that the open and move operations provide. You can, however, save a bookmark to these URLs after calling [`startAccessingSecurityScopedResource()`](../Foundation/nsurl/startaccessingsecurityscopedresource%28%29.md) to ensure you have access. Call the [`bookmarkData(options:includingResourceValuesForKeys:relativeTo:)`](../Foundation/nsurl/bookmarkdata%28options,includingresourcevaluesforkeys,relativeto%29.md) method and pass in the [`withSecurityScope`](../Foundation/nsurl/bookmarkcreationoptions/withsecurityscope.md) option, creating a bookmark that contains a security-scoped URL.

For more information about working with external documents, see [Providing access to directories](./providing-access-to-directories.md) and [Adding a document browser to your app](./adding-a-document-browser-to-your-app.md).

## Topics

### Creating a document picker
- [init?(coder: NSCoder)](./uidocumentpickerviewcontroller/init%28coder%29.md)
  Returns an initialized object from data in a specified unarchiver.
- [convenience init(forExporting: [URL])](./uidocumentpickerviewcontroller/init%28forexporting%29.md)
  Creates and returns a document picker that can export the types of documents you specify.
- [init(forExporting: [URL], asCopy: Bool)](./uidocumentpickerviewcontroller/init%28forexporting,ascopy%29.md)
  Creates and returns a document picker that can export or copy the types of documents you specify.
- [convenience init(forOpeningContentTypes: [UTType])](./uidocumentpickerviewcontroller/init%28foropeningcontenttypes%29.md)
  Creates and returns a document picker that can open the types of documents you specify.
- [init(forOpeningContentTypes: [UTType], asCopy: Bool)](./uidocumentpickerviewcontroller/init%28foropeningcontenttypes,ascopy%29.md)
  Creates and returns a document picker that can open or copy the types of documents you specify.
### Getting the user-selected document
- [var delegate: (any UIDocumentPickerDelegate)?](./uidocumentpickerviewcontroller/delegate.md)
  An object that acts as the delegate of the view controller.
- [protocol UIDocumentPickerDelegate](./uidocumentpickerdelegate.md)
  A set of methods for tracking when the user selects a document or destination, or cancels the operation.
- [var allowsMultipleSelection: Bool](./uidocumentpickerviewcontroller/allowsmultipleselection.md)
  A Boolean value that determines whether the user can select more than one document at a time.
- [var directoryURL: URL?](./uidocumentpickerviewcontroller/directoryurl.md)
  The initial directory that the document picker displays.
### Configuring a document picker
- [var shouldShowFileExtensions: Bool](./uidocumentpickerviewcontroller/shouldshowfileextensions.md)
  A Boolean value that determines whether the browser always shows file extensions.
### Deprecated
- [Deprecated symbols](./uidocumentpickerviewcontroller-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.
### Initializers
- [convenience init(forExportingURLs: [URL])](./uidocumentpickerviewcontroller/init%28forexportingurls%29.md)
- [init(forExportingURLs: [URL], asCopy: Bool)](./uidocumentpickerviewcontroller/init%28forexportingurls,ascopy%29.md)

## Relationships

### Inherits From
- [UIViewController](./uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](./uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](./uiappearancecontainer.md)
- [UIContentContainer](./uicontentcontainer.md)
- [UIFocusEnvironment](./uifocusenvironment.md)
- [UIPasteConfigurationSupporting](./uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](./uiresponderstandardeditactions.md)
- [UIStateRestoring](./uistaterestoring.md)
- [UITraitChangeObservable](./uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](./uitraitenvironment.md)
- [UIUserActivityRestoring](./uiuseractivityrestoring.md)

## See Also

### Documents and directories
- [Customizing a document-based app’s launch experience](./customizing-a-document-based-app-s-launch-experience.md)
  Add unique elements to your app’s document launch scene.
- [Adding a document browser to your app](./adding-a-document-browser-to-your-app.md)
  Give people access to their local or remote documents from within your app.
- [Providing access to directories](./providing-access-to-directories.md)
  Use a document picker to access the content of a directory outside your app’s container.
- [Building an app with a document browser](./building-an-app-with-a-document-browser.md)
  Provide access to on-device and cloud files by adding a document browser to your app.
- [Building a document browser app for custom file formats](./building-a-document-browser-app-for-custom-file-formats.md)
  Implement a custom document file format to manage user interactions with files on different cloud storage providers.
- [class UIDocumentViewController](./uidocumentviewcontroller.md)
  A view controller that manages and presents a document stored locally or in the cloud.
- [class UIDocumentBrowserViewController](./uidocumentbrowserviewcontroller.md)
  A view controller for browsing and performing actions on documents that you store locally and in the cloud.
- [class UIDocumentInteractionController](./uidocumentinteractioncontroller.md)
  A view controller that previews, opens, or prints files with a file format that your app can’t handle directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller)*