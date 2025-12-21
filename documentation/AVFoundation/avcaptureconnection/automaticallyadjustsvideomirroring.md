# automaticallyAdjustsVideoMirroring

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

For some session configurations, the connection mirrors the video data by default. When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the value of [`isVideoMirrored`](avcaptureconnection/isvideomirrored.md) may change, depending on the configuration of the session. For example, the value may change after switching to a different capture device input.

The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var isVideoMirroringSupported: Bool](avcaptureconnection/isvideomirroringsupported.md)
  A Boolean value that indicates whether the connection supports video mirroring.
- [var isVideoMirrored: Bool](avcaptureconnection/isvideomirrored.md)
  A Boolean value that indicates whether the connection horizontally flips the video flowing through it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/automaticallyadjustsvideomirroring)*