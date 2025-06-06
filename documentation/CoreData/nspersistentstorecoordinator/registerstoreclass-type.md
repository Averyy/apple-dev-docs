# registerStoreClass(_:type:)

**Framework**: Core Data  
**Kind**: method

Registers a persistent store subclass using the specified store type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
class func registerStoreClass(_ storeClass: AnyClass?, type: NSPersistentStore.StoreType)
```

#### Discussion

You must register the subclass before you load instances of it into the persistent store coordinator. To unregister a subclass for a specific store type, use `nil` for `storeClass`.

## Parameters

- `storeClass`: A subclass of  .
- `type`: The store type. For possible values, see  .

## See Also

- [class func registerStoreClass(AnyClass?, forStoreType: String)](nspersistentstorecoordinator/registerstoreclass(_:forstoretype:).md)
  Registers a persistent store subclass using the specified store type identifier.
- [class var registeredStoreTypes: [String : NSValue]](nspersistentstorecoordinator/registeredstoretypes.md)
  The coordinator’s registered store types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/registerstoreclass(_:type:))*