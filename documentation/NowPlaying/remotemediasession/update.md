# update(_:)

**Framework**: Now Playing  
**Kind**: method

Updates the session with new attributes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
func update(_ attributes: Attributes) async throws
```

#### Discussion

When session attributes change, call this method to send the updated attributes to your app extension through the [`update(_:)`](remotemediasessionrepresentable/update(_:).md) method.

> **Note**: [`RemoteMediaSessionError.invalidAttributes`](remotemediasessionerror/invalidattributes.md) if `attributes.id` doesn’t match this session’s id. [`RemoteMediaSessionError.internalFailure`](remotemediasessionerror/internalfailure.md) if the system couldn’t deliver the update.

## Parameters

- `attributes`: The updated attributes for this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasession/update(_:))*