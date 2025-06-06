# undoDeletion

**Framework**: Core Data  
**Kind**: property

Specifies a change due to undo from deletion.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static var undoDeletion: NSSnapshotEventType { get }
```

## See Also

- [static var undoInsertion: NSSnapshotEventType](nssnapshoteventtype/undoinsertion.md)
  Specifies a change due to undo from insertion.
- [static var undoUpdate: NSSnapshotEventType](nssnapshoteventtype/undoupdate.md)
  Specifies a change due to a property-level undo.
- [static var rollback: NSSnapshotEventType](nssnapshoteventtype/rollback.md)
  Specifies a change due to the managed object context being rolled back.
- [static var refresh: NSSnapshotEventType](nssnapshoteventtype/refresh.md)
  Specifies a change due to the managed object being refreshed.
- [static var mergePolicy: NSSnapshotEventType](nssnapshoteventtype/mergepolicy.md)
  Specifies a change due to conflict resolution during a save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nssnapshoteventtype/undodeletion)*