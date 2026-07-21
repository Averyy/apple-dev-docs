# defaultLayer

**Framework**: RealityKit  
**Kind**: property

The default layer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var defaultLayer: RenderLayer { get }
```

#### Discussion

Entities without a [`RenderLayerComponent`](renderlayercomponent.md) belong to this layer. Lights illuminate only this layer unless their `layers` set is changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/renderlayer/defaultlayer)*