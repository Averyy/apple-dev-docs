# NSSnapshotEventType

**Framework**: Core Data  
**Kind**: struct

Constants that specify the reason the managed object may need to reinitialize its values.

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
struct NSSnapshotEventType
```

## Topics

### Event Types
- [static var undoInsertion: NSSnapshotEventType](nssnapshoteventtype/undoinsertion.md)
  Specifies a change due to undo from insertion.
- [static var undoDeletion: NSSnapshotEventType](nssnapshoteventtype/undodeletion.md)
  Specifies a change due to undo from deletion.
- [static var undoUpdate: NSSnapshotEventType](nssnapshoteventtype/undoupdate.md)
  Specifies a change due to a property-level undo.
- [static var rollback: NSSnapshotEventType](nssnapshoteventtype/rollback.md)
  Specifies a change due to the managed object context being rolled back.
- [static var refresh: NSSnapshotEventType](nssnapshoteventtype/refresh.md)
  Specifies a change due to the managed object being refreshed.
- [static var mergePolicy: NSSnapshotEventType](nssnapshoteventtype/mergepolicy.md)
  Specifies a change due to conflict resolution during a save operation.
### Initializers
- [init(rawValue: UInt)](nssnapshoteventtype/init(rawvalue:).md)
  Creates a snapshot event using a raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nssnapshoteventtype)*