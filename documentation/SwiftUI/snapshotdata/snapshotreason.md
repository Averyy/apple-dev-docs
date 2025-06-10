# SnapshotData.SnapshotReason

**Framework**: SwiftUI  
**Kind**: enum

The reason for a background snapshot task.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
enum SnapshotReason
```

## Topics

### Getting the snapshot reasons
- [SnapshotData.SnapshotReason.appBackgrounded](snapshotdata/snapshotreason/appbackgrounded.md)
  The app transitioned from the foreground to the background.
- [SnapshotData.SnapshotReason.appScheduled](snapshotdata/snapshotreason/appscheduled.md)
  The app scheduled this snapshot.
- [SnapshotData.SnapshotReason.complicationUpdate](snapshotdata/snapshotreason/complicationupdate.md)
  The app updated the complication timeline.
- [SnapshotData.SnapshotReason.prelaunch](snapshotdata/snapshotreason/prelaunch.md)
  The system needs a snapshot for the dock, but the app has not been launched yet.
- [SnapshotData.SnapshotReason.returnToDefaultState](snapshotdata/snapshotreason/returntodefaultstate.md)
  It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let identifier: String?](snapshotdata/identifier.md)
  The identifier associated with this snapshot request.
- [let reason: SnapshotData.SnapshotReason](snapshotdata/reason.md)
  The reason for a background snapshot task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/snapshotdata/snapshotreason)*