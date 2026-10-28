# registerStoreClass(_:forStoreType:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

Registers a persistent store subclass using the specified store type identifier.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

> **Deprecated**: Use [`registerStoreClass(_:type:)`](./registerstoreclass%28_,type%29.md) instead.

## Declaration

```swift
class func registerStoreClass(_ storeClass: AnyClass?, forStoreType storeType: String)
```

```objc
+ (void) registerStoreClass:(Class) storeClass forStoreType:(NSString *) storeType;
```

## Discussion

You must invoke this method before a custom subclass of [`NSPersistentStore`](../nspersistentstore.md) can be loaded into a persistent store coordinator.

You can pass `nil` for `storeClass` to unregister the store type.

## Parameters

- `storeClass`: The `NSPersistentStore` subclass to use for the store of type `storeType`.
- `storeType`: A unique string that identifies a store type.

## See Also

### Registering store types
- [class func registerStoreClass(AnyClass?, type: NSPersistentStore.StoreType)](./registerstoreclass%28_,type%29.md)
  Registers a persistent store subclass using the specified store type.
- [class var registeredStoreTypes: [String : NSValue]](./registeredstoretypes.md)
  The coordinator’s registered store types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/registerstoreclass(_:forstoretype:))*