# devices

**Framework**: Now Playing  
**Kind**: property  
**Required**: Yes

The devices currently playing as part of this session.

**Availability**:
- iOS 27.0+ (Beta)
- iOS App Extension 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
var devices: [MediaDevice] { get }
```

## Mentions

- [Publishing remote media sessions](publishing-remote-media-sessions.md)

#### Discussion

Return an empty array when no devices are actively playing. The framework uses this list to surface per-device volume controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/remotemediasessionrepresentable/devices)*