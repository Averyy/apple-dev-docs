# managedObjectModel

**Framework**: UIKit  
**Kind**: property

The document’s managed object model.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var managedObjectModel: NSManagedObjectModel { get }
```

#### Discussion

Persistent documents always have a managed object model. The default model is the union of all models in the main bundle. You can specify a configuration to use with [`modelConfiguration`](uimanageddocument/modelconfiguration.md). You can subclass [`UIManagedDocument`](uimanageddocument.md) to override this method if you need custom behavior.

## See Also

- [func configurePersistentStoreCoordinator(for: URL, ofType: String, modelConfiguration: String?, storeOptions: [AnyHashable : Any]?) throws](uimanageddocument/configurepersistentstorecoordinator(for:oftype:modelconfiguration:storeoptions:).md)
  Creates or loads the document’s persistent store.
- [var managedObjectContext: NSManagedObjectContext](uimanageddocument/managedobjectcontext.md)
  The document’s managed object context.
- [var persistentStoreOptions: [AnyHashable : Any]?](uimanageddocument/persistentstoreoptions.md)
  Options used when creating the document’s persistent store.
- [var modelConfiguration: String?](uimanageddocument/modelconfiguration.md)
  A model configuration name to be passed when configuring the persistent store.
- [func persistentStoreType(forFileType: String) -> String](uimanageddocument/persistentstoretype(forfiletype:).md)
  Returns the Core Data store type for a given document file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimanageddocument/managedobjectmodel)*