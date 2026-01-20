# MPSImageTransformProvider

**Framework**: Metal Performance Shaders  
**Kind**: protocol

A general interface for objects that provide image resampling.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol MPSImageTransformProvider : NSSecureCoding, NSObjectProtocol
```

## Topics

### Instance Methods
- [func transform(forSourceImage: MPSImage, handle: (any MPSHandle)?) -> MPSScaleTransform](mpsimagetransformprovider/transform(forsourceimage:handle:).md)

## Relationships

### Inherits From
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSNNBilinearScaleNode](mpsnnbilinearscalenode.md)
  A representation of a bilinear resampling filter.
- [class MPSNNLanczosScaleNode](mpsnnlanczosscalenode.md)
  A representation of a Lanczos resampling filter.
- [class MPSNNScaleNode](mpsnnscalenode.md)
  Abstract node representing an image resampling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetransformprovider)*