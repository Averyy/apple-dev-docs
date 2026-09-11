# defaultLayer

**Framework**: RealityKit  
**Kind**: property

The default layer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static var defaultLayer: RenderLayer { get }
```

#### Discussion

Entities without a [`RenderLayerComponent`](renderlayercomponent.md) belong to this layer. Lights illuminate only this layer unless their `layers` set is changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/renderlayer/defaultlayer)*