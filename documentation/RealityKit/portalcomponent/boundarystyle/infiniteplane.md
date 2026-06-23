# infinitePlane()

**Framework**: RealityKit  
**Kind**: method

Portal with infinite half-space clipping and crossing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func infinitePlane() -> PortalComponent.BoundaryStyle
```

#### Discussion

Content inside the portal world is visible through the flat plane mesh and clipped by an infinite plane boundary.

Corresponds to `ClippingMode.plane(_:)` and `CrossingMode.plane(_:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/boundarystyle/infiniteplane())*