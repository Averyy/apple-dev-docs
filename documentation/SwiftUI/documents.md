# Documents

**Framework**: SwiftUI

Enable people to open and manage documents.

#### Overview

Create a user interface for opening and editing documents using the [`DocumentGroup`](documentgroup.md) scene type.

![None](https://docs-assets.developer.apple.com/published/9f0133f6a85bd81cbf87453f28384847/documents-hero%402x.png)

You initialize the scene with a model that describes the organization of the document’s data, and a view hierarchy that SwiftUI uses to display the document’s contents to the user. You can use either a value type model, which you typically store as a structure, that conforms to the [`FileDocument`](filedocument.md) protocol, or a reference type model you store in a class instance that conforms to the [`ReferenceFileDocument`](referencefiledocument.md) protocol. You can also use SwiftData-backed documents using an initializer like [`init(editing:contentType:editor:prepareDocument:)`](documentgroup/init(editing:contenttype:editor:preparedocument:).md).

SwiftUI supports standard behaviors that users expect from a document-based app, appropriate for each platform, like multiwindow support, open and save panels, drag and drop, and so on. For related design guidance, see [`Patterns`](https://developer.apple.com/design/Human-Interface-Guidelines/patterns) in the Human Interface Guidelines.

## Topics

### Creating a document
- [Building a document-based app with SwiftUI](building-a-document-based-app-with-swiftui.md)
  Create, save, and open documents in a multiplatform app.
- [Building a document-based app using SwiftData](building-a-document-based-app-using-swiftdata.md)
  Code along with the WWDC presenter to transform an app with SwiftData.
- [struct DocumentGroup](documentgroup.md)
  A scene that enables support for opening, creating, and saving documents.
### Storing document data in a structure instance
- [protocol FileDocument](filedocument.md)
  A type that you use to serialize documents to and from file.
- [struct FileDocumentConfiguration](filedocumentconfiguration.md)
  The properties of an open file document.
### Storing document data in a class instance
- [protocol ReferenceFileDocument](referencefiledocument.md)
  A type that you use to serialize reference type documents to and from file.
- [struct ReferenceFileDocumentConfiguration](referencefiledocumentconfiguration.md)
  The properties of an open reference file document.
- [var undoManager: UndoManager?](environmentvalues/undomanager.md)
  The undo manager used to register a view’s undo operations.
### Accessing document configuration
- [var documentConfiguration: DocumentConfiguration?](environmentvalues/documentconfiguration.md)
  The configuration of a document in a [`DocumentGroup`](documentgroup.md).
- [struct DocumentConfiguration](documentconfiguration.md)
### Reading and writing documents
- [struct FileDocumentReadConfiguration](filedocumentreadconfiguration.md)
  The configuration for reading file contents.
- [struct FileDocumentWriteConfiguration](filedocumentwriteconfiguration.md)
  The configuration for serializing file contents.
### Opening a document programmatically
- [var newDocument: NewDocumentAction](environmentvalues/newdocument.md)
  An action in the environment that presents a new document.
- [struct NewDocumentAction](newdocumentaction.md)
  An action that presents a new document.
- [var openDocument: OpenDocumentAction](environmentvalues/opendocument.md)
  An action in the environment that presents an existing document.
- [struct OpenDocumentAction](opendocumentaction.md)
  An action that presents an existing document.
### Configuring the document launch experience
- [struct DocumentGroupLaunchScene](documentgrouplaunchscene.md)
  A launch scene for document-based applications.
- [struct DocumentLaunchView](documentlaunchview.md)
  A view to present when launching document-related user experience.
- [struct DocumentLaunchGeometryProxy](documentlaunchgeometryproxy.md)
  A proxy for access to the frame of the scene and its title view.
- [struct DefaultDocumentGroupLaunchActions](defaultdocumentgrouplaunchactions.md)
  The default actions for the document group launch scene and the document launch view.
- [struct NewDocumentButton](newdocumentbutton.md)
  A button that creates and opens new documents.
- [protocol DocumentBaseBox](documentbasebox.md)
  A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.
### Renaming a document
- [struct RenameButton](renamebutton.md)
  A button that triggers a standard rename action.
- [func renameAction(_:)](view/renameaction(_:).md)
  Sets a closure to run for the rename action.
- [var rename: RenameAction?](environmentvalues/rename.md)
  An action that activates the standard rename interaction.
- [struct RenameAction](renameaction.md)
  An action that activates a standard rename interaction.

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