# AnnotationOverflowResolution.Strategy

**Framework**: Swift Charts  
**Kind**: struct

Strategies for annotation overflow resolution.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct Strategy
```

## Topics

### Type Properties
- [static let automatic: AnnotationOverflowResolution.Strategy](annotationoverflowresolution/strategy/automatic.md)
  Automatically chooses a overflow resolution.
- [static let disabled: AnnotationOverflowResolution.Strategy](annotationoverflowresolution/strategy/disabled.md)
  Places the annotation “as-is”.
- [static let fit: AnnotationOverflowResolution.Strategy](annotationoverflowresolution/strategy/fit.md)
  Fits the annotation automatically, adjusting its position to ensure it doesn’t overflow.
- [static let padScale: AnnotationOverflowResolution.Strategy](annotationoverflowresolution/strategy/padscale.md)
  Pads the scale of the chart to make space for the annotation.
### Type Methods
- [static func fit(to: AnnotationOverflowResolution.Boundary) -> AnnotationOverflowResolution.Strategy](annotationoverflowresolution/strategy/fit(to:).md)
  Fits the annotation to the given boundary, adjusting its position to ensure it doesn’t overflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/annotationoverflowresolution/strategy)*