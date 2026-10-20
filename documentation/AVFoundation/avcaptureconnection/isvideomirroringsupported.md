# isVideoMirroringSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the connection supports video mirroring.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var isVideoMirroringSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isVideoMirroringSupported) BOOL supportsVideoMirroring;
```

## See Also

### Mirroring a video
- [var isVideoMirrored: Bool](./isvideomirrored.md)
  A Boolean value that indicates whether the connection horizontally flips the video flowing through it.
- [var automaticallyAdjustsVideoMirroring: Bool](./automaticallyadjustsvideomirroring.md)
  A Boolean value that indicates whether you can enable mirroring based on a session’s configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideomirroringsupported)*