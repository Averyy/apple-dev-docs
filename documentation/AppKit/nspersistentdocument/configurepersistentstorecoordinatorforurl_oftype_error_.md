# configurePersistentStoreCoordinatorForURL:ofType:error:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Configures the receiver’s persistent store coordinator for a given URL and document type.

**Availability**:
- macOS 10.4+ - Deprecated in 10.5

> **Deprecated**: Use [`configurePersistentStoreCoordinator(for:ofType:modelConfiguration:storeOptions:)`](./configurepersistentstorecoordinator%28for,oftype,modelconfiguration,storeoptions%29.md) instead.

## Declaration

```objc
- (BOOL) configurePersistentStoreCoordinatorForURL:(NSURL *) url ofType:(NSString *) fileType error:(NSError **) error;
```

#### Return Value

[`true`](../../Swift/true.md) if the method completes successfully, otherwise [`false`](../../Swift/false.md).

#### Discussion

This method is invoked automatically when an existing document is opened. You override this method to customize creation of a persistent store for a given document or store type. You can retrieve the persistent store coordinator with the following code:

```objc
[[self managedObjectContext] persistentStoreCoordinator];
```

## Parameters

- `url`: An URL that specifies the location of the document’s store.
- `fileType`: The document type.
- `error`: If the method does not complete successfully, upon return contains an `NSError` object that describes the problem.

## See Also

### Related Documentation
- [func configurePersistentStoreCoordinator(for: URL, ofType: String, modelConfiguration: String?, storeOptions: [String : Any]?) throws](./configurepersistentstorecoordinator%28for,oftype,modelconfiguration,storeoptions%29.md)
  Configures the receiver’s persistent store coordinator with the appropriate stores for a given URL.
- [func persistentStoreType(forFileType: String) -> String](./persistentstoretype%28forfiletype%29.md)
  Returns the type of persistent store associated with the specified file type.
### Managing the Persistence Objects
- [var managedObjectContext: NSManagedObjectContext?](./managedobjectcontext.md)
  The managed object context for the document.
- [var managedObjectModel: NSManagedObjectModel?](./managedobjectmodel.md)
  The managed object model of the document.
- [func configurePersistentStoreCoordinator(for: URL, ofType: String, modelConfiguration: String?, storeOptions: [String : Any]?) throws](./configurepersistentstorecoordinator%28for,oftype,modelconfiguration,storeoptions%29.md)
  Configures the receiver’s persistent store coordinator with the appropriate stores for a given URL.
- [func persistentStoreType(forFileType: String) -> String](./persistentstoretype%28forfiletype%29.md)
  Returns the type of persistent store associated with the specified file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspersistentdocument/configurepersistentstorecoordinatorforurl:oftype:error:)*