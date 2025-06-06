# completionHandler

**Framework**: RealityKit  
**Kind**: property

A closure that the playback controller executes when it reaches the end of the audio stream.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var completionHandler: (() -> Void)? { get set }
```

#### Discussion

The controller doesn’t call the closure if you manually stop the audio by calling the [`stop()`](audioplaybackcontroller/stop().md) or the [`pause()`](audioplaybackcontroller/pause().md) method.

> **Note**: You can only register one handler at a time. If you set a new handler, the controller discards the old one.

You can only register one handler at a time. If you set a new handler, the controller discards the old one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackcontroller/completionhandler)*