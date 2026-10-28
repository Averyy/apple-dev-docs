# NSMergePolicy

**Framework**: Core Data  
**Kind**: class  
**Role**: Class

A policy object that you use to resolve conflicts between the persistent store and in-memory versions of managed objects.

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
class NSMergePolicy
```

```objc
@interface NSMergePolicy : NSObject
```

## Overview

A conflict is a mismatch between state held at two different layers in the Core Data stack. A conflict can arise when you save a managed object context and you have stale data at another layer. There are two places in which a conflict may occur:

- Between the managed object context layer and its in-memory cached state at the persistent store coordinator layer.
- Between the cached state at the persistent store coordinator and the external store (file, database, and so forth).

Conflicts are represented by instances of [`NSMergeConflict`](./nsmergeconflict.md).

## Topics

### Getting a Merge Policy
- [init(merge: NSMergePolicyType)](./nsmergepolicy/init%28merge%29.md)
  Returns a merge policy initialized with a given policy type.
- [var mergeType: NSMergePolicyType](./nsmergepolicy/mergetype.md)
  The merge type.
### Resolving a Conflict
- [func resolve(mergeConflicts: [Any]) throws](./nsmergepolicy/resolve%28mergeconflicts%29.md)
  Resolves the conflicts in a given list.
- [func resolve(constraintConflicts: [NSConstraintConflict]) throws](./nsmergepolicy/resolve%28constraintconflicts%29.md)
  Resolves the conflicts in a given list.
- [func resolve(optimisticLockingConflicts: [NSMergeConflict]) throws](./nsmergepolicy/resolve%28optimisticlockingconflicts%29.md)
  Resolves the conflicts in a given list.
### Defining Merge Policies
- [class var error: NSMergePolicy](./nsmergepolicy/error.md)
  The default merge policy for all managed object contexts.
- [class var mergeByPropertyStoreTrump: NSMergePolicy](./nsmergepolicy/mergebypropertystoretrump.md)
  A property-based merge policy that applies external changes.
- [class var mergeByPropertyObjectTrump: NSMergePolicy](./nsmergepolicy/mergebypropertyobjecttrump.md)
  A property-based merge policy that applies in-memory changes.
- [class var overwrite: NSMergePolicy](./nsmergepolicy/overwrite.md)
  A merge policy that overwrites the entire stored object.
- [class var rollback: NSMergePolicy](./nsmergepolicy/rollback.md)
  A merge policy that discards unsaved changes.
- [Merge Policies](./merge-policies.md)
  Define standard ways to handle conflicts during a save operation.
### Initializers
- [init(mergeType: NSMergePolicyType)](./nsmergepolicy/init%28mergetype%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Conflict Management
- [class NSConstraintConflict](./nsconstraintconflict.md)
  An encapsulation of conflicts that occur during an attempt to save a managed object.
- [class NSMergeConflict](./nsmergeconflict.md)
  An encapsulation of conflicts that occur during an attempt to save changes in a managed object context.
- [class NSQueryGenerationToken](./nsquerygenerationtoken.md)
  A token that indicates which generation of the persistent store is being accessed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergepolicy)*