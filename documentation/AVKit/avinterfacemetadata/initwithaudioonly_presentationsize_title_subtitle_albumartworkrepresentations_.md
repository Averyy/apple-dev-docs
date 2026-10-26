# initWithAudioOnly:presentationSize:title:subtitle:albumArtworkRepresentations:

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Initializes a new metadata object with the specified properties.

## Declaration

```objc
- (instancetype) initWithAudioOnly:(BOOL) audioOnly presentationSize:(CGSize) presentationSize title:(NSString *) title subtitle:(NSString *) subtitle albumArtworkRepresentations:(NSArray<AVInterfaceAlbumArtwork *> *) albumArtworkRepresentations;
```

## Parameters

- `audioOnly`: Whether the content is audio-only (no video component).
- `presentationSize`: The pixel dimensions for video presentation.
- `title`: Primary title or name of the media content.
- `subtitle`: Secondary descriptive text such as artist name or episode description.
- `albumArtworkRepresentations`: Array of available album artwork representations in various formats and sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemetadata/initwithaudioonly:presentationsize:title:subtitle:albumartworkrepresentations:)*