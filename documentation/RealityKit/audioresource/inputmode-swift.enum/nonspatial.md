# AudioResource.InputMode.nonSpatial

**Framework**: RealityKit  
**Kind**: case

the input channels are mixed to whatever the output format is without any spatialization

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+

## Declaration

```swift
case nonSpatial
```

## See Also

- [AudioResource.InputMode.spatial](audioresource/inputmode-swift.enum/spatial.md)
  a spatialized with all degrees of freedom. This treats a resource as a mono stream so mixes all its channels to mono
- [AudioResource.InputMode.ambient](audioresource/inputmode-swift.enum/ambient.md)
  spatialized but ignores listener translation and only follows listener head rotation


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioresource/inputmode-swift.enum/nonspatial)*