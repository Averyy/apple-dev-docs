# hash(into:)

**Framework**: RealityKit  
**Kind**: method

Hashes the essential components of the controller by feeding them into the given hash function.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher`: The hash function to use when combining the components of the controller.

## See Also

- [static func == (AnimationPlaybackController, AnimationPlaybackController) -> Bool](animationplaybackcontroller/==(_:_:).md)
  Indicates whether two animation playback controllers are equal.
- [static func != (Self, Self) -> Bool](animationplaybackcontroller/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [var hashValue: Int](animationplaybackcontroller/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/hash(into:))*