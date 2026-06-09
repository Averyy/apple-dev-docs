# bounds

**Framework**: RealityKit  
**Kind**: property

The bounds of this mesh instance, in model space, or `nil` to derive bounds from the mesh part.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var bounds: BoundingSphereBox? { get set }
```

#### Discussion

Assign a value to override the mesh part’s bounds — for example, when using instancing to place instances across a wider area than the base mesh part covers, or when a geometry modifier displaces vertices beyond the mesh part’s recorded bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshinstance/bounds)*