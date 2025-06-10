# play()

**Framework**: RealityKit  
**Kind**: method

Begins the audio stream from the generator render handler.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@MainActor
func play()
```

#### Discussion

When you play the controller, the render handler starts receiving callbacks. The controller ignores calls to [`play()`](audiogeneratorcontroller/play().md) when audio is already playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiogeneratorcontroller/play())*