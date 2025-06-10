# hash(into:)

**Framework**: RealityKit  
**Kind**: method

Hashes the essential components of the controller by feeding them into the given hash function.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
nonisolated
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher`: The hash function to use when combining the components of the controller.

## See Also

- [static func == (AnimationPlaybackController, AnimationPlaybackController) -> Bool](animationplaybackcontroller/==(_:_:).md)
  Indicates whether two animation playback controllers are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/hash(into:))*