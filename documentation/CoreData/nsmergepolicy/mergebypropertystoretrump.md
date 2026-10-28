# mergeByPropertyStoreTrump

**Framework**: Core Data  
**Kind**: property  
**Role**: Type Property

A property-based merge policy that applies external changes.

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
class var mergeByPropertyStoreTrump: NSMergePolicy { get }
```

```objc
@property (class, strong, readonly) NSMergePolicy * mergeByPropertyStoreTrumpMergePolicy;
```

## Discussion

A policy that merges conflicts between the persistent store’s version of the object and the current in-memory version by individual property, with external changes trumping in-memory changes.

## See Also

### Defining Merge Policies
- [class var error: NSMergePolicy](./error.md)
  The default merge policy for all managed object contexts.
- [class var mergeByPropertyObjectTrump: NSMergePolicy](./mergebypropertyobjecttrump.md)
  A property-based merge policy that applies in-memory changes.
- [class var overwrite: NSMergePolicy](./overwrite.md)
  A merge policy that overwrites the entire stored object.
- [class var rollback: NSMergePolicy](./rollback.md)
  A merge policy that discards unsaved changes.
- [Merge Policies](../merge-policies.md)
  Define standard ways to handle conflicts during a save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergepolicy/mergebypropertystoretrump)*