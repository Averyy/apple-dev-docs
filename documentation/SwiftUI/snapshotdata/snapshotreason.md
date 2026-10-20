# SnapshotData.SnapshotReason

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

The reason for a background snapshot task.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
enum SnapshotReason
```

## Topics

### Getting the snapshot reasons
- [SnapshotData.SnapshotReason.appBackgrounded](./snapshotreason/appbackgrounded.md)
  The app transitioned from the foreground to the background.
- [SnapshotData.SnapshotReason.appScheduled](./snapshotreason/appscheduled.md)
  The app scheduled this snapshot.
- [SnapshotData.SnapshotReason.complicationUpdate](./snapshotreason/complicationupdate.md)
  The app updated the complication timeline.
- [SnapshotData.SnapshotReason.prelaunch](./snapshotreason/prelaunch.md)
  The system needs a snapshot for the dock, but the app has not been launched yet.
- [SnapshotData.SnapshotReason.returnToDefaultState](./snapshotreason/returntodefaultstate.md)
  It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the data
- [let identifier: String?](./identifier.md)
  The identifier associated with this snapshot request.
- [let reason: SnapshotData.SnapshotReason](./reason.md)
  The reason for a background snapshot task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/snapshotdata/snapshotreason)*