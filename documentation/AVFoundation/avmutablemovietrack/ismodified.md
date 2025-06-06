# isModified

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether a track is in a modified state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var isModified: Bool { get set }
```

#### Discussion

This property is `YES` when the `AVMutableMovieTrack` object has been modified since it was created, was last written, or had its modified state cleared.

## See Also

- [var alternateGroupID: Int](avmutablemovietrack/alternategroupid.md)
  A number that identifies the track as a member of a particular alternate group.
- [var mediaDataStorage: AVMediaDataStorage?](avmutablemovietrack/mediadatastorage.md)
  A storage container for the media data to be added to a track.
- [var sampleReferenceBaseURL: URL?](avmutablemovietrack/samplereferencebaseurl.md)
  The base URL for sample references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/ismodified)*