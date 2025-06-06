# isSpatialVideoCaptureEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether a movie file output captures spatial videos.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var isSpatialVideoCaptureEnabled: Bool { get set }
```

#### Discussion

Spatial capture lets you record your favorite moments in 3D for playback on Apple Vision Pro. This feature isn’t supported on all devices, so you can only enable this property when [`isSpatialVideoCaptureSupported`](avcapturemoviefileoutput/isspatialvideocapturesupported.md) is [`true`](https://developer.apple.com/documentation/swift/true).

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isSpatialVideoCaptureSupported: Bool](avcapturemoviefileoutput/isspatialvideocapturesupported.md)
  A Boolean value that indicates whether a movie file output supports capturing spatial videos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/isspatialvideocaptureenabled)*