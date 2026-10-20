# rollback

**Framework**: Core Data  
**Kind**: property  
**Role**: Type Property

A merge policy that discards unsaved changes.

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
class var rollback: NSMergePolicy { get }
```

```objc
@property (class, strong, readonly) NSMergePolicy * rollbackMergePolicy;
```

#### Discussion

This policy merges conflicts between the persistent store’s version of the object and the current in-memory version by discarding unsaved changes.

## See Also

### Defining Merge Policies
- [class var error: NSMergePolicy](./error.md)
  The default merge policy for all managed object contexts.
- [class var mergeByPropertyStoreTrump: NSMergePolicy](./mergebypropertystoretrump.md)
  A property-based merge policy that applies external changes.
- [class var mergeByPropertyObjectTrump: NSMergePolicy](./mergebypropertyobjecttrump.md)
  A property-based merge policy that applies in-memory changes.
- [class var overwrite: NSMergePolicy](./overwrite.md)
  A merge policy that overwrites the entire stored object.
- [Merge Policies](../merge-policies.md)
  Define standard ways to handle conflicts during a save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergepolicy/rollback)*