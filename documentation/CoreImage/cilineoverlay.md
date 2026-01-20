# CILineOverlay

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a line overlay filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CILineOverlay : CIFilterProtocol
```

## Topics

### Instance Properties
- [var nrNoiseLevel: Float](cilineoverlay/nrnoiselevel.md)
  The noise level of the image, used with camera data, that’s removed before tracing the edges of the image.
- [var nrSharpness: Float](cilineoverlay/nrsharpness.md)
  The amount of sharpening done when removing noise in the image before tracing the edges of the image.
- [var contrast: Float](cilineoverlay/contrast.md)
  The amount of antialiasing to use on the edges produced by this filter.
- [var edgeIntensity: Float](cilineoverlay/edgeintensity.md)
  The accentuation factor of the Sobel gradient information when tracing the edges of the image.
- [var inputImage: CIImage?](cilineoverlay/inputimage.md)
  The image to use as an input image.
- [var threshold: Float](cilineoverlay/threshold.md)
  A value that determines edge visibility.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func lineOverlay() -> any CIFilter & CILineOverlay](cifilter-swift.class/lineoverlay.md)
  Creates an image that resembles a sketch of the outlines of objects.
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
- [protocol CIMix](cimix.md)
  The properties you use to configure a mix filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilineoverlay)*