# resolve(constraintConflicts:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Resolves the conflicts in a given list.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func resolve(constraintConflicts list: [NSConstraintConflict]) throws
```

```objc
- (BOOL) resolveConstraintConflicts:(NSArray<NSConstraintConflict *> *) list error:(NSError **) error;
```

## See Also

### Resolving a Conflict
- [func resolve(mergeConflicts: [Any]) throws](./resolve%28mergeconflicts%29.md)
  Resolves the conflicts in a given list.
- [func resolve(optimisticLockingConflicts: [NSMergeConflict]) throws](./resolve%28optimisticlockingconflicts%29.md)
  Resolves the conflicts in a given list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergepolicy/resolve(constraintconflicts:))*