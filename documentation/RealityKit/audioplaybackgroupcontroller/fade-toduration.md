# fade(to:duration:)

**Framework**: RealityKit  
**Kind**: method

Transitions the gain to the given value over a time interval using a linear curve for all audio resources in the group.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func fade(to newValue: Audio.Decibel, duration: TimeInterval)
```

#### Discussion

The target gain must be zero or negative, where zero is nominal loudness and negative infinity is silent. If the gain is positive, it will be reset to zero.

## Parameters

- `newValue`: The target decibel level.
- `duration`: How long in seconds the fade should last.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackgroupcontroller/fade(to:duration:))*