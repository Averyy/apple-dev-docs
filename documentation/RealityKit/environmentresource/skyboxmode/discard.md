# discard

**Framework**: RealityKit  
**Kind**: property

Only keep a low-resolution proxy of the skybox, reducing memory usage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var discard: EnvironmentResource.SkyboxMode { get }
```

#### Discussion

> **Note**: The skybox is not needed for lighting with `VirtualEnvironmentProbeComponent` and `ImageBasedLightComponent`.

## See Also

- [static var preserve: EnvironmentResource.SkyboxMode](environmentresource/skyboxmode/preserve.md)
  Preserve and reference the original skybox cube texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/skyboxmode/discard)*