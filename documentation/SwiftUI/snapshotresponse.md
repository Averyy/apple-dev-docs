# SnapshotResponse

**Framework**: SwiftUI  
**Kind**: struct

Your appplication’s response to a snapshot background task.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
struct SnapshotResponse
```

## Topics

### Creating a response
- [init(restoredDefaultState: Bool, estimatedSnapshotExpiration: Date?, identifier: String?)](snapshotresponse/init(restoreddefaultstate:estimatedsnapshotexpiration:identifier:).md)
  Creates a snapshot response.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) -> some Scene](scene/backgroundtask(_:action:).md)
  Runs the specified action when the system provides a background task.
- [struct BackgroundTask](backgroundtask.md)
  The kinds of background tasks that your app or extension can handle.
- [struct SnapshotData](snapshotdata.md)
  The associated data of a snapshot background task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/snapshotresponse)*