# UIManagedDocument

**Framework**: UIKit  
**Kind**: class

A managed document object that integrates with Core Data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIManagedDocument
```

#### Overview

[`UIManagedDocument`](uimanageddocument.md) is a concrete subclass of [`UIDocument`](uidocument.md). When you initialize a managed document, you specify the URL for the document location. The document object then creates a Core Data stack to use to access the document’s persistent store using a managed object model from the app’s main bundle. [`UIManagedDocument`](uimanageddocument.md) performs all the basic setup you need for Core Data, and in some cases you may use instances of the class directly (without a need to subclass). You can supply configuration options for the creation of the coordinator using [`persistentStoreOptions`](uimanageddocument/persistentstoreoptions.md), and for the model using [`modelConfiguration`](uimanageddocument/modelconfiguration.md). You can also perform additional customization by creating a subclass of [`UIManagedDocument`](uimanageddocument.md):

- Override [`persistentStoreName`](uimanageddocument/persistentstorename.md) to customize the name of the persistent store file inside the document’s file package.
- Override [`managedObjectModel`](uimanageddocument/managedobjectmodel.md) to customize creation of the managed object model.

You do this if, for example, your app supports multiple document types, each of which uses a different model. You want to ensure that the models aren’t merged for each document class.

- Override [`persistentStoreType(forFileType:)`](uimanageddocument/persistentstoretype(forfiletype:).md) to customize the type of persistent store used by a document.
- Override [`configurePersistentStoreCoordinator(for:ofType:modelConfiguration:storeOptions:)`](uimanageddocument/configurepersistentstorecoordinator(for:oftype:modelconfiguration:storeoptions:).md) to customize the loading or creation of a persistent store.

##### Handling Errors

To enable your app to observe and handle errors in saving and validating a managed document, you must subclass the [`UIManagedDocument`](uimanageddocument.md) class and override one or both of the following two inherited methods from the [`UIDocument`](uidocument.md) class:

- [`handleError(_:userInteractionPermitted:)`](uidocument/handleerror(_:userinteractionpermitted:).md)
- [`finishedHandlingError(_:recovered:)`](uidocument/finishedhandlingerror(_:recovered:).md)

Overriding is required because otherwise, the only information your app receives on error is the [`stateChangedNotification`](uidocument/statechangednotification.md) notification, which doesn’t contain a `userInfo` dictionary and so doesn’t convey specific error information.

## Topics

### Managing the Core Data stack
- [func configurePersistentStoreCoordinator(for: URL, ofType: String, modelConfiguration: String?, storeOptions: [AnyHashable : Any]?) throws](uimanageddocument/configurepersistentstorecoordinator(for:oftype:modelconfiguration:storeoptions:).md)
  Creates or loads the document’s persistent store.
- [var managedObjectContext: NSManagedObjectContext](uimanageddocument/managedobjectcontext.md)
  The document’s managed object context.
- [var managedObjectModel: NSManagedObjectModel](uimanageddocument/managedobjectmodel.md)
  The document’s managed object model.
- [var persistentStoreOptions: [AnyHashable : Any]?](uimanageddocument/persistentstoreoptions.md)
  Options used when creating the document’s persistent store.
- [var modelConfiguration: String?](uimanageddocument/modelconfiguration.md)
  A model configuration name to be passed when configuring the persistent store.
- [func persistentStoreType(forFileType: String) -> String](uimanageddocument/persistentstoretype(forfiletype:).md)
  Returns the Core Data store type for a given document file type.
### Customizing read and write operations
- [func readAdditionalContent(from: URL) throws](uimanageddocument/readadditionalcontent(from:).md)
  Handles reading non-Core Data content in the additional content directory in the document’s file package.
- [func additionalContent(for: URL) throws -> Any](uimanageddocument/additionalcontent(for:).md)
  Handles writing non-Core Data content to the additional content directory in the document’s file package.
- [func writeAdditionalContent(Any, to: URL, originalContentsURL: URL?) throws](uimanageddocument/writeadditionalcontent(_:to:originalcontentsurl:).md)
  Handles writing non-Core Data content to the document’s file package.
### Naming the persistent store file
- [class var persistentStoreName: String](uimanageddocument/persistentstorename.md)
  Returns the name for the persistent store file inside the document’s file package.

## Relationships

### Inherits From
- [UIDocument](uidocument.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
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

- [class UIDocument](uidocument.md)
  An abstract base class for managing discrete portions of your app’s data.
- [Synchronizing documents in the iCloud environment](synchronizing-documents-in-the-icloud-environment.md)
  Manage documents across multiple devices to create a seamless editing and collaboration experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimanageddocument)*