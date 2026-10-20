# modelConfiguration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A model configuration name to be passed when configuring the persistent store.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var modelConfiguration: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * modelConfiguration;
```

#### Discussion

By default, this value is `nil`.

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
- [func persistentStoreType(forFileType: String) -> String](./persistentstoretype%28forfiletype%29.md)
  Returns the Core Data store type for a given document file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimanageddocument/modelconfiguration)*