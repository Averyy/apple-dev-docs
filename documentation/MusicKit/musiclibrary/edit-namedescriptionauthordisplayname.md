# edit(_:name:description:authorDisplayName:)

**Framework**: MusicKit  
**Kind**: method

Edits a playlist that your app has created.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@discardableResult
func edit(_ playlist: Playlist, name: String? = nil, description: String? = nil, authorDisplayName: String? = nil) async throws -> Playlist
```

#### Return Value

The edited playlist.

#### Discussion

This function will throw an error if your app attempts to edit a playlist that another app created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrary/edit(_:name:description:authordisplayname:))*