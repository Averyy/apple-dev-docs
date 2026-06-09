# init(_:)

**Framework**: Now Playing  
**Kind**: init

Creates a new local Now Playing session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
init(_ representable: Representable)
```

#### Discussion

The session automatically observes the representable and syncs metadata, commands, and playback state to the system.

## Parameters

- `representable`: The session representable that supplies content metadata, playback state, and commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediasession/init(_:))*