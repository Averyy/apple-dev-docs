# init(scale:rotation:translation:)

**Framework**: Spatial  
**Kind**: init

Returns a new scale, rotate, translate transform.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(scale: Size3DFloat = Size3DFloat(width: 1.0, height: 1, depth: 1), rotation: Rotation3DFloat = .identity, translation: Vector3DFloat = .zero)
```

## Parameters

- `scale`: The scale.
- `rotation`: The rotation.
- `translation`: The translation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3dfloat/init(scale:rotation:translation:))*