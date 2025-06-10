# sampleOrdering

**Framework**: RealityKit  
**Kind**: property

The order of the image samples.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var sampleOrdering: PhotogrammetrySession.Configuration.SampleOrdering
```

#### Discussion

By default, RealityKit assumes that image samples aren’t in any particular order. If you’re providing the images in order, with adjacent images next to each other, specifying [`PhotogrammetrySession.Configuration.SampleOrdering.sequential`](photogrammetrysession/configuration-swift.struct/sampleordering-swift.enum/sequential.md) for this value may result in better performance.

This setting has no impact on the quality of the produced object.

## See Also

- [PhotogrammetrySession.Configuration.SampleOrdering](photogrammetrysession/configuration-swift.struct/sampleordering-swift.enum.md)
  The ordering of samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/configuration-swift.struct/sampleordering-swift.property)*