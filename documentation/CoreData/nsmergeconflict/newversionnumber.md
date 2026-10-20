# newVersionNumber

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The new version number for the change.

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
var newVersionNumber: Int { get }
```

```objc
@property (readonly) NSUInteger newVersionNumber;
```

#### Discussion

A new version number of 0 means the object was deleted and the corresponding snapshot is `nil`.

## See Also

### Accessing Merge Conflict Details
- [var sourceObject: NSManagedObject](./sourceobject.md)
  The source object for the conflict.
- [var objectSnapshot: [String : Any]?](./objectsnapshot.md)
  A dictionary containing the values of the source object.
- [var cachedSnapshot: [String : Any]?](./cachedsnapshot.md)
  A dictionary containing the values of the source object held in the persistent store coordinator layer.
- [var persistedSnapshot: [String : Any]?](./persistedsnapshot.md)
  A dictionary containing the values of the source object held in the persistent store.
- [var oldVersionNumber: Int](./oldversionnumber.md)
  The old version number for the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergeconflict/newversionnumber)*