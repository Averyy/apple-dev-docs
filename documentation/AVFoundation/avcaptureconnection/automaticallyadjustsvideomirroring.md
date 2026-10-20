# automaticallyAdjustsVideoMirroring

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you can enable mirroring based on a session’s configuration.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var automaticallyAdjustsVideoMirroring: Bool { get set }
```

```objc
@property (nonatomic) BOOL automaticallyAdjustsVideoMirroring;
```

#### Discussion

For some session configurations, the connection mirrors the video data by default. When the value of this property is [`true`](../../Swift/true.md), the value of [`isVideoMirrored`](./isvideomirrored.md) may change, depending on the configuration of the session. For example, the value may change after switching to a different capture device input.

The default value is [`true`](../../Swift/true.md).

## See Also

### Mirroring a video
- [var isVideoMirroringSupported: Bool](./isvideomirroringsupported.md)
  A Boolean value that indicates whether the connection supports video mirroring.
- [var isVideoMirrored: Bool](./isvideomirrored.md)
  A Boolean value that indicates whether the connection horizontally flips the video flowing through it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/automaticallyadjustsvideomirroring)*