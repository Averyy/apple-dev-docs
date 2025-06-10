# currentImageSize

**Framework**: RealityKit  
**Kind**: property

What is the width and height of currently playing video (for stereo, the width and height of each eye)? This is optional because the video may not currently be playing, or the size is otherwise not available.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency var currentImageSize: CGSize? { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videoplaybackcontroller/currentimagesize-85cha)*