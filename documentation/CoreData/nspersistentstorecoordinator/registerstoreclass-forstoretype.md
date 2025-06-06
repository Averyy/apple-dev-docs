# registerStoreClass(_:forStoreType:)

**Framework**: Core Data  
**Kind**: method

Registers a persistent store subclass using the specified store type identifier.

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
class func registerStoreClass(_ storeClass: AnyClass?, forStoreType storeType: String)
```

#### Discussion

You must invoke this method before a custom subclass of [`NSPersistentStore`](nspersistentstore.md) can be loaded into a persistent store coordinator.

You can pass `nil` for `storeClass` to unregister the store type.

## Parameters

- `storeClass`: The   subclass to use for the store of type  .
- `storeType`: A unique string that identifies a store type.

## See Also

- [class func registerStoreClass(AnyClass?, type: NSPersistentStore.StoreType)](nspersistentstorecoordinator/registerstoreclass(_:type:).md)
  Registers a persistent store subclass using the specified store type.
- [class var registeredStoreTypes: [String : NSValue]](nspersistentstorecoordinator/registeredstoretypes.md)
  The coordinator’s registered store types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/registerstoreclass(_:forstoretype:))*