# shadow

**Framework**: RealityKit  
**Kind**: property

The shadow for the spotlight.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency var shadow: SpotLightComponent.Shadow? { get set }
```

#### Discussion

Set this property to `nil` to remove shadows for the light. Set it to an instance of [`SpotLightComponent.Shadow`](spotlightcomponent/shadow.md) to create shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasspotlight/shadow)*