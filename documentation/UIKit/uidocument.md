# UIDocument

**Framework**: UIKit  
**Kind**: class

An abstract base class for managing discrete portions of your app’s data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDocument
```

## Mentions

- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md)
- [About App Development with UIKit](about-app-development-with-uikit.md)

#### Overview

Apps that make use of [`UIDocument`](uidocument.md) and its underlying architecture get many benefits for their documents:

- Asynchronous reading and writing of data on a background queue, meaning your app’s responsiveness is unaffected while reading and writing operations take place
- Coordinated reading and writing of document files automatically integrated with cloud services
- Support for discovering conflicts between different versions of a document
- Safe-saving of document data by writing data first to a temporary file and then replacing the current document file with it
- Automatic saving of document data at opportune moments and support for dealing with suspend behaviors

In the Model-View-Controller design pattern, a [`UIDocument`](uidocument.md) object is a model object or model-controller object — it manages the data of a document or the aggregate model objects that together constitute the document’s data. You typically pair it with a view controller that manages the view presenting the document’s contents. [`UIDocument`](uidocument.md) provides no direct support for managing document views, but view controllers that subclass [`UIDocumentViewController`](uidocumentviewcontroller.md) can present a `UIDocument`, and view controllers that subclass [`UIDocumentBrowserViewController`](uidocumentbrowserviewcontroller.md) can organize and display `UIDocument` collections.

Document-based apps include those that can generate multiple documents, each with its own file-system location. A document-based app must create a subclass of [`UIDocument`](uidocument.md) for its documents.

> **Note**:  If you’re using a database to store document data, create a subclass of the [`UIManagedDocument`](uimanageddocument.md) class instead of [`UIDocument`](uidocument.md); [`UIManagedDocument`](uimanageddocument.md) is a subclass of [`UIDocument`](uidocument.md).

The primary attribute of a document in the [`UIDocument`](uidocument.md) architecture is its file URL. When you initialize an instance of your document subclass by calling [`init(fileURL:)`](uidocument/init(fileurl:).md), you must pass a file URL locating the document file in the app sandbox. [`UIDocument`](uidocument.md) determines the file type (the Uniform Type Identifier associated with the file extension) and the document name (the filename component) from the file URL. You can override the accessor methods of the [`fileType`](uidocument/filetype.md) and [`localizedName`](uidocument/localizedname.md) properties to supply different values.

The following outlines the life cycle of a typical document:

1. You create a new document or open an existing document. - To create a new document, allocate and initialize an instance of your subclass and then call [`save(to:for:completionHandler:)`](uidocument/save(to:for:completionhandler:).md) on the instance.
- To open an existing document (selected by the user), allocate and initialize an instance of your subclass and then call [`open(completionHandler:)`](uidocument/open(completionhandler:).md) on the instance.
2. The user edits the document. As the user edits, track changes to the document. [`UIDocument`](uidocument.md) periodically notes when there are unsaved changes and writes the document data to its file.
3. The user requests that the document be integrated with cloud services (optional). You must enable the document for cloud storage. You must also resolve any conflicts between different versions of the same document.
4. The user closes the document. Call [`close(completionHandler:)`](uidocument/close(completionhandler:).md) on the document instance. [`UIDocument`](uidocument.md) saves the document if there are any unsaved changes.

A typical document-based app calls [`open(completionHandler:)`](uidocument/open(completionhandler:).md), [`close(completionHandler:)`](uidocument/close(completionhandler:).md), and [`save(to:for:completionHandler:)`](uidocument/save(to:for:completionhandler:).md) on the main thread. When the read or save operation kicked off by these methods concludes, the system executes the completion-handler block on the same dispatch queue as the system used to invoke the method, allowing you to complete any tasks contingent on the read or save operation. If the operation isn’t successful, the system passes [`false`](https://developer.apple.com/documentation/swift/false) to the completion-handler block.

##### Implement the Nsfilepresenter Protocol

The [`UIDocument`](uidocument.md) class adopts the [`NSFilePresenter`](https://developer.apple.com/documentation/Foundation/NSFilePresenter) protocol. When another client attempts to read the document of a [`UIDocument`](uidocument.md)-based app, the system suspends reading until the system provides the [`UIDocument`](uidocument.md) object an opportunity to save any changes made to the document.

Although some implementations do nothing, [`UIDocument`](uidocument.md) implements all [`NSFilePresenter`](https://developer.apple.com/documentation/Foundation/NSFilePresenter) methods. Specifically, [`UIDocument`](uidocument.md):

- Implements [`relinquishPresentedItem(toReader:)`](https://developer.apple.com/documentation/Foundation/NSFilePresenter/relinquishPresentedItem(toReader:)) to forward the incoming block to [`performAsynchronousFileAccess(_:)`](uidocument/performasynchronousfileaccess(_:).md)
- Implements [`relinquishPresentedItem(toWriter:)`](https://developer.apple.com/documentation/Foundation/NSFilePresenter/relinquishPresentedItem(toWriter:)) to check if the file-modification date changed; if the file is newer than before, it calls [`revert(toContentsOf:completionHandler:)`](uidocument/revert(tocontentsof:completionhandler:).md) with the value of the [`fileURL`](uidocument/fileurl.md) as the URL parameter
- Implements [`presentedItemDidMove(to:)`](https://developer.apple.com/documentation/Foundation/NSFilePresenter/presentedItemDidMove(to:)) to update the document’s file URL ([`fileURL`](uidocument/fileurl.md))

In your [`UIDocument`](uidocument.md) subclass, if you override a [`NSFilePresenter`](https://developer.apple.com/documentation/Foundation/NSFilePresenter) method, you can always invoke the superclass implementation (`super`).

##### Create a Subclass

Each document-based app must create a subclass of [`UIDocument`](uidocument.md) whose instances represent its documents. The subclassing requirements for most apps are simple:

- For writing operations, implement the [`contents(forType:)`](uidocument/contents(fortype:).md) method to provide a snapshot of document data. The data must be in the form of an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object (for flat files) or an [`FileWrapper`](https://developer.apple.com/documentation/Foundation/FileWrapper) object (for file packages). Writing operations are usually initiated through the autosave feature.
- For reading operations, implement the [`load(fromContents:ofType:)`](uidocument/load(fromcontents:oftype:).md) method to receive an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) or [`FileWrapper`](https://developer.apple.com/documentation/Foundation/FileWrapper) object and initialize the app’s data structures with it.
- Implement change tracking to enable the autosaving feature. See [`Track changes`](uidocument#Track-changes.md) for details.
- When cloud services are enabled for a document, resolve conflicts between different versions of a document. See [`Resolve conflicts and handle errors`](uidocument#Resolve-conflicts-and-handle-errors.md) for details. The system typically calls the [`contents(forType:)`](uidocument/contents(fortype:).md) and [`load(fromContents:ofType:)`](uidocument/load(fromcontents:oftype:).md) methods on the main queue. More specifically:
- The system calls the [`contents(forType:)`](uidocument/contents(fortype:).md) method on the queue that the system called the [`save(to:for:completionHandler:)`](uidocument/save(to:for:completionhandler:).md) method on; writing of data takes place on a background thread.
- The system calls the [`load(fromContents:ofType:)`](uidocument/load(fromcontents:oftype:).md) method on the queue that the system called the [`open(completionHandler:)`](uidocument/open(completionhandler:).md) method on.

If you have special requirements for reading and writing document data for which the [`contents(forType:)`](uidocument/contents(fortype:).md) and [`load(fromContents:ofType:)`](uidocument/load(fromcontents:oftype:).md) methods won’t suffice, you can override other methods of the [`UIDocument`](uidocument.md) class. See [`Override input and output methods`](uidocument#Override-input-and-output-methods.md) for a discussion of these requirements and methods.

###### Track Changes

To enable the autosaving feature of [`UIDocument`](uidocument.md), you must notify it when users make changes to a document. [`UIDocument`](uidocument.md) periodically checks whether the [`hasUnsavedChanges`](uidocument/hasunsavedchanges.md) method returns [`true`](https://developer.apple.com/documentation/swift/true); if it does, it initiates the save operation for the document.

There are two primary ways to implement change tracking in your [`UIDocument`](uidocument.md) subclass:

- Call the methods of the [`UndoManager`](https://developer.apple.com/documentation/Foundation/UndoManager) class to implement undo and redo for the document. You can access the default [`UndoManager`](https://developer.apple.com/documentation/Foundation/UndoManager) object from the [`undoManager`](uidocument/undomanager.md) property. This is the preferred approach, especially for existing apps that already support undo and redo.
- Call the [`updateChangeCount(_:)`](uidocument/updatechangecount(_:).md) method at the appropriate junctures in your code.

###### Resolve Conflicts and Handle Errors

A [`UIDocument`](uidocument.md) object has a specific state at any moment in its life cycle. You can check the current state by querying the [`documentState`](uidocument/documentstate.md) property, and get notified about changes by observing the [`stateChangedNotification`](uidocument/statechangednotification.md) notification.

If the owner enables a document for iCloud, it’s important to check for conflicting versions and to attempt to resolve conflicts. Listen for the [`stateChangedNotification`](uidocument/statechangednotification.md) notification and then checking if the document state is [`inConflict`](uidocument/state/inconflict.md). This state indicates that there are conflicting versions of the document, which you can access by calling the [`NSFileVersion`](https://developer.apple.com/documentation/Foundation/NSFileVersion) class method [`unresolvedConflictVersionsOfItem(at:)`](https://developer.apple.com/documentation/Foundation/NSFileVersion/unresolvedConflictVersionsOfItem(at:)), passing in the document’s file URL. If you can resolve a conflict correctly without user interaction, do so. Otherwise, discretely notify the user that a conflict exists and let them choose how to resolve it. Possible approaches include:

- Display the conflicting versions, from which a user can pick one or both versions to keep.
- Display a merged version and giving the user an option to pick it.
- Display the file modification dates and giving the user the option to choose one or both.

Document state, in addition to indicating an inter-file conflict, can indicate errors. For example, [`closed`](uidocument/state/closed.md) indicates an error in reading, and [`savingError`](uidocument/state/savingerror.md) indicates an error in saving or reverting a document. The system notifies your app of reading and writing errors through the `success` parameter passed into the completion handlers of the [`open(completionHandler:)`](uidocument/open(completionhandler:).md), [`close(completionHandler:)`](uidocument/close(completionhandler:).md), [`revert(toContentsOf:completionHandler:)`](uidocument/revert(tocontentsof:completionhandler:).md), and [`save(to:for:completionHandler:)`](uidocument/save(to:for:completionhandler:).md) methods.

You can handle errors by calling or implementing the [`handleError(_:userInteractionPermitted:)`](uidocument/handleerror(_:userinteractionpermitted:).md) method; the default implementations of the [`open(completionHandler:)`](uidocument/open(completionhandler:).md) and [`save(to:for:completionHandler:)`](uidocument/save(to:for:completionhandler:).md) methods call `handleError(_:userInteractionPermitted:)` when a [`UIDocument`](uidocument.md) object encounters a reading or writing error, respectively. You can handle read, save, and reversion errors by informing the user and, if the situation permits, trying to recover from the error.

Be sure to read the description for the [`contents(forType:)`](uidocument/contents(fortype:).md) method for its guidance on handling errors encountered during document saving.

###### Override Input and Output Methods

If you app has special requirements for reading or writing document data, it can override methods of [`UIDocument`](uidocument.md) other than [`load(fromContents:ofType:)`](uidocument/load(fromcontents:oftype:).md) and [`contents(forType:)`](uidocument/contents(fortype:).md). These requirements often include the following:

- Incremental reading and writing of large data files Override the [`read(from:)`](uidocument/read(from:).md) and [`writeContents(_:to:for:originalContentsURL:)`](uidocument/writecontents(_:to:for:originalcontentsurl:).md) methods, respectively.
- Custom representations of document data (that is, not an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) or [`FileWrapper`](https://developer.apple.com/documentation/Foundation/FileWrapper) object) Override the [`read(from:)`](uidocument/read(from:).md) method when reading document data and the [`writeContents(_:to:for:originalContentsURL:)`](uidocument/writecontents(_:to:for:originalcontentsurl:).md) method when writing document data.
- Performing actions before or after reading or writing data Override [`open(completionHandler:)`](uidocument/open(completionhandler:).md) and [`save(to:for:completionHandler:)`](uidocument/save(to:for:completionhandler:).md).
- A custom approach to safe-saving Override the [`writeContents(_:andAttributes:safelyTo:for:)`](uidocument/writecontents(_:andattributes:safelyto:for:).md) method.
- Changing the file type of a document before it’s saved Override the [`savingFileType`](uidocument/savingfiletype.md) method to return a file type other than the default ([`fileType`](uidocument/filetype.md)). An example of this is an RTF document which, after a user adds an image to it, should be saved as an RTFD document.

If you override these methods, be aware that all reading and writing of document data must be done on a background queue and must be coordinated with other attempts to read from and write to the same document file. Because of this, you usually call the superclass implementation (`super`) as part of your override, and if you call other `UIDocument` methods, you usually invoke them in the block passed into a call of the [`performAsynchronousFileAccess(_:)`](uidocument/performasynchronousfileaccess(_:).md) method. Read the method descriptions for details.

###### Access Document Attributes

If you override any of the document-attribute properties (listed under [`Accessing document attributes`](uidocument#Accessing-document-attributes.md)) by overriding the related accessor methods, be aware that the UIKit framework can call these accessor methods on a background thread. Thus your overriding implementation must be thread safe.

##### Rename Documents

`UIDocument` provides support for changing the document’s title. Security considerations require that clients can’t programmatically rename a file on the file system, and that the system confirms that a person intends to rename their file. To satisfy these restrictions, the system, instead of your app, presents a renaming user interface using a process outside your app. The external process renames the underlying file and reports the new location back to the client.

To support this external process, `UIDocument` conforms to [`UINavigationItemRenameDelegate`](uinavigationitemrenamedelegate-96g5t.md) and handles the rename request internally when a person invokes renaming from the title menu. If you’re using [`UIDocumentViewController`](uidocumentviewcontroller.md), it automatically configures renaming for you. Otherwise, you manually assign the document as the navigation item’s [`renameDelegate`](uinavigationitem/renamedelegate-o32h.md).

```swift
init(document: MyDocument) {
    self.document = document
    super.init(nibName:nil, bundle: nil)
    self.navigationItem.renameDelegate = document
}
```

The Rename action appears in the title menu as one of the system-suggested actions. When a person taps the Rename action, the system shows an inline text field for changing the navigation item’s `title`. Upon renaming the item, the system changes the file name in storage as though the person renamed the file in another application.

Prior to iOS 17, to enable the system rename user interface, a client view controller adopts the `UINavigationItemRenameDelegate` protocol and assigns itself as the navigation item’s `renameDelegate`. It’s the client’s responsibility to implement callbacks such as [`navigationItem(_:didEndRenamingWith:)`](uinavigationitemrenamedelegate-5j4ws/navigationitem(_:didendrenamingwith:).md) (Swift) or [`navigationItem:didEndRenamingWithTitle:`](uinavigationitemrenamedelegate-96g5t/navigationitem:didendrenamingwithtitle:.md) (Objective-C) to explicitly move the file in storage.

```swift
class EditorViewController: UIViewController,
        UINavigationItemRenameDelegate {

    override func viewDidLoad() {
        super.viewDidLoad()
        navigationItem.renameDelegate = self
    }

    func navigationItem(_ navigationItem: UINavigationItem, didEndRenamingWith: title: String) {
        // Move the file, update the model, and so on.
    }
}
```

## Topics

### Initializing a document object
- [init(fileURL: URL)](uidocument/init(fileurl:).md)
  Returns a document object initialized with its file-system location.
### Accessing document attributes
- [var fileURL: URL](uidocument/fileurl.md)
  The file URL you use to initialize the document.
- [var localizedName: String](uidocument/localizedname.md)
  The localized name of the document.
- [var fileType: String?](uidocument/filetype.md)
  The file type of the document.
- [var fileModificationDate: Date?](uidocument/filemodificationdate.md)
  The date and time your app last modified the document file.
- [var documentState: UIDocument.State](uidocument/documentstate.md)
  The current state of the document.
- [var progress: Progress?](uidocument/progress.md)
  The upload or download progress of a document.
### Writing document data
- [func close(completionHandler: ((Bool) -> Void)?)](uidocument/close(completionhandler:).md)
  Asynchronously closes the document after saving any changes.
- [func contents(forType: String) throws -> Any](uidocument/contents(fortype:).md)
  Returns the document data to be saved.
- [func save(to: URL, for: UIDocument.SaveOperation, completionHandler: ((Bool) -> Void)?)](uidocument/save(to:for:completionhandler:).md)
  Saves document data to the specified location in the application sandbox.
- [func writeContents(Any, andAttributes: [AnyHashable : Any]?, safelyTo: URL, for: UIDocument.SaveOperation) throws](uidocument/writecontents(_:andattributes:safelyto:for:).md)
  Ensures that document data is written safely to a specified location in the application sandbox.
- [func writeContents(Any, to: URL, for: UIDocument.SaveOperation, originalContentsURL: URL?) throws](uidocument/writecontents(_:to:for:originalcontentsurl:).md)
  Writes the document data to disk at the sandbox location indicated by a file URL.
- [var savingFileType: String?](uidocument/savingfiletype.md)
  Returns the file type to use for saving a document.
- [func fileAttributesToWrite(to: URL, for: UIDocument.SaveOperation) throws -> [AnyHashable : Any]](uidocument/fileattributestowrite(to:for:).md)
  Returns a dictionary of file attributes to associate with the document file when writing or updating it.
- [func fileNameExtension(forType: String?, saveOperation: UIDocument.SaveOperation) -> String](uidocument/filenameextension(fortype:saveoperation:).md)
  Returns a file extension to append to the file URL of the document file being written.
### Reading document data
- [func open(completionHandler: ((Bool) -> Void)?)](uidocument/open(completionhandler:).md)
  Opens a document asynchronously.
- [func load(fromContents: Any, ofType: String?) throws](uidocument/load(fromcontents:oftype:).md)
  Loads the document data into the app’s data model.
- [func read(from: URL) throws](uidocument/read(from:).md)
  Reads the document data in a file at a specified location in the application sandbox.
### Creating new documents
- [UIDocument.CreationIntent](uidocument/creationintent.md)
  An app intent that creates new documents for your app.
### Accessing document files asynchronously
- [func performAsynchronousFileAccess(() -> Void)](uidocument/performasynchronousfileaccess(_:).md)
  Schedules a document-reading or document-writing operation on a concurrent background queue.
### Reverting a document
- [func revert(toContentsOf: URL, completionHandler: ((Bool) -> Void)?)](uidocument/revert(tocontentsof:completionhandler:).md)
  Reverts a document to the most recent document data stored on-disk.
### Disabling and enabling editing
- [func disableEditing()](uidocument/disableediting.md)
  Disables editing when it’s unsafe to make changes to a document.
- [func enableEditing()](uidocument/enableediting.md)
  Enables editing when it’s safe again to make changes to a document.
### Tracking changes and autosaving
- [var hasUnsavedChanges: Bool](uidocument/hasunsavedchanges.md)
  A Boolean value that indicates whether the document has any unsaved changes.
- [func updateChangeCount(UIDocument.ChangeKind)](uidocument/updatechangecount(_:).md)
  Updates the change counter by indicating the kind of change.
- [var undoManager: UndoManager!](uidocument/undomanager.md)
  The undo manager for the document.
- [func changeCountToken(for: UIDocument.SaveOperation) -> Any](uidocument/changecounttoken(for:).md)
  Returns a change token for a specific save operation.
- [func updateChangeCount(withToken: Any, for: UIDocument.SaveOperation)](uidocument/updatechangecount(withtoken:for:).md)
  Updates the change count with reference to a change-count token passed in by UIKit.
- [func autosave(completionHandler: ((Bool) -> Void)?)](uidocument/autosave(completionhandler:).md)
  Initiates automatic saving of documents with unsaved changes.
### Supporting user activities
- [var userActivity: NSUserActivity?](uidocument/useractivity.md)
  An object encapsulating a user activity supported by this document.
- [func restoreUserActivityState(NSUserActivity)](uidocument/restoreuseractivitystate(_:).md)
  Restores the state needed to continue the given user activity.
- [func updateUserActivityState(NSUserActivity)](uidocument/updateuseractivitystate(_:).md)
  Updates the state of the given user activity.
### Resolving conflicts and handling errors
- [func handleError(any Error, userInteractionPermitted: Bool)](uidocument/handleerror(_:userinteractionpermitted:).md)
  Handles an error that occurs during an attempt to read, save, or revert a document.
- [func finishedHandlingError(any Error, recovered: Bool)](uidocument/finishedhandlingerror(_:recovered:).md)
  Tells UIKit that you finished handling the error.
- [func userInteractionNoLongerPermitted(forError: any Error)](uidocument/userinteractionnolongerpermitted(forerror:).md)
  Indicates when it’s no longer safe to proceed without immediately handling the error.
### Constants
- [UIDocument.ChangeKind](uidocument/changekind.md)
  Constants that specify the kind of change to a document.
- [UIDocument.SaveOperation](uidocument/saveoperation.md)
  Constants that specify the type of save operation.
- [UIDocument.State](uidocument/state.md)
  Constants that specify the document state.
- [class let userActivityURLKey: String](uidocument/useractivityurlkey.md)
  The key that identifies the document associated with a user activity.
### Notifications
- [class let stateChangedNotification: NSNotification.Name](uidocument/statechangednotification.md)
  A notification the document object posts when there’s a change in the state of the document.
### Structures
- [UIDocument.StateChangedMessage](uidocument/statechangedmessage.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIManagedDocument](uimanageddocument.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSFilePresenter](../Foundation/NSFilePresenter.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [ProgressReporting](../Foundation/ProgressReporting.md)
- [Sendable](../Swift/Sendable.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UIManagedDocument](uimanageddocument.md)
  A managed document object that integrates with Core Data.
- [Synchronizing documents in the iCloud environment](synchronizing-documents-in-the-icloud-environment.md)
  Manage documents across multiple devices to create a seamless editing and collaboration experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument)*