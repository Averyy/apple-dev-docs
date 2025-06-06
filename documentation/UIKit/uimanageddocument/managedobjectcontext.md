# managedObjectContext

**Framework**: UIKit  
**Kind**: property

The document’s managed object context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var managedObjectContext: NSManagedObjectContext { get }
```

#### Discussion

The document automatically creates a managed object context using its persistent store coordinator.

##### Special Considerations

You must not use the document’s managed object context in [`writeAdditionalContent(_:to:originalContentsURL:)`](uimanageddocument/writeadditionalcontent(_:to:originalcontentsurl:).md), or any of the asynchronous [`UIDocument`](uidocument.md) methods.

## See Also

- [func configurePersistentStoreCoordinator(for: URL, ofType: String, modelConfiguration: String?, storeOptions: [AnyHashable : Any]?) throws](uimanageddocument/configurepersistentstorecoordinator(for:oftype:modelconfiguration:storeoptions:).md)
  Creates or loads the document’s persistent store.
- [var managedObjectModel: NSManagedObjectModel](uimanageddocument/managedobjectmodel.md)
  The document’s managed object model.
- [var persistentStoreOptions: [AnyHashable : Any]?](uimanageddocument/persistentstoreoptions.md)
  Options used when creating the document’s persistent store.
- [var modelConfiguration: String?](uimanageddocument/modelconfiguration.md)
  A model configuration name to be passed when configuring the persistent store.
- [func persistentStoreType(forFileType: String) -> String](uimanageddocument/persistentstoretype(forfiletype:).md)
  Returns the Core Data store type for a given document file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimanageddocument/managedobjectcontext)*