# SHMediaItem

**Framework**: ShazamKit  
**Kind**: class

An object that represents the metadata for a reference signature.

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
class SHMediaItem
```

#### Overview

This class uses subscripting for the data elements of a custom media item that an existing property doesn’t already represent.

Add a readable custom property by extending [`SHMediaItemProperty`](shmediaitemproperty.md) with a key for that property, and by extending this class with a property that uses the key. The following code shows the extensions for an episode number:

```swift
// Add an episode number to the list of properties.
extension SHMediaItemProperty {
    static let episode = SHMediaItemProperty("Episode")
}

// Add a property for returning the episode number using a subscript.
extension SHMediaItem {
    var episode: Int? {
        return self[.episode] as? Int
    }
}
```

Add your custom property when you create the media item as the following code shows:

```swift
// Create a new media item and set the title, subtitle, and episode properties.
let mediaItem = SHMediaItem(properties: [.episode: 42,
                                         .title: "Question",
                                         .subtitle: "The Answer"])
```

> **Note**:  The class of the object that represents a custom object must be one of: `Dictionary`, `Array`, `URL`, `Number`, `String`, `Date`, or `Data`.

 The class of the object that represents a custom object must be one of: `Dictionary`, `Array`, `URL`, `Number`, `String`, `Date`, or `Data`.

## Topics

### Creating a new media item object
- [convenience init(properties: [SHMediaItemProperty : Any])](shmediaitem/init(properties:).md)
  Creates a media item object with a dictionary of properties and their associated values.
### Working with media item properties
- [subscript(SHMediaItemProperty) -> Any](shmediaitem/subscript(_:).md)
  Accesses the property for the specified key for reading.
- [struct SHMediaItemProperty](shmediaitemproperty.md)
  Constants for the media item property names.
- [var timeRanges: [Range<TimeInterval>]](shmediaitem/timeranges-8msna.md)
  An array of ranges that indicate the offsets within the reference signature that this media item describes.
- [var frequencySkewRanges: [Range<Float>]](shmediaitem/frequencyskewranges-1j7d3.md)
  An array of ranges that indicate the frequency skews in the reference signature that this media item describes.
### Reading general media item properties
- [var title: String?](shmediaitem/title.md)
  A title for the media item.
- [var subtitle: String?](shmediaitem/subtitle.md)
  A subtitle for the media item.
- [var artist: String?](shmediaitem/artist.md)
  The name of the artist for the media item, such as the performer of a song.
- [var artworkURL: URL?](shmediaitem/artworkurl.md)
  The URL for artwork for the media item, such as an album cover.
- [var videoURL: URL?](shmediaitem/videourl.md)
  The URL for a video for the media item, such as a music video.
- [var genres: [String]](shmediaitem/genres.md)
  An array of genre names for the media item.
- [var explicitContent: Bool](shmediaitem/explicitcontent.md)
  A Boolean value that indicates whether the media item contains explicit content.
- [var creationDate: Date?](shmediaitem/creationdate.md)
  The date the media item was created.
- [var isrc: String?](shmediaitem/isrc.md)
  The International Standard Recording Code (ISRC) for the media item.
- [var id: UUID](shmediaitem/id.md)
  A unique identifier for this media item.
### Reading Apple Music properties
- [var songs: [Song]](shmediaitem/songs.md)
  An array of MusicKit song objects that represent the song.
- [var appleMusicURL: URL?](shmediaitem/applemusicurl.md)
  A link to the Apple Music page that contains the full information for the song.
- [var appleMusicID: String?](shmediaitem/applemusicid.md)
  The Apple Music ID for the song.
### Working with Shazam music catalog media items
- [var webURL: URL?](shmediaitem/weburl.md)
  A link to the Shazam Music catalog page that contains the full information for the song.
- [var shazamID: String?](shmediaitem/shazamid.md)
  The Shazam ID for the song.
- [class func fetch(shazamID: String, completionHandler: (SHMediaItem?, (any Error)?) -> Void)](shmediaitem/fetch(shazamid:completionhandler:).md)
  Requests the media item for the song with the specified Shazam ID.
### Default Implementations
- [Identifiable Implementations](shmediaitem/identifiable-implementations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [SHMatchedMediaItem](shmatchedmediaitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class SHSession](shsession.md)
  An object that matches a specific audio recording when a segment of that recording is part of captured sound in the Shazam catalog or your custom catalog.
- [class SHManagedSession](shmanagedsession.md)
  An object that records and matches a recording with captured sound in the Shazam catalog or your custom catalog.
- [protocol SHSessionDelegate](shsessiondelegate.md)
  Methods that the session calls with the result of a match request.
- [class SHMatch](shmatch.md)
  An object that represents the catalog media items that match a query.
- [class SHMatchedMediaItem](shmatchedmediaitem.md)
  An object that represents the metadata for a matched reference signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmediaitem)*