# cachedSnapshot

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A dictionary containing the values of the source object held in the persistent store coordinator layer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var cachedSnapshot: [String : Any]? { get }
```

```objc
@property (retain, readonly, nullable) NSDictionary<NSString *,id> * cachedSnapshot;
```

## See Also

### Accessing Merge Conflict Details
- [var sourceObject: NSManagedObject](./sourceobject.md)
  The source object for the conflict.
- [var objectSnapshot: [String : Any]?](./objectsnapshot.md)
  A dictionary containing the values of the source object.
- [var persistedSnapshot: [String : Any]?](./persistedsnapshot.md)
  A dictionary containing the values of the source object held in the persistent store.
- [var newVersionNumber: Int](./newversionnumber.md)
  The new version number for the change.
- [var oldVersionNumber: Int](./oldversionnumber.md)
  The old version number for the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergeconflict/cachedsnapshot)*