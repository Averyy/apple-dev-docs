# SnapshotData.SnapshotReason.returnToDefaultState

**Framework**: SwiftUI  
**Kind**: case

It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
case returnToDefaultState
```

## See Also

- [SnapshotData.SnapshotReason.appBackgrounded](snapshotdata/snapshotreason/appbackgrounded.md)
  The app transitioned from the foreground to the background.
- [SnapshotData.SnapshotReason.appScheduled](snapshotdata/snapshotreason/appscheduled.md)
  The app scheduled this snapshot.
- [SnapshotData.SnapshotReason.complicationUpdate](snapshotdata/snapshotreason/complicationupdate.md)
  The app updated the complication timeline.
- [SnapshotData.SnapshotReason.prelaunch](snapshotdata/snapshotreason/prelaunch.md)
  The system needs a snapshot for the dock, but the app has not been launched yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/snapshotdata/snapshotreason/returntodefaultstate)*