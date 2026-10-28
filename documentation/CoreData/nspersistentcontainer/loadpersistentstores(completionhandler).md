# loadPersistentStores(completionHandler:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) loadPersistentStoresWithCompletionHandler:(void (^)(NSPersistentStoreDescription *, NSError *)) block;
```

## Discussion

Once the persistent container has been initialized, you need to execute [`loadPersistentStores(completionHandler:)`](./loadpersistentstores%28completionhandler%29.md) to instruct the container to load the persistent stores and complete the creation of the Core Data stack.

Once the completion handler has fired, the stack is fully initialized and is ready for use. The completion handler will be called once for each persistent store that is created.

If there is an error in the loading of the persistent stores, the [`NSError`](../../Foundation/nserror.md) value will be populated.

## Parameters

- `block`: Once the loading of the persistent stores has completed, this block will be executed on the calling thread.

## See Also

### Managing Persistent Stores
- [var persistentStoreDescriptions: [NSPersistentStoreDescription]](./persistentstoredescriptions.md)
  The descriptions of the container’s persistent stores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer/loadpersistentstores(completionhandler:))*