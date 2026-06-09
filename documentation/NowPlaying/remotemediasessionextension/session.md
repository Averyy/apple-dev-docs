# session(_:)

**Framework**: Now Playing  
**Kind**: method  
**Required**: Yes

Creates a session configured with the specified attributes.

**Availability**:
- iOS 27.0+ (Beta)
- iOS App Extension 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
func session(_ attributes: Self.Attributes) async throws -> Self.Session
```

## Mentions

- [Publishing remote media sessions](publishing-remote-media-sessions.md)

#### Return Value

A configured remote session.

#### Discussion

> **Note**: An error if a session can’t be created.

## Parameters

- `attributes`: The attributes that configure the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasessionextension/session(_:))*