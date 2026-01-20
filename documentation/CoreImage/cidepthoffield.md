# CIDepthOfField

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a depth-of-field filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIDepthOfField : CIFilterProtocol
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cidepthoffield/inputimage.md)
  The image to use as an input image.
- [var point0: CGPoint](cidepthoffield/point0.md)
  The first point in the focused region of the output image.
- [var point1: CGPoint](cidepthoffield/point1.md)
  The second point in the focused region of the output image.
- [var radius: Float](cidepthoffield/radius.md)
  The distance from the center of the effect.
- [var saturation: Float](cidepthoffield/saturation.md)
  The amount to adjust the saturation by.
- [var unsharpMaskIntensity: Float](cidepthoffield/unsharpmaskintensity.md)
  The intensity of the unsharp mask effect applied to the in-focus area.
- [var unsharpMaskRadius: Float](cidepthoffield/unsharpmaskradius.md)
  The radius of the unsharp mask effect applied to the in-focus area.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func depthOfField() -> any CIFilter & CIDepthOfField](cifilter-swift.class/depthoffield.md)
  Simulates a depth of field effect.
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
- [protocol CIMix](cimix.md)
  The properties you use to configure a mix filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidepthoffield)*