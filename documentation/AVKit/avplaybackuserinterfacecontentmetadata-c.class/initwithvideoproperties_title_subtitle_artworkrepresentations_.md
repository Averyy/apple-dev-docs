# initWithVideoProperties:title:subtitle:artworkRepresentations:

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Initializes a new metadata object with the specified properties.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
- (instancetype) initWithVideoProperties:(AVPlaybackUserInterfaceContentVideoProperties *) videoProperties title:(NSString *) title subtitle:(NSString *) subtitle artworkRepresentations:(NSArray<AVPlaybackUserInterfaceContentArtwork *> *) artworkRepresentations;
```

## Parameters

- `videoProperties`: Properties describing the video content, or `nil` for content without video.
- `title`: Primary title or name of the media content.
- `subtitle`: Secondary descriptive text such as artist name or episode description.
- `artworkRepresentations`: Array of available artwork representations in various formats and sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacecontentmetadata-c.class/initwithvideoproperties:title:subtitle:artworkrepresentations:)*