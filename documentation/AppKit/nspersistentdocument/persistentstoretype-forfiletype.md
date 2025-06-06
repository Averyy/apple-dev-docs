# persistentStoreType(forFileType:)

**Framework**: AppKit  
**Kind**: method

Returns the type of persistent store associated with the specified file type.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func persistentStoreType(forFileType fileType: String) -> String
```

#### Return Value

The type of persistent store associated with `fileType`. For possible values, see [`NSPersistentStoreCoordinator`](https://developer.apple.com/documentation/CoreData/NSPersistentStoreCoordinator).

#### Discussion

You set the persistent store type in the application’s property list.

## Parameters

- `fileType`: A document file type.

## See Also

- [var managedObjectContext: NSManagedObjectContext?](nspersistentdocument/managedobjectcontext.md)
  The managed object context for the document.
- [var managedObjectModel: NSManagedObjectModel?](nspersistentdocument/managedobjectmodel.md)
  The managed object model of the document.
- [func configurePersistentStoreCoordinator(for: URL, ofType: String, modelConfiguration: String?, storeOptions: [String : Any]?) throws](nspersistentdocument/configurepersistentstorecoordinator(for:oftype:modelconfiguration:storeoptions:).md)
  Configures the receiver’s persistent store coordinator with the appropriate stores for a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspersistentdocument/persistentstoretype(forfiletype:))*