# options

**Framework**: Core Data  
**Kind**: property

The options that Core Data uses to create the store.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var options: [AnyHashable : Any]? { get }
```

#### Discussion

See [`NSPersistentStoreCoordinator`](nspersistentstorecoordinator.md) for a list of key names for options in this dictionary.

## See Also

- [var configurationName: String](nspersistentstore/configurationname.md)
  The name of the managed object model configuration that creates the persistent store.
- [var persistentStoreCoordinator: NSPersistentStoreCoordinator?](nspersistentstore/persistentstorecoordinator.md)
  The persistent store coordinator that loads the persistent store.
- [var type: String](nspersistentstore/type.md)
  The type string of the persistent store.
- [NSPersistentStore.StoreType](nspersistentstore/storetype.md)
  The types of persistent stores that Core Data supports.
- [Persistent Store Types](persistent-store-types.md)
  Persist data through the available store types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/options)*