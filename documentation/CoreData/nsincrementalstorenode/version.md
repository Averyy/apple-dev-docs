# version

**Framework**: Core Data  
**Kind**: property

The version of data in the receiver.

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
var version: UInt64 { get }
```

#### Discussion

The version number is used by the persistent store coordinator to detect and handle merge conflicts. The version number should be stored with the record. The version number should (implicitly) start at zero (where zero indicates an unsaved object in memory) and be incremented by exactly one every time you save. In addition, you increment the version number when you or the Core Data framework have marked the associated managed object for optimistic locking.

## See Also

- [var objectID: NSManagedObjectID](nsincrementalstorenode/objectid.md)
  The object ID that identifies the data stored by the receiver.
- [func update(withValues: [String : Any], version: UInt64)](nsincrementalstorenode/update(withvalues:version:).md)
  Update the values and version to reflect new data being saved to or loaded from the external store.
- [func value(for: NSPropertyDescription) -> Any?](nsincrementalstorenode/value(for:).md)
  Returns the value for the given property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/version)*