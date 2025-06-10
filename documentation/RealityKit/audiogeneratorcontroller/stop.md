# stop()

**Framework**: RealityKit  
**Kind**: method

Stops playback of the render handler.

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
func stop()
```

#### Discussion

Callbacks to the render handler stop after calling [`stop()`](audiogeneratorcontroller/stop().md). There may be a short delay between when you call `stop` and when the callbacks actually stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiogeneratorcontroller/stop())*