# NSSnapshotEventType

**Framework**: Core Data  
**Kind**: struct  
**Role**: Structure

Constants that specify the reason the managed object may need to reinitialize its values.

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
struct NSSnapshotEventType
```

```c
enum NSSnapshotEventType : NSUInteger;
```

## Topics

### Event Types
- [static var undoInsertion: NSSnapshotEventType](./nssnapshoteventtype/undoinsertion.md)
  Specifies a change due to undo from insertion.
- [static var undoDeletion: NSSnapshotEventType](./nssnapshoteventtype/undodeletion.md)
  Specifies a change due to undo from deletion.
- [static var undoUpdate: NSSnapshotEventType](./nssnapshoteventtype/undoupdate.md)
  Specifies a change due to a property-level undo.
- [static var rollback: NSSnapshotEventType](./nssnapshoteventtype/rollback.md)
  Specifies a change due to the managed object context being rolled back.
- [static var refresh: NSSnapshotEventType](./nssnapshoteventtype/refresh.md)
  Specifies a change due to the managed object being refreshed.
- [static var mergePolicy: NSSnapshotEventType](./nssnapshoteventtype/mergepolicy.md)
  Specifies a change due to conflict resolution during a save operation.
### Initializers
- [init(rawValue: UInt)](./nssnapshoteventtype/init%28rawvalue%29.md)
  Creates a snapshot event using a raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nssnapshoteventtype)*