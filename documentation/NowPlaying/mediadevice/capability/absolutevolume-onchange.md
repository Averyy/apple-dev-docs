# absoluteVolume(_:onChange:)

**Framework**: Now Playing  
**Kind**: method

Returns a capability that lets the device be set to a specific volume level.

**Availability**:
- iOS 27.0+ (Beta)
- iOS App Extension 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
static func absoluteVolume(_ currentLevel: Float, onChange: @escaping @Sendable (Float) async throws -> Void) -> MediaDevice.Capability
```

## Mentions

- [Publishing remote media sessions](publishing-remote-media-sessions.md)

#### Discussion

Use this when the device supports setting an absolute volume level in the range `0.0` to `1.0`, where `0` represents silence and `1.0` represents the maximum volume level.

## Parameters

- `currentLevel`: The current volume level of the device, in the range `0.0` to `1.0`. The system uses this to display the device’s current volume in the interface.
- `onChange`: An async closure the system calls when the user requests a new volume level. The closure receives the requested new level in the range `0.0` to `1.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediadevice/capability/absolutevolume(_:onchange:))*