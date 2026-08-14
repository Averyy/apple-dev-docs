# Documents

**Framework**: SwiftUI

Enable people to open and manage documents.

#### Overview

Create a user interface for opening and editing documents.

![None](/images/com.apple.SwiftUI/documents-hero@2x.png)

Use the [`ReadableDocument`](readabledocument.md) and [`WritableDocument`](writabledocument.md) protocols to define your document model, or adopt [`Document`](document.md), a convenience protocol that combines both, when your document needs to support reading and writing. They give you direct access to file URLs, integrate with Swift concurrency, and support progress reporting. You can also use SwiftData-backed documents using an initializer like [`init(editing:contentType:editor:prepareDocument:)`](documentgroup/init(editing:contenttype:editor:preparedocument:).md).

SwiftUI supports standard behaviors people expect from a document-based app, appropriate for each platform, like multiwindow support, open and save panels. For related design guidance, see [`Patterns`](https://developer.apple.com/design/human-interface-guidelines/patterns) in the Human Interface Guidelines.

## Topics

### Creating a document
- [Creating a document-based app](creating-a-document-based-app.md)
  Build apps that people can use to open, edit, and save files using coordinated file access.
- [Handling advanced document scenarios](handling-advanced-document-scenarios.md)
  Extend your document-based app to support custom file formats, on-demand file access, and progress reporting.
- [Updating your document-based app](updating-your-document-based-app.md)
  Migrate an existing app to adopt URL-based document reading and writing with Swift concurrency.
- [Building a document-based app with SwiftUI](building-a-document-based-app-with-swiftui.md)
  Create, save, and open documents in a multiplatform app.
- [Building a document-based app using SwiftData](building-a-document-based-app-using-swiftdata.md)
  Code along with the WWDC presenter to transform an app with SwiftData.
- [struct DocumentGroup](documentgroup.md)
  A scene that enables support for opening, creating, and saving documents.
### Storing document data in a reference type instance
- [protocol Document](document.md)
  A document that supports both reading and writing.
- [protocol ReadableDocument](readabledocument.md)
  A document type that supports reading from file.
- [protocol WritableDocument](writabledocument.md)
  A document type that supports writing to file.
- [class URLDocumentConfiguration](urldocumentconfiguration.md)
  The configuration of an open document that stores its file URL, last modification date, and related metadata.
- [struct DocumentCreationContext](documentcreationcontext.md)
  Context about how a document was created.
- [protocol DocumentBaseBox](documentbasebox.md)
  A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.
### Accessing document configuration
- [var documentConfiguration: DocumentConfiguration?](environmentvalues/documentconfiguration.md)
  The configuration of a document in a [`DocumentGroup`](documentgroup.md).
- [struct DocumentConfiguration](documentconfiguration.md)
  The configuration of a document in a [`DocumentGroup`](documentgroup.md).
- [var undoManager: UndoManager?](environmentvalues/undomanager.md)
  The undo manager used to register a view’s undo operations.
### Reading and writing documents
- [struct DocumentReadConfiguration](documentreadconfiguration.md)
  The context SwiftUI passes to [`reader(configuration:)`](readabledocument/reader(configuration:).md).
- [struct DocumentWriteConfiguration](documentwriteconfiguration.md)
  The context SwiftUI passes to [`writer(configuration:)`](writabledocument/writer(configuration:).md).
- [protocol DocumentReader](documentreader.md)
  A type that reads a document’s content from a file.
- [protocol DocumentWriter](documentwriter.md)
  A type that writes a document’s content to a file.
- [struct FileWrapperDocumentReader](filewrapperdocumentreader.md)
  A document reader that deserializes a `FileWrapper` into a snapshot.
- [struct FileWrapperDocumentWriter](filewrapperdocumentwriter.md)
  A document writer that serializes a snapshot into a `FileWrapper`.
### Opening a document programmatically
- [var newDocument: NewDocumentAction](environmentvalues/newdocument.md)
  An action in the environment that presents a new document.
- [var openDocument: OpenDocumentAction](environmentvalues/opendocument.md)
  An action in the environment that presents an existing document.
- [struct OpenDocumentAction](opendocumentaction.md)
  An action that presents an existing document.
### Configuring the document launch experience
- [struct DocumentGroupLaunchScene](documentgrouplaunchscene.md)
  A launch scene for document-based applications.
- [func documentLaunchTitle(_:)](scene/documentlaunchtitle(_:).md)
  Sets the title displayed on the document launch card.
- [func documentLaunchSubtitle(_:)](scene/documentlaunchsubtitle(_:).md)
  Sets the subtitle displayed beneath the title on the document launch card.
- [struct DocumentLaunchView](documentlaunchview.md)
  A view to present when launching document-related user experience.
- [func documentLaunchTitle(_:)](view/documentlaunchtitle(_:).md)
  Sets the title displayed on the document launch card.
- [func documentLaunchSubtitle(_:)](view/documentlaunchsubtitle(_:).md)
  Sets the subtitle displayed beneath the title on the document launch card.
- [func documentBrowserContextMenu(([URL]?) -> some View) -> some View](view/documentbrowsercontextmenu(_:).md)
  Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [struct DocumentLaunchGeometryProxy](documentlaunchgeometryproxy.md)
  A proxy for access to the frame of the scene and its title view.
- [struct DefaultDocumentGroupLaunchActions](defaultdocumentgrouplaunchactions.md)
  The default actions for the document group launch scene and the document launch view.
- [struct NewDocumentButton](newdocumentbutton.md)
  A button that creates and opens new documents.
- [struct DefaultNewDocumentButtonLabel](defaultnewdocumentbuttonlabel.md)
  The default label used for a new document button.
- [struct DocumentCreationSource](documentcreationsource.md)
  Describes the source used to create a new document.
### Renaming a document
- [struct RenameButton](renamebutton.md)
  A button that triggers a standard rename action.
- [func renameAction(_:)](view/renameaction(_:).md)
  Sets a closure to run for the rename action.
- [var rename: RenameAction?](environmentvalues/rename.md)
  An action that activates the standard rename interaction.
- [struct RenameAction](renameaction.md)
  An action that activates a standard rename interaction.
### Deprecated
- [protocol FileDocument](filedocument.md)
  A type that you use to serialize documents to and from file.
- [struct FileDocumentConfiguration](filedocumentconfiguration.md)
  The properties of an open file document.
- [struct FileDocumentReadConfiguration](filedocumentreadconfiguration.md)
  The configuration for reading file contents.
- [struct FileDocumentWriteConfiguration](filedocumentwriteconfiguration.md)
  The configuration for serializing file contents.
- [struct NewDocumentAction](newdocumentaction.md)
  An action that presents a new document.
- [protocol ReferenceFileDocument](referencefiledocument.md)
  A type that you use to serialize reference type documents to and from file.
- [struct ReferenceFileDocumentConfiguration](referencefiledocumentconfiguration.md)
  The properties of an open reference file document.

## See Also

- [App organization](app-organization.md)
  Define the entry point and top-level structure of your app.
- [Scenes](scenes.md)
  Declare the user interface groupings that make up the parts of your app.
- [Windows](windows.md)
  Display user interface content in a window or a collection of windows.
- [Immersive spaces](immersive-spaces.md)
  Display unbounded content in a person’s surroundings.
- [Navigation](navigation.md)
  Enable people to move between different parts of your app’s view hierarchy within a scene.
- [Modal presentations](modal-presentations.md)
  Present content in a separate view that offers focused interaction.
- [Toolbars](toolbars.md)
  Provide immediate access to frequently used commands and controls.
- [Search](search.md)
  Enable people to search for text or other content within your app.
- [App extensions](app-extensions.md)
  Extend your app’s basic functionality to other parts of the system, like by adding a Widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documents)*