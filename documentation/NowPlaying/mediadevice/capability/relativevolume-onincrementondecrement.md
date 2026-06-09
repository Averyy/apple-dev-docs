# relativeVolume(onIncrement:onDecrement:)

**Framework**: Now Playing  
**Kind**: method

Returns a capability that lets the device increase or decrease its volume incrementally.

**Availability**:
- iOS 27.0+ (Beta)
- iOS App Extension 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
static func relativeVolume(onIncrement: @escaping @Sendable () async throws -> Void, onDecrement: @escaping @Sendable () async throws -> Void) -> MediaDevice.Capability
```

## Mentions

- [Publishing remote media sessions](publishing-remote-media-sessions.md)

#### Discussion

Use this when the device supports stepwise volume changes but doesn’t expose an absolute level.

## Parameters

- `onIncrement`: An async closure the system calls to step the volume up by one increment.
- `onDecrement`: An async closure the system calls to step the volume down by one increment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediadevice/capability/relativevolume(onincrement:ondecrement:))*