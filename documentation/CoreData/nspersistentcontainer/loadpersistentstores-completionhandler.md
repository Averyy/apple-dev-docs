# loadPersistentStores(completionHandler:)

**Framework**: Core Data  
**Kind**: method

Loads the persistent stores.

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
func loadPersistentStores(completionHandler block: @escaping (NSPersistentStoreDescription, (any Error)?) -> Void)
```

#### Discussion

Once the persistent container has been initialized, you need to execute [`loadPersistentStores(completionHandler:)`](nspersistentcontainer/loadpersistentstores(completionhandler:).md) to instruct the container to load the persistent stores and complete the creation of the Core Data stack.

Once the completion handler has fired, the stack is fully initialized and is ready for use. The completion handler will be called once for each persistent store that is created.

If there is an error in the loading of the persistent stores, the [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) value will be populated.

## Parameters

- `block`: Once the loading of the persistent stores has completed, this block will be executed on the calling thread.

## See Also

- [var persistentStoreDescriptions: [NSPersistentStoreDescription]](nspersistentcontainer/persistentstoredescriptions.md)
  The descriptions of the container’s persistent stores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer/loadpersistentstores(completionhandler:))*