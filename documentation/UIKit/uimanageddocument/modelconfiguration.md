# modelConfiguration

**Framework**: UIKit  
**Kind**: property

A model configuration name to be passed when configuring the persistent store.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var modelConfiguration: String? { get set }
```

#### Discussion

By default, this value is `nil`.

## See Also

- [func configurePersistentStoreCoordinator(for: URL, ofType: String, modelConfiguration: String?, storeOptions: [AnyHashable : Any]?) throws](uimanageddocument/configurepersistentstorecoordinator(for:oftype:modelconfiguration:storeoptions:).md)
  Creates or loads the document’s persistent store.
- [var managedObjectContext: NSManagedObjectContext](uimanageddocument/managedobjectcontext.md)
  The document’s managed object context.
- [var managedObjectModel: NSManagedObjectModel](uimanageddocument/managedobjectmodel.md)
  The document’s managed object model.
- [var persistentStoreOptions: [AnyHashable : Any]?](uimanageddocument/persistentstoreoptions.md)
  Options used when creating the document’s persistent store.
- [func persistentStoreType(forFileType: String) -> String](uimanageddocument/persistentstoretype(forfiletype:).md)
  Returns the Core Data store type for a given document file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimanageddocument/modelconfiguration)*