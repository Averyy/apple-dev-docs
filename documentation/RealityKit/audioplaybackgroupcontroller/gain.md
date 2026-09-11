# gain

**Framework**: RealityKit  
**Kind**: property

The individual gain in decibels for all audio resources in the group.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency var gain: Audio.Decibel { get set }
```

#### Discussion

The gain must be zero or negative, where zero is nominal loudness and negative infinity is silent. If the gain is positive, it will be reset to zero.

Use the [`fade(to:duration:)`](audioplaybackgroupcontroller/fade(to:duration:).md) method to change the gain gradually and create smooth transitions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackgroupcontroller/gain)*