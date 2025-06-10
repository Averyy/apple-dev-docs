# selectSubjects(_:)

**Framework**: DockKit  
**Kind**: method

Selects subjects to track with specific identifiers

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
final func selectSubjects(_ ids: [UUID]) async throws
```

#### Discussion

`TrackingStates` provide a list of subjects with their unique identifiers in the video frame. Use this method to select a subset of subjects to track by passing a list of unique identifiers. If you pass an empty list, the system defaults to system tracking (if enabled).

If you disable system tracking, this configuration change applies to any custom tracking for this dock accessory. If system tracking is enabled, the configuration applies to any camera stream that the app has open.

Call this method when implementing your own custom tracking behavior.

> **Note**: [`DockKitError.notConnected`](dockkiterror/notconnected.md) if device isn’t docked, or other errors if no subject is found at the position.

## Parameters

- `ids`: The unique identifiers of subjects in the video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/selectsubjects(_:))*