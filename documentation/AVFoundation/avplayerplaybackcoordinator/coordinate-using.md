# coordinate(using:)

**Framework**: AVFoundation  
**Kind**: method

Connects the playback coordinator to the coordination medium

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func coordinate(using coordinationMedium: AVPlaybackCoordinationMedium?) throws
```

#### Discussion

This connects the playback coordinator to a coordination medium to enable sending and receiving messages from other connected playback coordinators. If the coordination medium is non-NULL, this will connect the playback coordinator to the specified coordination medium. If the coordination medium is set to NULL, this will disconnect the playback coordinator from the playback coordination medium. The player will no longer be coordinated with the other players connected to the coordination medium. The playback coordinator can either only coordinate with local players through an AVPlaybackCoordinationMedium or coordinate with a remote group session through the `coordinateWithSession` API. If the client attempts to connect to an AVPlaybackCoordinationMedium while already connected to a group session, this method will populate the outError parameter If the playback coordinator successfully connects to the coordination medium or disconnects from a coordination medium, the `outError` parameter will be nil. If the playback coordinator fails to connect to the specified coordination medium, the `outError` parameter will describe what went wrong.

## Parameters

- `coordinationMedium`: The coordination medium the playback coordinator connects to. If NULL, the playback coordinator disconnects from any existing coordination medium.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerplaybackcoordinator/coordinate(using:))*