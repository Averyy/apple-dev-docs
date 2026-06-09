# init(position:extents:)

**Framework**: RealityKit  
**Kind**: init

Creates a volume with the given center position and extents.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(position: SIMD3<Float> = .zero, extents: SIMD3<Float>)
```

## Parameters

- `position`: The center position of the volume in portal-local space. Defaults to `.zero`.
- `extents`: The size of the volume (width, height, depth) in portal-local space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/volume/init(position:extents:))*