# init(source:newVersion:oldVersion:cachedSnapshot:persistedSnapshot:)

**Framework**: Core Data  
**Kind**: init

Initializes a merge conflict.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(source srcObject: NSManagedObject, newVersion newvers: Int, oldVersion oldvers: Int, cachedSnapshot cachesnap: [String : Any]?, persistedSnapshot persnap: [String : Any]?)
```

#### Return Value

A merge conflict object initialized with the given parameters.

## Parameters

- `srcObject`: The source object for the conflict.
- `newvers`: A value of 0 means the object was deleted and the corresponding snapshot is  .
- `oldvers`: The old version number for the change.
- `cachesnap`: A dictionary containing the values of   held in the persistent store coordinator layer.
- `persnap`: A dictionary containing the values of   held in the persistent store.

## See Also

- [Core Data Model Versioning and Data Migration Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/Introduction.html#//apple_ref/doc/uid/TP40004399)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergeconflict/init(source:newversion:oldversion:cachedsnapshot:persistedsnapshot:))*