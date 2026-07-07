# start(endpoint:)

**Framework**: Spatial Preview  
**Kind**: method

Connects to the specified endpoint and prepares the session to send document updates.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
final nonisolated(nonsending) func start(endpoint: SpatialPreviewEndpoint) async throws
```

#### Discussion

Call this method once before sending document content via [`updateContents(data:)`](documentpreviewsession/updatecontents(data:).md) or [`updateContents(url:)`](documentpreviewsession/updatecontents(url:).md). The method establishes connection and transitions the session’s `state` to [`SpatialPreviewSessionState.connected`](spatialpreviewsessionstate/connected.md).

> **Note**: [`SpatialPreviewSessionError`](spatialpreviewsessionerror.md) if the connection cannot be established or the session has already been invalidated.

## Parameters

- `endpoint`: The destination endpoint representing the device to connect to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/documentpreviewsession/start(endpoint:))*