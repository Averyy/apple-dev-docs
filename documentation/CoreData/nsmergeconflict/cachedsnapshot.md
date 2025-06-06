# cachedSnapshot

**Framework**: Core Data  
**Kind**: property

A dictionary containing the values of the source object held in the persistent store coordinator layer.

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
var cachedSnapshot: [String : Any]? { get }
```

## See Also

- [var sourceObject: NSManagedObject](nsmergeconflict/sourceobject.md)
  The source object for the conflict.
- [var objectSnapshot: [String : Any]?](nsmergeconflict/objectsnapshot.md)
  A dictionary containing the values of the source object.
- [var persistedSnapshot: [String : Any]?](nsmergeconflict/persistedsnapshot.md)
  A dictionary containing the values of the source object held in the persistent store.
- [var newVersionNumber: Int](nsmergeconflict/newversionnumber.md)
  The new version number for the change.
- [var oldVersionNumber: Int](nsmergeconflict/oldversionnumber.md)
  The old version number for the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergeconflict/cachedsnapshot)*