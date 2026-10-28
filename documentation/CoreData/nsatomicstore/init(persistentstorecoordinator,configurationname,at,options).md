# init(persistentStoreCoordinator:configurationName:at:options:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Creates an atomic store at the specified location.

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
init(persistentStoreCoordinator coordinator: NSPersistentStoreCoordinator?, configurationName: String?, at url: URL, options: [AnyHashable : Any]? = nil)
```

```objc
- (instancetype) initWithPersistentStoreCoordinator:(NSPersistentStoreCoordinator *) coordinator configurationName:(NSString *) configurationName URL:(NSURL *) url options:(NSDictionary *) options;
```

## Discussion

Typically, you don’t invoke this method yourself; instead, the persistent store coordinator invokes the method when it creates a new store or adds an existing one.

In your implementation, check whether a file exists at `url`. If it doesn’t exist, create a zero-length file at `url` so that the file exists before the coordinator calls the store’s [`load()`](./load%28%29.md) method. A zero-length file indicates to the system that it should create a new store at that location. If the coordinator removes the store without first calling [`save()`](./save%28%29.md), delete the zero-length file.

It’s your responsibility to load the store’s metadata during initialization and set it using the [`setMetadata(_:forPersistentStoreAt:)`](../nspersistentstore/setmetadata%28_,forpersistentstoreat%29.md) method.

> ❗ **Important**:  If you override this method, you must invoke the superclass implementation to ensure that Core Data correctly initializes the store.

## Parameters

- `coordinator`: The persistent store coordinator.
- `configurationName`: The name of the store’s configuration in the managed object model.
- `url`: The URL of the store to load. This value can’t be `nil`.
- `options`: A dictionary that contains the store’s options. For possible values, see [Store options](../store-options.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstore/init(persistentstorecoordinator:configurationname:at:options:))*