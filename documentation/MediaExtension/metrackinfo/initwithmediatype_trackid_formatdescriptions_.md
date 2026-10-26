# initWithMediaType:trackID:formatDescriptions:

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method

Creates a new track info object with the media type, track ID, and format descriptions that you specify.

**Availability**:
- macOS 14.0+

## Declaration

```objc
- (instancetype) initWithMediaType:(CMMediaType) mediaType trackID:(CMPersistentTrackID) trackID formatDescriptions:(NSArray *) formatDescriptions;
```

## Parameters

- `mediaType`: The media type of the track.
- `trackID`: An integer that identifies the track within the media asset.
- `formatDescriptions`: An array of format descriptions for the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/metrackinfo/initwithmediatype:trackid:formatdescriptions:)*