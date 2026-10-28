# persistentStoreType(forFileType:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the Core Data store type for a given document file type.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func persistentStoreType(forFileType fileType: String) -> String
```

```objc
- (NSString *) persistentStoreTypeForFileType:(NSString *) fileType;
```

## Return Value

The persistent store type for `fileType`.

## Discussion

Override this method to specify a persistent store type for a given document type.

The default returns [`NSSQLiteStoreType`](../../CoreData/nssqlitestoretype.md).

## Parameters

- `fileType`: The document file type.

## See Also

### Managing the Core Data stack
- [func configurePersistentStoreCoordinator(for: URL, ofType: String, modelConfiguration: String?, storeOptions: [AnyHashable : Any]?) throws](./configurepersistentstorecoordinator%28for,oftype,modelconfiguration,storeoptions%29.md)
  Creates or loads the document’s persistent store.
- [var managedObjectContext: NSManagedObjectContext](./managedobjectcontext.md)
  The document’s managed object context.
- [var managedObjectModel: NSManagedObjectModel](./managedobjectmodel.md)
  The document’s managed object model.
- [var persistentStoreOptions: [AnyHashable : Any]?](./persistentstoreoptions.md)
  Options used when creating the document’s persistent store.
- [var modelConfiguration: String?](./modelconfiguration.md)
  A model configuration name to be passed when configuring the persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimanageddocument/persistentstoretype(forfiletype:))*