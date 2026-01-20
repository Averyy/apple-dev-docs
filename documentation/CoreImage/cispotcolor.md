# CISpotColor

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a spot color filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CISpotColor : CIFilterProtocol
```

## Topics

### Instance Properties
- [var centerColor1: CIColor](cispotcolor/centercolor1.md)
  The center value of the first color range to replace.
- [var centerColor2: CIColor](cispotcolor/centercolor2.md)
  The center value of the second color range to replace.
- [var centerColor3: CIColor](cispotcolor/centercolor3.md)
  The center value of the third color range to replace.
- [var closeness1: Float](cispotcolor/closeness1.md)
  A value that indicates how closely the first color must match before it’s replaced.
- [var closeness2: Float](cispotcolor/closeness2.md)
  A value that indicates how closely the second color must match before it’s replaced.
- [var closeness3: Float](cispotcolor/closeness3.md)
  A value that indicates how closely the third color must match before it’s replaced.
- [var contrast1: Float](cispotcolor/contrast1.md)
  The contrast of the first replacement color.
- [var contrast2: Float](cispotcolor/contrast2.md)
  The contrast of the second replacement color.
- [var contrast3: Float](cispotcolor/contrast3.md)
  The contrast of the third replacement color.
- [var inputImage: CIImage?](cispotcolor/inputimage.md)
  The image to use as an input image.
- [var replacementColor1: CIColor](cispotcolor/replacementcolor1.md)
  A replacement color for the first color range.
- [var replacementColor2: CIColor](cispotcolor/replacementcolor2.md)
  A replacement color for the second color range.
- [var replacementColor3: CIColor](cispotcolor/replacementcolor3.md)
  A replacement color for the third color range.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func spotColor() -> any CIFilter & CISpotColor](cifilter-swift.class/spotcolor.md)
  Replaces colors of an image with specifed colors.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cispotcolor)*