# configurePersistentStoreCoordinator(for:ofType:modelConfiguration:storeOptions:)

**Framework**: Appkit  
**Kind**: method

Configures the receiver’s persistent store coordinator with the appropriate stores for a given URL.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func configurePersistentStoreCoordinator(for url: URL, ofType fileType: String, modelConfiguration configuration: String?, storeOptions: [String : Any]? = nil) throws
```

#### Discussion

This method is invoked automatically when an existing document is opened. You override this method to customize creation of a persistent store for a given document or store type. You can retrieve the persistent store coordinator with the following code:

```objc
[[self managedObjectContext] persistentStoreCoordinator];
```

You can override this method to create the store to save to or load from (invoked from within the other `NSDocument` methods to read/write files), which gives developers the ability to load/save from/to different persistent store types (default type is XML).

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: An URL that specifies the location of the document’s store.
- `fileType`: The document type.
- `configuration`: The name of the managed object model configuration to use. (The managed object model is associated with the persistent store coordinator.) Pass   if you do not want to specify a configuration.
- `storeOptions`: Options for the store. See “Store Options” in   for possible values.

## See Also

- [var managedObjectContext: NSManagedObjectContext?](nspersistentdocument/managedobjectcontext.md)
  The managed object context for the document.
- [var managedObjectModel: NSManagedObjectModel?](nspersistentdocument/managedobjectmodel.md)
  The managed object model of the document.
- [func persistentStoreType(forFileType: String) -> String](nspersistentdocument/persistentstoretype(forfiletype:).md)
  Returns the type of persistent store associated with the specified file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspersistentdocument/configurepersistentstorecoordinator(for:oftype:modelconfiguration:storeoptions:))*