# SnapshotData.SnapshotReason.appScheduled

**Framework**: SwiftUI  
**Kind**: case  
**Role**: Case

The app scheduled this snapshot.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
case appScheduled
```

## See Also

### Getting the snapshot reasons
- [SnapshotData.SnapshotReason.appBackgrounded](./appbackgrounded.md)
  The app transitioned from the foreground to the background.
- [SnapshotData.SnapshotReason.complicationUpdate](./complicationupdate.md)
  The app updated the complication timeline.
- [SnapshotData.SnapshotReason.prelaunch](./prelaunch.md)
  The system needs a snapshot for the dock, but the app has not been launched yet.
- [SnapshotData.SnapshotReason.returnToDefaultState](./returntodefaultstate.md)
  It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/snapshotdata/snapshotreason/appscheduled)*