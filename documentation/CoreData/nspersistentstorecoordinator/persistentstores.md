# persistentStores

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The coordinator’s persistent stores.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var persistentStores: [NSPersistentStore] { get }
```

```objc
@property (strong, readonly) NSArray<__kindof NSPersistentStore *> * persistentStores;
```

## See Also

### Managing configuration
- [var name: String?](./name.md)
  The coordinator’s name.
- [var managedObjectModel: NSManagedObjectModel](./managedobjectmodel.md)
  The coordinator’s managed object model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/persistentstores)*