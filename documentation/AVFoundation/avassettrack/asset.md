# asset

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The asset object that contains this track.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
weak var asset: AVAsset? { get }
```

```objc
@property (nonatomic, weak, readonly) AVAsset * asset;
```

## See Also

### Identifying an asset track
- [var trackID: CMPersistentTrackID](./trackid.md)
  The persistent unique identifier for this track.
- [var mediaType: AVMediaType](./mediatype.md)
  The type of media that a track presents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/asset)*