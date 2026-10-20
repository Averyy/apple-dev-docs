# NSDocumentController

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that manages an app’s documents.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
class NSDocumentController
```

```objc
@interface NSDocumentController : NSObject
```

#### Overview

As the first-responder target of New and Open menu commands, [`NSDocumentController`](./nsdocumentcontroller.md) creates and opens documents and tracks them throughout a session of the app. When opening documents, a document controller runs and manages the modal Open panel. [`NSDocumentController`](./nsdocumentcontroller.md) objects also maintain and manage the mappings of document types, extensions, and [`NSDocument`](./nsdocument.md) subclasses as specified in the [CFBundleDocumentTypes](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-101685) property loaded from the information property list (`Info.plist`).

You can use various [`NSDocumentController`](./nsdocumentcontroller.md) methods to get a list of the current documents, get the current document (which is the document whose window is currently key), get documents based on a given filename or window, and find out about a document’s extension, type, display name, and document class.

In some situations, it’s worthwhile to subclass [`NSDocumentController`](./nsdocumentcontroller.md) in non-[`NSDocument`](./nsdocument.md)-based apps to get some of its features. For example, the [`NSDocumentController`](./nsdocumentcontroller.md) management of the Open Recent menu is useful in apps that don’t use subclasses of [`NSDocument`](./nsdocument.md).

## Topics

### Obtaining the Shared Document Controller
- [class var shared: NSDocumentController](./nsdocumentcontroller/shared.md)
  Returns the shared `NSDocumentController` instance.
### Initializing a New NSDocumentController
- [init()](./nsdocumentcontroller/init%28%29.md)
  This method is the designated initializer for `NSDocumentController`.
- [init?(coder: NSCoder)](./nsdocumentcontroller/init%28coder%29.md)
  This method initializes a new NSDocumentController from the coder.
### Creating and Opening Documents
- [func document(for: URL) -> NSDocument?](./nsdocumentcontroller/document%28for%29-i5zi.md)
  Returns, for a given URL, the open document whose file or file package is located by the URL, or `nil` if there is no such open document.
- [func duplicateDocument(withContentsOf: URL, copying: Bool, displayName: String?) throws -> NSDocument](./nsdocumentcontroller/duplicatedocument%28withcontentsof,copying,displayname%29.md)
  Creates a new document by reading the contents for the document from another URL, presents its user interface, and returns the document if successful.
- [func openDocument(withContentsOf: URL, display: Bool, completionHandler: (NSDocument?, Bool, (any Error)?) -> Void)](./nsdocumentcontroller/opendocument%28withcontentsof,display,completionhandler%29.md)
  Opens a document located by a URL, optionally presents its user interface, and calls the passed-in completion handler.
- [func openUntitledDocumentAndDisplay(Bool) throws -> NSDocument](./nsdocumentcontroller/openuntitleddocumentanddisplay%28_%29.md)
  Creates a new untitled document, presents its user interface if `displayDocument` is `true`, and returns the document if successful.
- [func makeDocument(for: URL?, withContentsOf: URL, ofType: String) throws -> NSDocument](./nsdocumentcontroller/makedocument%28for,withcontentsof,oftype%29.md)
  Instantiates a document located by a URL, of a specified type, but by reading the contents for the document from another URL, and returns it if successful.
- [func makeDocument(withContentsOf: URL, ofType: String) throws -> NSDocument](./nsdocumentcontroller/makedocument%28withcontentsof,oftype%29.md)
  Instantiates a document located by a URL, of a specified type, and returns it if successful.
- [func makeUntitledDocument(ofType: String) throws -> NSDocument](./nsdocumentcontroller/makeuntitleddocument%28oftype%29.md)
  Instantiates a new untitled document of the specified type and returns it if successful.
- [func reopenDocument(for: URL?, withContentsOf: URL, display: Bool, completionHandler: (NSDocument?, Bool, (any Error)?) -> Void)](./nsdocumentcontroller/reopendocument%28for,withcontentsof,display,completionhandler%29.md)
  Reopens a document, optionally located by a URL, by reading the contents for the document from another URL, optionally presents its user interface, and calls the passed-in completion handler.
### Managing Documents
- [var documents: [NSDocument]](./nsdocumentcontroller/documents.md)
  The document objects managed by the receiver.
- [func addDocument(NSDocument)](./nsdocumentcontroller/adddocument%28_%29.md)
  Adds the given document to the list of open documents.
- [var currentDocument: NSDocument?](./nsdocumentcontroller/currentdocument.md)
  The document object associated with the main window.
- [func document(for: NSWindow) -> NSDocument?](./nsdocumentcontroller/document%28for%29-a5yd.md)
  Returns the document object whose window controller owns a specified window.
- [var hasEditedDocuments: Bool](./nsdocumentcontroller/hasediteddocuments.md)
  A Boolean value indicating whether the receiver has any documents with unsaved changes.
- [func removeDocument(NSDocument)](./nsdocumentcontroller/removedocument%28_%29.md)
  Removes the given document from the list of open documents.
### Managing Document Types
- [var documentClassNames: [String]](./nsdocumentcontroller/documentclassnames.md)
  An array of strings representing the custom document classes supported by this app.
- [var defaultType: String?](./nsdocumentcontroller/defaulttype.md)
  Returns the name of the document type that should be used when creating new documents.
- [func documentClass(forType: String) -> AnyClass?](./nsdocumentcontroller/documentclass%28fortype%29.md)
  Returns the `NSDocument` subclass associated with a given document type.
- [func displayName(forType: String) -> String?](./nsdocumentcontroller/displayname%28fortype%29.md)
  Returns the descriptive name for the specified document type, which is used in the File Format pop-up menu of the Save As dialog.
- [func typeForContents(of: URL) throws -> String](./nsdocumentcontroller/typeforcontents%28of%29.md)
  Returns, for a specified URL, the document type identifier to use when opening the document at that location, if successful.
### Autosaving
- [var autosavingDelay: TimeInterval](./nsdocumentcontroller/autosavingdelay.md)
  The time interval (in seconds) for periodic autosaving.
### Closing Documents
- [func closeAllDocuments(withDelegate: Any?, didCloseAllSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)](./nsdocumentcontroller/closealldocuments%28withdelegate,didcloseallselector,contextinfo%29.md)
  Iterates through all the open documents and tries to close them one by one using the specified delegate.
- [func reviewUnsavedDocuments(withAlertTitle: String?, cancellable: Bool, delegate: Any?, didReviewAllSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)](./nsdocumentcontroller/reviewunsaveddocuments%28withalerttitle,cancellable,delegate,didreviewallselector,contextinfo%29.md)
  Displays an alert asking if the user wants to review unsaved documents, quit regardless of unsaved documents, or cancel the save operation.
### Responding to Action Messages
- [func newDocument(Any?)](./nsdocumentcontroller/newdocument%28_%29.md)
  An action method called by the New menu command, this method creates a new `NSDocument` object and adds it to the list of such objects managed by the document controller.
- [func openDocument(Any?)](./nsdocumentcontroller/opendocument%28_%29.md)
  An action method called by the Open menu command, it runs the modal Open panel and, based on the selected filenames, creates one or more `NSDocument` objects from the contents of the files.
- [func saveAllDocuments(Any?)](./nsdocumentcontroller/savealldocuments%28_%29.md)
  As the action method called by the Save All command, saves all open documents of the application that need to be saved.
### Managing the Open Dialog
- [func beginOpenPanel(completionHandler: ([URL]?) -> Void)](./nsdocumentcontroller/beginopenpanel%28completionhandler%29.md)
  Presents an Open dialog and delivers the results to a completion handler as an array of URLs for the chosen files, or nil.
- [func beginOpenPanel(NSOpenPanel, forTypes: [String]?, completionHandler: (Int) -> Void)](./nsdocumentcontroller/beginopenpanel%28_,fortypes,completionhandler%29.md)
  Presents a nonmodal Open dialog that displays files you can open from a list of UTIs.
- [func runModalOpenPanel(NSOpenPanel, forTypes: [String]?) -> Int](./nsdocumentcontroller/runmodalopenpanel%28_,fortypes%29.md)
  Presents a modal Open dialog and limits selection to specific file types.
- [var currentDirectory: String?](./nsdocumentcontroller/currentdirectory.md)
  The directory path to use as the starting point in the Open dialog.
- [func urlsFromRunningOpenPanel() -> [URL]?](./nsdocumentcontroller/urlsfromrunningopenpanel%28%29.md)
  An array of URLs that correspond to the selected files in a running Open dialog.
### Managing the Open Recent Menu
- [var maximumRecentDocumentCount: Int](./nsdocumentcontroller/maximumrecentdocumentcount.md)
  The maximum number of items that may be presented in the standard Open Recent menu.
- [func clearRecentDocuments(Any?)](./nsdocumentcontroller/clearrecentdocuments%28_%29.md)
  Empties the recent documents list for the application.
- [func noteNewRecentDocumentURL(URL)](./nsdocumentcontroller/notenewrecentdocumenturl%28_%29.md)
  Adds or replaces an Open Recent menu item corresponding to the data located by the URL.
- [func noteNewRecentDocument(NSDocument)](./nsdocumentcontroller/notenewrecentdocument%28_%29.md)
  Adds or replaces an Open Recent menu item corresponding to the document.
- [var recentDocumentURLs: [URL]](./nsdocumentcontroller/recentdocumenturls.md)
  The list of recent-document URLs.
### Validating User Interface Items
- [func validateUserInterfaceItem(any NSValidatedUserInterfaceItem) -> Bool](./nsdocumentcontroller/validateuserinterfaceitem%28_%29.md)
  Returns a Boolean value that indicates whether a given user interface item should be enabled.
### Sharing
- [var allowsAutomaticShareMenu: Bool](./nsdocumentcontroller/allowsautomaticsharemenu.md)
  A Boolean value that the system uses to insert a Share menu in the File menu.
- [func standardShareMenuItem() -> NSMenuItem](./nsdocumentcontroller/standardsharemenuitem%28%29.md)
  Returns a menu item that your app uses for sharing the current document.
### Handling Errors
- [func presentError(any Error) -> Bool](./nsdocumentcontroller/presenterror%28_%29.md)
  Presents an error alert to the user as a modal panel.
- [func presentError(any Error, modalFor: NSWindow, delegate: Any?, didPresent: Selector?, contextInfo: UnsafeMutableRawPointer?)](./nsdocumentcontroller/presenterror%28_,modalfor,delegate,didpresent,contextinfo%29.md)
  Presents an error alert to the user as a modal panel.
- [func willPresentError(any Error) -> any Error](./nsdocumentcontroller/willpresenterror%28_%29.md)
  Indicates an error condition and provides the opportunity to return the same or a different error.
### Deprecated
- [Deprecated symbols](./nsdocumentcontroller-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSMenuItemValidation](./nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSUserInterfaceValidations](./nsuserinterfacevalidations.md)
- [NSWindowRestoration](./nswindowrestoration.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Documents
- [Developing a Document-Based App](./developing-a-document-based-app.md)
  Write an app that creates, manages, edits, and saves text documents.
- [class NSDocument](./nsdocument.md)
  An abstract class that defines the interface for macOS documents.
- [class NSPersistentDocument](./nspersistentdocument.md)
  A document object that can integrate with Core Data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller)*