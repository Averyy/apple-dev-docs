# PhotogrammetrySession.Configuration.FeatureSensitivity

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

The sensitivity to sample landmarks.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
enum FeatureSensitivity
```

## Topics

### Specifying feature sensitivity
- [PhotogrammetrySession.Configuration.FeatureSensitivity.normal](./featuresensitivity-swift.enum/normal.md)
  The session uses the default algorithm to detect landmarks.
- [PhotogrammetrySession.Configuration.FeatureSensitivity.high](./featuresensitivity-swift.enum/high.md)
  The session uses a slower, more sensitive algorithm to detect landmarks.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Configuring feature sensitivity
- [var featureSensitivity: PhotogrammetrySession.Configuration.FeatureSensitivity](./featuresensitivity-swift.property.md)
  The precision of landmark detection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/configuration-swift.struct/featuresensitivity-swift.enum)*