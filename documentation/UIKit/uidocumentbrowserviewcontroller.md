# UIDocumentBrowserViewController

**Framework**: UIKit  
**Kind**: class

A view controller for browsing and performing actions on documents that you store locally and in the cloud.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDocumentBrowserViewController
```

## Mentions

- [Providing access to directories](providing-access-to-directories.md)
- [Customizing the browser](customizing-the-browser.md)

#### Overview

With the document browser view controller, users can easily access and view their documents in the cloud. By default, the document browser can access both the system’s local file provider and its iCloud file provider.

![A screenshot of the document browser. The On My iPad location is in a selected state on the left, and several photos and folders appear in the pane on the right.](https://docs-assets.developer.apple.com/published/294c1b3d0e1de953ec9fc339c2907ef8/media-2922157%402x.png)

The local file provider grants access to all the documents in the app’s `Documents` directory. Users can also access documents from another app’s `Documents` directory, if that app declares either the [`UISupportsDocumentBrowser`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UISupportsDocumentBrowser) key, or both the [`UIFileSharingEnabled`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIFileSharingEnabled) and [`LSSupportsOpeningDocumentsInPlace`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/LSSupportsOpeningDocumentsInPlace) keys in its `Info.plist` file. When the user opens a document from another app’s `Documents` directory, they edit the document in place, and save the changes to the other app’s `Documents` directory.

The iCloud file provider creates a folder for your app in the user’s iCloud Drive. Users can access documents from this folder, or from anywhere in their iCloud Drive. The system automatically handles access to iCloud for you, so you don’t need to enable your app’s iCloud capabilities.

Third-party storage services can also provide access to the documents they manage by implementing a File Provider extension (iOS 11 or later). For more information, see [`File Provider`](https://developer.apple.com/documentation/FileProvider).

> ❗ **Important**:  Don’t assume that the files you access are local. Users can store files in iCloud Drive, or in any cloud storage that provides a current File Provider extension. Remember that the system (or other apps) might modify the files that the document browser provides at any time. Therefore, you must coordinate your access to these files using either a [`UIDocument`](uidocument.md) subclass, or [`NSFilePresenter`](https://developer.apple.com/documentation/Foundation/NSFilePresenter) and [`NSFileCoordinator`](https://developer.apple.com/documentation/Foundation/NSFileCoordinator) objects.

## Topics

### Creating a document browser
- [Adding a document browser to your app](adding-a-document-browser-to-your-app.md)
  Give users access to their local or remote documents from within your app.
- [init(forOpening: [UTType]?)](uidocumentbrowserviewcontroller/init(foropening:).md)
  Initializes and returns a document browser view controller that can open the specified file types.
### Creating new documents
- [var activeDocumentCreationIntent: UIDocument.CreationIntent?](uidocumentbrowserviewcontroller/activedocumentcreationintent.md)
  The current intent that defines how your app creates a document.
### Responding to browser events
- [var delegate: (any UIDocumentBrowserViewControllerDelegate)?](uidocumentbrowserviewcontroller/delegate.md)
  The document browser’s delegate.
- [protocol UIDocumentBrowserViewControllerDelegate](uidocumentbrowserviewcontrollerdelegate.md)
  The protocol you implement to respond as the user interacts with the document browser.
- [func importDocument(at: URL, nextToDocumentAt: URL, mode: UIDocumentBrowserViewController.ImportMode, completionHandler: (URL?, (any Error)?) -> Void)](uidocumentbrowserviewcontroller/importdocument(at:nexttodocumentat:mode:completionhandler:).md)
  Imports a document into the same location as an existing document.
### Configuring a document browser
- [var allowsDocumentCreation: Bool](uidocumentbrowserviewcontroller/allowsdocumentcreation.md)
  A Boolean value that determines whether the document browser can create new documents.
- [var allowsPickingMultipleItems: Bool](uidocumentbrowserviewcontroller/allowspickingmultipleitems.md)
  A Boolean value that determines whether the user can select and open more than one document at a time.
- [func revealDocument(at: URL, importIfNeeded: Bool, completion: ((URL?, (any Error)?) -> Void)?)](uidocumentbrowserviewcontroller/revealdocument(at:importifneeded:completion:).md)
  Reveals, and optionally imports, the document at the provided URL.
- [var contentTypesForRecentDocuments: [UTType]](uidocumentbrowserviewcontroller/contenttypesforrecentdocuments.md)
  Content types for browsing recent documents.
### Modifying the browser’s appearance
- [var browserUserInterfaceStyle: UIDocumentBrowserViewController.BrowserUserInterfaceStyle](uidocumentbrowserviewcontroller/browseruserinterfacestyle-swift.property.md)
  The visual style for the document browser.
- [UIDocumentBrowserViewController.BrowserUserInterfaceStyle](uidocumentbrowserviewcontroller/browseruserinterfacestyle-swift.enum.md)
  Styles that define the document browser’s appearance.
- [var additionalLeadingNavigationBarButtonItems: [UIBarButtonItem]](uidocumentbrowserviewcontroller/additionalleadingnavigationbarbuttonitems.md)
  Additional bar button items that the document browser displays on the leading side of its navigation bar.
- [var additionalTrailingNavigationBarButtonItems: [UIBarButtonItem]](uidocumentbrowserviewcontroller/additionaltrailingnavigationbarbuttonitems.md)
  Additional bar button items that the document browser displays on the trailing side of its navigation bar.
- [var shouldShowFileExtensions: Bool](uidocumentbrowserviewcontroller/shouldshowfileextensions.md)
  A Boolean value that determines whether the browser always shows file extensions.
- [var localizedCreateDocumentActionTitle: String](uidocumentbrowserviewcontroller/localizedcreatedocumentactiontitle.md)
  The title for the Create Document button.
- [var defaultDocumentAspectRatio: CGFloat](uidocumentbrowserviewcontroller/defaultdocumentaspectratio.md)
  The aspect ratio for the Create Document button.
### Adding custom actions
- [var customActions: [UIDocumentBrowserAction]](uidocumentbrowserviewcontroller/customactions.md)
  Custom document browser actions.
- [class UIDocumentBrowserAction](uidocumentbrowseraction.md)
  A custom action that you can create and add to a document browser’s Edit menu or navigation bar.
### Animating transitions
- [func transitionController(forDocumentAt: URL) -> UIDocumentBrowserTransitionController](uidocumentbrowserviewcontroller/transitioncontroller(fordocumentat:).md)
  Creates a transition controller that provides the standard system-loading and segue animations for the document browser.
- [class UIDocumentBrowserTransitionController](uidocumentbrowsertransitioncontroller.md)
  An object that implements the standard loading and transition animations for a document browser.
### Renaming a document
- [func renameDocument(at: URL, proposedName: String, completionHandler: (URL?, (any Error)?) -> Void)](uidocumentbrowserviewcontroller/renamedocument(at:proposedname:completionhandler:).md)
  Renames a document at the specified URL.
### Handling errors
- [struct UIDocumentBrowserError](uidocumentbrowsererror.md)
  A structure that contains information about document browser errors.
- [UIDocumentBrowserError.Code](uidocumentbrowsererror/code.md)
  The error codes for document browser errors.
- [let UIDocumentBrowserErrorDomain: String](uidocumentbrowsererrordomain.md)
  The error domain for document browser errors.
### Deprecated symbols
- [init(forOpeningFilesWithContentTypes: [String]?)](uidocumentbrowserviewcontroller/init(foropeningfileswithcontenttypes:).md)
  Initializes and returns a document browser view controller that can open the specified file types.
- [var recentDocumentsContentTypes: [String]](uidocumentbrowserviewcontroller/recentdocumentscontenttypes.md)
  Content types for browsing recent documents.
- [var allowedContentTypes: [String]](uidocumentbrowserviewcontroller/allowedcontenttypes.md)
  The document types that the browser can open.
- [func transitionController(forDocumentURL: URL) -> UIDocumentBrowserTransitionController](uidocumentbrowserviewcontroller/transitioncontroller(fordocumenturl:).md)
  Creates a transition controller that provides the standard system-loading and segue animations for the document browser.

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
- [class UIDocumentPickerViewController](uidocumentpickerviewcontroller.md)
  A view controller that provides access to documents or destinations outside your app’s sandbox.
- [class UIDocumentInteractionController](uidocumentinteractioncontroller.md)
  A view controller that previews, opens, or prints files with a file format that your app can’t handle directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller)*