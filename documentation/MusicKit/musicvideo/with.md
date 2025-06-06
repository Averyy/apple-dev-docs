# with(_:)

**Framework**: MusicKit  
**Kind**: method

Loads a new instance of the music item that includes the specified properties.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func with(_ properties: [PartialMusicAsyncProperty<Self>]) async throws -> Self
```

#### Discussion

This asynchronous method fetches a more complete representation of the receiver from Apple Music API over the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicvideo/with(_:))*