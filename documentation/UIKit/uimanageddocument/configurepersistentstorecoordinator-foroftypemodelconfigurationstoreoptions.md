# configurePersistentStoreCoordinator(for:ofType:modelConfiguration:storeOptions:)

**Framework**: UIKit  
**Kind**: method

Creates or loads the document’s persistent store.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func configurePersistentStoreCoordinator(for storeURL: URL, ofType fileType: String, modelConfiguration configuration: String?, storeOptions: [AnyHashable : Any]? = nil) throws
```

#### Discussion

You can override this method if you want customize the creation or loading of the document’s persistent store. For example, you can perform post-migration clean-up — if your app needs to migrate store data to use a new version of the managed object model, you can override this method to make additional modifications to the store after migration.

> **Note**:  In Swift, this method is marked with the `throws` keyword to indicate that it throws an error in cases of failure. When overriding this method, use the `throw` statement to throw an `NSError`, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `storeURL`: The URL for the persistent store.
- `fileType`: The document’s file type.
- `configuration`: The managed object model configuration to use.
- `storeOptions`: The options used to configure the persistent store coordinator.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimanageddocument/configurepersistentstorecoordinator(for:oftype:modelconfiguration:storeoptions:))*