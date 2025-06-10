# NSPersistentDocument

**Framework**: AppKit  
**Kind**: class

A document object that can integrate with Core Data.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSPersistentDocument
```

#### Overview

The [`NSPersistentDocument`](nspersistentdocument.md) class is a subclass of [`NSDocument`](nsdocument.md) that is designed to easily integrate into the Core Data framework. It provides methods to access a document-wide [`NSManagedObjectContext`](https://developer.apple.com/documentation/CoreData/NSManagedObjectContext) object, and provides default implementations of methods to read and write files using the persistence framework. In a persistent document, the undo manager functionality is taken over by managed object context.

Standard document behavior is implemented as follows:

- Opening a document invokes [`configurePersistentStoreCoordinator(for:ofType:modelConfiguration:storeOptions:)`](nspersistentdocument/configurepersistentstorecoordinator(for:oftype:modelconfiguration:storeoptions:).md) with the new URL, and adds a store of the default type (XML). Objects are loaded from the persistent store on demand through the document’s context.
- Saving a new document adds a store of the default type with the chosen URL and invokes save: on the context. For an existing document, a save just invokes [`save()`](https://developer.apple.com/documentation/CoreData/NSManagedObjectContext/save()) on the context.
- Save As for a new document simply invokes save. For an opened document, it migrates the persistent store to the new URL and invokes [`save()`](https://developer.apple.com/documentation/CoreData/NSManagedObjectContext/save()) on the context.
- Revert resets the document’s managed object context. Objects are subsequently loaded from the persistent store on demand, as with opening a new document.

By default an [`NSPersistentDocument`](nspersistentdocument.md) instance creates its own ready-to-use persistence stack including managed object context, persistent object store coordinator and persistent store. There is a one-to-one mapping between the document and the backing object store.

You can customize the architecture of the persistence stack by overriding the [`managedObjectModel`](nspersistentdocument/managedobjectmodel.md) property and [`configurePersistentStoreCoordinator(for:ofType:modelConfiguration:storeOptions:)`](nspersistentdocument/configurepersistentstorecoordinator(for:oftype:modelconfiguration:storeoptions:).md) method. You might wish to do this, for example, to specify a particular managed object model.

> ❗ **Important**:  [`NSPersistentDocument`](nspersistentdocument.md) does not support some document behaviors: - File wrappers.
- [`NSDocument.SaveOperationType.saveToOperation`](nsdocument/saveoperationtype/savetooperation.md) operation type. Core Data does not support saving changes to a new document while maintaining the unsaved state in the current document. - Asynchronous saving. [`NSPersistentDocument`](nspersistentdocument.md) does not support the asynchronous saving API of [`NSDocument`](nsdocument.md) because that API requires accessing the document’s state on multiple threads and that violates the requirements of the [`NSManagedObjectContext`](https://developer.apple.com/documentation/CoreData/NSManagedObjectContext) class. Do not override [`canAsynchronouslyWrite(to:ofType:for:)`](nsdocument/canasynchronouslywrite(to:oftype:for:).md).

##### Undo Support

The persistent document uses the managed object context’s undo manager.

> ❗ **Important**: Do not override the following properties, their getters, or their setters: - [`hasUndoManager`](nsdocument/hasundomanager.md)
- [`undoManager`](nsdocument/undomanager.md)

The [`isDocumentEdited`](nsdocument/isdocumentedited.md) method returns [`true`](https://developer.apple.com/documentation/swift/true) if the persistent document’s managed object context, or editors registered with the context, have uncommitted changes, otherwise it returns [`false`](https://developer.apple.com/documentation/swift/false).

## Topics

### Managing the Persistence Objects
- [var managedObjectContext: NSManagedObjectContext?](nspersistentdocument/managedobjectcontext.md)
  The managed object context for the document.
- [var managedObjectModel: NSManagedObjectModel?](nspersistentdocument/managedobjectmodel.md)
  The managed object model of the document.
- [func configurePersistentStoreCoordinator(for: URL, ofType: String, modelConfiguration: String?, storeOptions: [String : Any]?) throws](nspersistentdocument/configurepersistentstorecoordinator(for:oftype:modelconfiguration:storeoptions:).md)
  Configures the receiver’s persistent store coordinator with the appropriate stores for a given URL.
- [func persistentStoreType(forFileType: String) -> String](nspersistentdocument/persistentstoretype(forfiletype:).md)
  Returns the type of persistent store associated with the specified file type.
### Document Content Management
- [func read(from: URL, ofType: String) throws](nspersistentdocument/read(from:oftype:).md)
  Sets the contents of the receiver by reading from a file of a given type located by a given URL.
- [func revert(toContentsOf: URL, ofType: String) throws](nspersistentdocument/revert(tocontentsof:oftype:).md)
  Overridden to clean up the managed object context and controllers during a revert.
- [func write(to: URL, ofType: String, for: NSDocument.SaveOperationType, originalContentsURL: URL?) throws](nspersistentdocument/write(to:oftype:for:originalcontentsurl:).md)
  Saves changes in the document’s managed object context and saves the document’s persistent store to a given URL.

## Relationships

### Inherits From
- [NSDocument](nsdocument.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSEditorRegistration](nseditorregistration.md)
- [NSFilePresenter](../Foundation/NSFilePresenter.md)
- [NSMenuItemValidation](nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceValidations](nsuserinterfacevalidations.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Developing a Document-Based App](developing-a-document-based-app.md)
  Write an app that creates, manages, edits, and saves text documents.
- [class NSDocument](nsdocument.md)
  An abstract class that defines the interface for macOS documents.
- [class NSDocumentController](nsdocumentcontroller.md)
  An object that manages an app’s documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspersistentdocument)*