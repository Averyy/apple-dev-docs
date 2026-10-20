# MPSImageTransformProvider

**Framework**: Metal Performance Shaders  
**Kind**: protocol  
**Role**: Protocol

A general interface for objects that provide image resampling.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
protocol MPSImageTransformProvider : NSSecureCoding, NSObjectProtocol
```

```objc
@protocol MPSImageTransformProvider <NSSecureCoding, NSObject>
```

## Topics

### Instance Methods
- [func transform(forSourceImage: MPSImage, handle: (any MPSHandle)?) -> MPSScaleTransform](./mpsimagetransformprovider/transform%28forsourceimage,handle%29.md)

## Relationships

### Inherits From
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Resampling Nodes
- [class MPSNNBilinearScaleNode](./mpsnnbilinearscalenode.md)
  A representation of a bilinear resampling filter.
- [class MPSNNLanczosScaleNode](./mpsnnlanczosscalenode.md)
  A representation of a Lanczos resampling filter.
- [class MPSNNScaleNode](./mpsnnscalenode.md)
  Abstract node representing an image resampling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetransformprovider)*