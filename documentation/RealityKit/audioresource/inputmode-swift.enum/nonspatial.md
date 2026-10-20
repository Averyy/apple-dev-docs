# AudioResource.InputMode.nonSpatial

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

the input channels are mixed to whatever the output format is without any spatialization

**Availability**:
- iOS 13.0+ - Deprecated in 16.3
- iPadOS 13.0+ - Deprecated in 16.3
- Mac Catalyst 13.0+ - Deprecated in 16.3
- macOS 10.15+ - Deprecated in 13.3
- tvOS 26.0+ - Deprecated in 26.0

> **Deprecated**: Use the ChannelAudioComponent, AmbientAudioComponent, or SpatialAudioComponent instead.

## Declaration

```swift
case nonSpatial
```

## See Also

### Input modes
- [AudioResource.InputMode.spatial](./spatial.md)
  a spatialized with all degrees of freedom. This treats a resource as a mono stream so mixes all its channels to mono
- [AudioResource.InputMode.ambient](./ambient.md)
  spatialized but ignores listener translation and only follows listener head rotation


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioresource/inputmode-swift.enum/nonspatial)*