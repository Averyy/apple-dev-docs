# resolve(mergeConflicts:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Resolves the conflicts in a given list.

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
func resolve(mergeConflicts list: [Any]) throws
```

```objc
- (BOOL) resolveConflicts:(NSArray *) list error:(NSError **) error;
```

## Discussion

If you override this method in a subclass, you should typically invoke the superclass’s implementation in addition to performing your own operations.

## Parameters

- `list`: An array of merge conflicts (instances of [`NSMergeConflict`](../nsmergeconflict.md)).

## See Also

### Resolving a Conflict
- [func resolve(constraintConflicts: [NSConstraintConflict]) throws](./resolve%28constraintconflicts%29.md)
  Resolves the conflicts in a given list.
- [func resolve(optimisticLockingConflicts: [NSMergeConflict]) throws](./resolve%28optimisticlockingconflicts%29.md)
  Resolves the conflicts in a given list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergepolicy/resolve(mergeconflicts:))*