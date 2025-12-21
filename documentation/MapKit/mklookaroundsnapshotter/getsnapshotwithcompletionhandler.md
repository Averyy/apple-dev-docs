# getSnapshotWithCompletionHandler(_:)

**Framework**: MapKit  
**Kind**: method

Requests a new snapshot and calls the completion handler you provide.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var snapshot: MKLookAroundSnapshotter.Snapshot { get async throws }
```

## Parameters

- `completionHandler`: A completion handler the framework calls to indicate the success or failure of the snapshot request.

## See Also

- [func cancel()](mklookaroundsnapshotter/cancel.md)
  Cancels an in-progress snapshot request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundsnapshotter/getsnapshotwithcompletionhandler(_:))*