# error

**Framework**: Core Data  
**Kind**: property  
**Role**: Type Property

The default merge policy for all managed object contexts.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class var error: NSMergePolicy { get }
```

```objc
@property (class, strong, readonly) NSMergePolicy * errorMergePolicy;
```

#### Discussion

If a save fails because of conflicting objects, you can find the IDs of those objects in error’s `userInfo` dictionary. Use the [`NSInsertedObjectsKey`](../nsinsertedobjectskey.md) and [`NSUpdatedObjectsKey`](../nsupdatedobjectskey.md) keys to extract the object IDs.

## See Also

### Defining Merge Policies
- [class var mergeByPropertyStoreTrump: NSMergePolicy](./mergebypropertystoretrump.md)
  A property-based merge policy that applies external changes.
- [class var mergeByPropertyObjectTrump: NSMergePolicy](./mergebypropertyobjecttrump.md)
  A property-based merge policy that applies in-memory changes.
- [class var overwrite: NSMergePolicy](./overwrite.md)
  A merge policy that overwrites the entire stored object.
- [class var rollback: NSMergePolicy](./rollback.md)
  A merge policy that discards unsaved changes.
- [Merge Policies](../merge-policies.md)
  Define standard ways to handle conflicts during a save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergepolicy/error)*