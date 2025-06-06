# persistentStoreDescriptions

**Framework**: Core Data  
**Kind**: property

The descriptions of the container’s persistent stores.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var persistentStoreDescriptions: [NSPersistentStoreDescription] { get set }
```

#### Discussion

If you want to override the type (or types) of persistent store(s) used by the persistent container, you can set this property with an array of [`NSPersistentStoreDescription`](nspersistentstoredescription.md) objects.

If you will be configuring custom persistent store descriptions, you must set this property before calling [`loadPersistentStores(completionHandler:)`](nspersistentcontainer/loadpersistentstores(completionhandler:).md).

## See Also

- [func loadPersistentStores(completionHandler: (NSPersistentStoreDescription, (any Error)?) -> Void)](nspersistentcontainer/loadpersistentstores(completionhandler:).md)
  Loads the persistent stores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer/persistentstoredescriptions)*