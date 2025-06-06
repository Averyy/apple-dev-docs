# registeredStoreTypes

**Framework**: Core Data  
**Kind**: property

The coordinator’s registered store types.

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
class var registeredStoreTypes: [String : NSValue] { get }
```

#### Return Value

A dictionary of the registered store types—the keys are the store type strings, and the values are the [`NSPersistentStore`](nspersistentstore.md) subclasses.

## See Also

- [class func registerStoreClass(AnyClass?, type: NSPersistentStore.StoreType)](nspersistentstorecoordinator/registerstoreclass(_:type:).md)
  Registers a persistent store subclass using the specified store type.
- [class func registerStoreClass(AnyClass?, forStoreType: String)](nspersistentstorecoordinator/registerstoreclass(_:forstoretype:).md)
  Registers a persistent store subclass using the specified store type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/registeredstoretypes)*