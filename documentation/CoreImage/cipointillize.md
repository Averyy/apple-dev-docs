# CIPointillize

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a pointillize filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIPointillize : CIFilterProtocol
```

## Topics

### Instance Properties
- [var center: CGPoint](cipointillize/center.md)
  The x and y position to use as the center of the effect.
- [var inputImage: CIImage?](cipointillize/inputimage.md)
  The image to use as an input image.
- [var radius: Float](cipointillize/radius.md)
  The radius of the circles in the resulting pattern.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func pointillize() -> any CIFilter & CIPointillize](cifilter-swift.class/pointillize.md)
  Applies a pointillize effect to an image.
- [protocol CIBlendWithMask](ciblendwithmask.md)
  The properties you use to configure a blend with mask filter.
- [protocol CIBloom](cibloom.md)
  The properties you use to configure a bloom filter.
- [protocol CICannyEdgeDetector](cicannyedgedetector.md)
- [protocol CIComicEffect](cicomiceffect.md)
  The properties you use to configure a comic effect filter.
- [protocol CICoreMLModel](cicoremlmodel.md)
  The properties you use to configure a Core ML model filter.
- [protocol CICrystallize](cicrystallize.md)
  The properties you use to configure a crystalize filter.
- [protocol CIDepthOfField](cidepthoffield.md)
  The properties you use to configure a depth-of-field filter.
- [protocol CIEdgeWork](ciedgework.md)
  The properties you use to configure an edge-work filter.
- [protocol CIEdges](ciedges.md)
  The properties you use to configure an edges filter.
- [protocol CIGaborGradients](cigaborgradients.md)
  The properties you use to configure a Gabor gradients filter.
- [protocol CIGloom](cigloom.md)
  The properties you use to configure a gloom filter.
- [protocol CIHeightFieldFromMask](ciheightfieldfrommask.md)
  The properties you use to configure a height-field-from-mask filter.
- [protocol CIHexagonalPixellate](cihexagonalpixellate.md)
  The properties you use to configure a hexagonal pixellate filter.
- [protocol CIHighlightShadowAdjust](cihighlightshadowadjust.md)
  The properties you use to configure a highlight-shadow adjust filter.
- [protocol CILineOverlay](cilineoverlay.md)
  The properties you use to configure a line overlay filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipointillize)*