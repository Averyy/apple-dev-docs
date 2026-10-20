# isSpatialVideoCaptureEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, getter=isSpatialVideoCaptureEnabled) BOOL spatialVideoCaptureEnabled;
```

#### Discussion

Spatial capture lets you record your favorite moments in 3D for playback on Apple Vision Pro. This feature isn’t supported on all devices, so you can only enable this property when [`isSpatialVideoCaptureSupported`](./isspatialvideocapturesupported.md) is [`true`](../../Swift/true.md).

The default value is [`false`](../../Swift/false.md).

## See Also

### Enabling spatial capture
- [var isSpatialVideoCaptureSupported: Bool](./isspatialvideocapturesupported.md)
  A Boolean value that indicates whether a movie file output supports capturing spatial videos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/isspatialvideocaptureenabled)*