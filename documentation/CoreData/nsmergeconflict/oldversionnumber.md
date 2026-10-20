# oldVersionNumber

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The old version number for the change.

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
var oldVersionNumber: Int { get }
```

```objc
@property (readonly) NSUInteger oldVersionNumber;
```

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
- [var newVersionNumber: Int](./newversionnumber.md)
  The new version number for the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergeconflict/oldversionnumber)*