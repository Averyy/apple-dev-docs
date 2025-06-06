# init(patternImage:)

**Framework**: UIKit  
**Kind**: init

Creates a color object using the specified image object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(patternImage image: UIImage)
```

#### Return Value

The pattern color.

#### Discussion

You can use pattern colors to set the fill or stroke color just as you’d a solid color. During drawing, the image in the pattern color is tiled as necessary to cover the given area.

By default, the phase of the returned color is 0, which causes the top-left corner of the image to be aligned with the drawing origin. To change the phase, make the color the current color and then use the [`setPatternPhase(_:)`](https://developer.apple.com/documentation/CoreGraphics/CGContext/setPatternPhase(_:)) function to change the phase.

## Parameters

- `image`: The image to use when creating the pattern color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/init(patternimage:))*