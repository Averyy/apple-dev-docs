# resolve(mergeConflicts:)

**Framework**: Core Data  
**Kind**: method

Resolves the conflicts in a given list.

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
func resolve(mergeConflicts list: [Any]) throws
```

#### Discussion

If you override this method in a subclass, you should typically invoke the superclass’s implementation in addition to performing your own operations.

## Parameters

- `list`: An array of merge conflicts (instances of  ).

## See Also

- [func resolve(constraintConflicts: [NSConstraintConflict]) throws](nsmergepolicy/resolve(constraintconflicts:).md)
  Resolves the conflicts in a given list.
- [func resolve(optimisticLockingConflicts: [NSMergeConflict]) throws](nsmergepolicy/resolve(optimisticlockingconflicts:).md)
  Resolves the conflicts in a given list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergepolicy/resolve(mergeconflicts:))*