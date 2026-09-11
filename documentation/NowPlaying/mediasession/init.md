# init(_:)

**Framework**: Now Playing  
**Kind**: init

Creates a new local Now Playing session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

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