# sessions()

**Framework**: Now Playing  
**Kind**: method

Returns all registered remote sessions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
static func sessions() async throws -> [RemoteMediaSession<Attributes>]
```

#### Return Value

An array of all remote sessions currently registered with the system.

#### Discussion

> **Note**: [`RemoteMediaSessionError.internalFailure`](remotemediasessionerror/internalfailure.md) if the system couldn’t enumerate registered sessions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasession/sessions())*