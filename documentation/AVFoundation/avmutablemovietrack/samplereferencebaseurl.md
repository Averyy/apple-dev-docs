# sampleReferenceBaseURL

**Framework**: AVFoundation  
**Kind**: property

The base URL for sample references.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var sampleReferenceBaseURL: URL? { get set }
```

#### Discussion

When this property is an absolute URL, the sample locations written to the file when appending sample references to this track are relative to this URL. The URL must point to a location contained by any common parent directory of the locations that will be referenced. For example, setting the this property to `file:///Users/johnappleseed/Movies/` and appending sample buffers that refer to `file:///Users/johnappleseed/Movies/data/movie1.mov` will cause the sample reference `data/movie1.mov` to be written to the movie file.

If this property can’t be resolved as an absolute URL or if it points to a location that isn’t contained by any common parent directory of the locations referenced, the unmodified location is written. The default value is `nil`, indicating that the unmodified location will be written.

## See Also

- [var isModified: Bool](avmutablemovietrack/ismodified.md)
  A Boolean value that indicates whether a track is in a modified state.
- [var alternateGroupID: Int](avmutablemovietrack/alternategroupid.md)
  A number that identifies the track as a member of a particular alternate group.
- [var mediaDataStorage: AVMediaDataStorage?](avmutablemovietrack/mediadatastorage.md)
  A storage container for the media data to be added to a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/samplereferencebaseurl)*