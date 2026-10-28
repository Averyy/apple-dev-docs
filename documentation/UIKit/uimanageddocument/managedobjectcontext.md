# managedObjectContext

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The document’s managed object context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var managedObjectContext: NSManagedObjectContext { get }
```

```objc
@property (nonatomic, strong, readonly) NSManagedObjectContext * managedObjectContext;
```

## Discussion

The document automatically creates a managed object context using its persistent store coordinator.

### Special considerations

You must not use the document’s managed object context in [`writeAdditionalContent(_:to:originalContentsURL:)`](./writeadditionalcontent%28_,to,originalcontentsurl%29.md), or any of the asynchronous [`UIDocument`](../uidocument.md) methods.

## See Also

### Managing the Core Data stack
- [func configurePersistentStoreCoordinator(for: URL, ofType: String, modelConfiguration: String?, storeOptions: [AnyHashable : Any]?) throws](./configurepersistentstorecoordinator%28for,oftype,modelconfiguration,storeoptions%29.md)
  Creates or loads the document’s persistent store.
- [var managedObjectModel: NSManagedObjectModel](./managedobjectmodel.md)
  The document’s managed object model.
- [var persistentStoreOptions: [AnyHashable : Any]?](./persistentstoreoptions.md)
  Options used when creating the document’s persistent store.
- [var modelConfiguration: String?](./modelconfiguration.md)
  A model configuration name to be passed when configuring the persistent store.
- [func persistentStoreType(forFileType: String) -> String](./persistentstoretype%28forfiletype%29.md)
  Returns the Core Data store type for a given document file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimanageddocument/managedobjectcontext)*