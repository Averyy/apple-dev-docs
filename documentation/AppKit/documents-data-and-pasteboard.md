# Documents, Data, and Pasteboard

**Framework**: AppKit

Organize your app’s data and preferences, and share that data on the pasteboard or in iCloud.

## Topics

### Documents
- [Developing a Document-Based App](developing-a-document-based-app.md)
  Write an app that creates, manages, edits, and saves text documents.
- [class NSDocument](nsdocument.md)
  An abstract class that defines the interface for macOS documents.
- [class NSDocumentController](nsdocumentcontroller.md)
  An object that manages an app’s documents.
- [class NSPersistentDocument](nspersistentdocument.md)
  A document object that can integrate with Core Data.
### User Preferences
- [class NSUserDefaultsController](nsuserdefaultscontroller.md)
  A controller that accesses user preference information for your app from the user’s defaults database.
- [class NSUbiquitousKeyValueStore](../Foundation/NSUbiquitousKeyValueStore.md)
  An iCloud-based container of key-value pairs you share among instances of your app running on a person’s devices.
### Pasteboard
- [class NSPasteboard](nspasteboard.md)
  An object that transfers data to and from the pasteboard server.
- [class NSPasteboardItem](nspasteboarditem.md)
  An item on a pasteboard.
- [protocol NSPasteboardReading](nspasteboardreading.md)
  A set of methods that defines the interface for initializing an object from a pasteboard.
- [protocol NSPasteboardWriting](nspasteboardwriting.md)
  A set of methods that defines the interface for retrieving a representation of an object that can be written to a pasteboard.
- [protocol NSPasteboardItemDataProvider](nspasteboarditemdataprovider.md)
  A set of methods implemented by the data provider of a pasteboard item to provide the data for a particular UTI type.
- [NSPasteboard.ContentsOptions](nspasteboard/contentsoptions.md)
  Options for preparing the pasteboard.
- [protocol NSPasteboardTypeOwner](nspasteboardtypeowner.md)
  An object that serves as a data provider for data types that use lazy data fulfillment from a pasteboard request.
### File Promises
- [Supporting Drag and Drop Through File Promises](supporting-drag-and-drop-through-file-promises.md)
  Receive and provide file promises to support dragged app files and pasteboard operations.
- [Supporting Table View Drag and Drop Through File Promises](supporting-table-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [Supporting Collection View Drag and Drop Through File Promises](supporting-collection-view-drag-and-drop-through-file-promises.md)
  Share data between macOS apps during drag and drop by using an item provider.
- [class NSFilePromiseProvider](nsfilepromiseprovider.md)
  An object that provides a promise for the pasteboard.
- [protocol NSFilePromiseProviderDelegate](nsfilepromiseproviderdelegate.md)
  A set of methods that provides the name of the promised file and writes the file to the destination directory when the file promise is fulfilled.
- [class NSFilePromiseReceiver](nsfilepromisereceiver.md)
  An object that receives a file promise from the pasteboard.
### Object Editing
- [protocol NSEditor](nseditor.md)
- [protocol NSEditorRegistration](nseditorregistration.md)
  A set of methods that controllers can implement to enable an editor view to inform the controller when it has uncommitted changes.

## See Also

- [App and Environment](app-and-environment.md)
  Learn about the objects that you use to interact with the system.
- [Cocoa Bindings](cocoa-bindings.md)
  Automatically synchronize your data model with your app’s interface using Cocoa Bindings.
- [Resource Management](resource-management.md)
  Manage the storyboards and nib files containing your app’s user interface, and learn how to load data that is stored in resource files.
- [App Extensions](app-extensions.md)
  Extend your app’s basic functionality to other parts of the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/documents-data-and-pasteboard)*