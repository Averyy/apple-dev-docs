# SnapshotData.SnapshotReason.complicationUpdate

**Framework**: SwiftUI  
**Kind**: case

The app updated the complication timeline.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
case complicationUpdate
```

## See Also

- [SnapshotData.SnapshotReason.appBackgrounded](snapshotdata/snapshotreason/appbackgrounded.md)
  The app transitioned from the foreground to the background.
- [SnapshotData.SnapshotReason.appScheduled](snapshotdata/snapshotreason/appscheduled.md)
  The app scheduled this snapshot.
- [SnapshotData.SnapshotReason.prelaunch](snapshotdata/snapshotreason/prelaunch.md)
  The system needs a snapshot for the dock, but the app has not been launched yet.
- [SnapshotData.SnapshotReason.returnToDefaultState](snapshotdata/snapshotreason/returntodefaultstate.md)
  It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/snapshotdata/snapshotreason/complicationupdate)*