# managedObjectContext

**Framework**: AppKit  
**Kind**: property

The managed object context for the document.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var managedObjectContext: NSManagedObjectContext? { get set }
```

#### Discussion

If a managed object context for the document does not exist, one is created automatically. If you want to customize the creation of the persistence stack, reimplement this property in your custom subclass and use your implementation to create the appropriate objects.

## See Also

- [Core Data Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
- [Document-Based App Programming Guide for Mac](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/DocBasedAppProgrammingGuideForOSX/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011179)
- [var managedObjectModel: NSManagedObjectModel?](nspersistentdocument/managedobjectmodel.md)
  The managed object model of the document.
- [func configurePersistentStoreCoordinator(for: URL, ofType: String, modelConfiguration: String?, storeOptions: [String : Any]?) throws](nspersistentdocument/configurepersistentstorecoordinator(for:oftype:modelconfiguration:storeoptions:).md)
  Configures the receiver’s persistent store coordinator with the appropriate stores for a given URL.
- [func persistentStoreType(forFileType: String) -> String](nspersistentdocument/persistentstoretype(forfiletype:).md)
  Returns the type of persistent store associated with the specified file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspersistentdocument/managedobjectcontext)*