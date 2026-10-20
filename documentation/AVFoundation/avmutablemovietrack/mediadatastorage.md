# mediaDataStorage

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A storage container for the media data to be added to a track.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var mediaDataStorage: AVMediaDataStorage? { get set }
```

```objc
@property (nonatomic, copy, nullable) AVMediaDataStorage * mediaDataStorage;
```

## See Also

### Configuring track information
- [var isModified: Bool](./ismodified.md)
  A Boolean value that indicates whether a track is in a modified state.
- [var alternateGroupID: Int](./alternategroupid.md)
  A number that identifies the track as a member of a particular alternate group.
- [var sampleReferenceBaseURL: URL?](./samplereferencebaseurl.md)
  The base URL for sample references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/mediadatastorage)*