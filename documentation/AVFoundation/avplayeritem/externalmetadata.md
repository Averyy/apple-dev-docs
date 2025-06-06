# externalMetadata

**Framework**: AVFoundation  
**Kind**: property

An array of additional metadata for the player item to supplement or replace an asset’s embedded metadata.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var externalMetadata: [AVMetadataItem] { get set }
```

#### Discussion

[`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController) supports displaying the following metadata identifiers:

- [`commonKeyTitle`](avmetadatakey/commonkeytitle.md)
- [`iTunesMetadataTrackSubTitle`](avmetadataidentifier/itunesmetadatatracksubtitle.md)
- [`commonIdentifierArtwork`](avmetadataidentifier/commonidentifierartwork.md)
- [`commonKeyDescription`](avmetadatakey/commonkeydescription.md)
- [`iTunesMetadataKeyContentRating`](avmetadatakey/itunesmetadatakeycontentrating.md)
- [`quickTimeMetadataKeyGenre`](avmetadatakey/quicktimemetadatakeygenre.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/externalmetadata)*