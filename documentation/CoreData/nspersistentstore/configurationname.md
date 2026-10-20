# configurationName

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The name of the managed object model configuration that creates the persistent store.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var configurationName: String { get }
```

```objc
@property (copy, readonly) NSString * configurationName;
```

## See Also

### Getting Store Configuration
- [var options: [AnyHashable : Any]?](./options.md)
  The options that Core Data uses to create the store.
- [var persistentStoreCoordinator: NSPersistentStoreCoordinator?](./persistentstorecoordinator.md)
  The persistent store coordinator that loads the persistent store.
- [var type: String](./type.md)
  The type string of the persistent store.
- [NSPersistentStore.StoreType](./storetype.md)
  The types of persistent stores that Core Data supports.
- [Persistent Store Types](../persistent-store-types.md)
  Persist data through the available store types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/configurationname)*