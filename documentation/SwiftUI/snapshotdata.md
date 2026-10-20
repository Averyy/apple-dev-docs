# SnapshotData

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The associated data of a snapshot background task.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
struct SnapshotData
```

## Topics

### Getting the data
- [let identifier: String?](./snapshotdata/identifier.md)
  The identifier associated with this snapshot request.
- [let reason: SnapshotData.SnapshotReason](./snapshotdata/reason.md)
  The reason for a background snapshot task.
- [SnapshotData.SnapshotReason](./snapshotdata/snapshotreason.md)
  The reason for a background snapshot task.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Handling background tasks
- [func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) -> some Scene](./scene/backgroundtask%28_,action%29.md)
  Runs the specified action when the system provides a background task.
- [struct BackgroundTask](./backgroundtask.md)
  The kinds of background tasks that your app or extension can handle.
- [struct SnapshotResponse](./snapshotresponse.md)
  Your application’s response to a snapshot background task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/snapshotdata)*