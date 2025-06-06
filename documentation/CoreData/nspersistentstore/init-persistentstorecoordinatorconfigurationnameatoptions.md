# init(persistentStoreCoordinator:configurationName:at:options:)

**Framework**: Core Data  
**Kind**: init

Returns a store initialized with the given arguments.

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
init(persistentStoreCoordinator root: NSPersistentStoreCoordinator?, configurationName name: String?, at url: URL, options: [AnyHashable : Any]? = nil)
```

#### Return Value

A new store object, associated with `coordinator`, that represents a persistent store at url using the options in `options` and—if it is not `nil`—the managed object model configuration `configurationName`.

#### Discussion

You must ensure that you load metadata during initialization and set it using [`metadata`](nspersistentstore/metadata.md).

##### Special Considerations

This is the designated initializer for persistent stores.

## Parameters

- `root`: A persistent store coordinator.
- `name`: The name of the managed object model configuration to use. Pass   if you do not want to specify a configuration.
- `url`: The URL of the store to load.
- `options`: A dictionary containing configuration options. See   for a list of key names for options in this dictionary.

## See Also

- [var metadata: [String : Any]!](nspersistentstore/metadata.md)
  The metadata for the persistent store.
- [Core Data Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
- [Atomic Store Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AtomicStore_Concepts/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004521)
- [Incremental Store Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/IncrementalStorePG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010706)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstore/init(persistentstorecoordinator:configurationname:at:options:))*