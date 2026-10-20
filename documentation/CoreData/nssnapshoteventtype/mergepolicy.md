# mergePolicy

**Framework**: Core Data  
**Kind**: property  
**Role**: Type Property

Specifies a change due to conflict resolution during a save operation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
static var mergePolicy: NSSnapshotEventType { get }
```

```c
NSSnapshotEventMergePolicy
```

## See Also

### Event Types
- [static var undoInsertion: NSSnapshotEventType](./undoinsertion.md)
  Specifies a change due to undo from insertion.
- [static var undoDeletion: NSSnapshotEventType](./undodeletion.md)
  Specifies a change due to undo from deletion.
- [static var undoUpdate: NSSnapshotEventType](./undoupdate.md)
  Specifies a change due to a property-level undo.
- [static var rollback: NSSnapshotEventType](./rollback.md)
  Specifies a change due to the managed object context being rolled back.
- [static var refresh: NSSnapshotEventType](./refresh.md)
  Specifies a change due to the managed object being refreshed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nssnapshoteventtype/mergepolicy)*