# getPlaylist(with:creationMetadata:completionHandler:)

**Framework**: Media Player  
**Kind**: method

Retrieves an app maintained existing playlist or creates a new playlist when no playlist exists.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func getPlaylist(with uuid: UUID, creationMetadata: MPMediaPlaylistCreationMetadata?) async throws -> MPMediaPlaylist
```

#### Discussion

This function retrieves the playlist associated with the UUID. Create a static instance of the UUID using a previously generated UUID. Creating a new UUID using `init(uuidString:)` to retrieve a playlist doesn’t guarantee its retrieval.

When there’s no playlist associated with the UUID, the system creates a new playlist with the UUID and the creation metadata. The system ignores this metadata when the playlist already exists.

## Parameters

- `uuid`: The unique identifier for the playlist.
- `creationMetadata`: The metadata that the system uses to create a new playlist, which it ignores if a playlist already exists.
- `completionHandler`: A block that the system calls after it retrieves or creates the playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/getplaylist(with:creationmetadata:completionhandler:))*