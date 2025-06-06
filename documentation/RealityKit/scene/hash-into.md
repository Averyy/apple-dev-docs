# hash(into:)

**Framework**: RealityKit  
**Kind**: method

Hashes the essential components of the scene by feeding them into the given hash function.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
nonisolated
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher`: The hash function to use when combining the components of the   scene.

## See Also

- [static func == (Scene, Scene) -> Bool](scene/==(_:_:).md)
  Indicates whether two scenes are equal.
- [static func != (Self, Self) -> Bool](scene/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [var hashValue: Int](scene/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/hash(into:))*