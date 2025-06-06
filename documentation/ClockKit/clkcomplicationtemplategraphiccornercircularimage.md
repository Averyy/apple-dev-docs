# CLKComplicationTemplateGraphicCornerCircularImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying an image in the clock face’s corner.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicCornerCircularImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCorner`](clkcomplicationfamily/graphiccorner.md) family. [`Figure 1`](clkcomplicationtemplategraphiccornercircularimage#3030689.md) shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of an image.](https://docs-assets.developer.apple.com/published/6885b0cd312aede6a90203a83a298402/media-3030689%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as @2x images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 64 pixels | 64 pixels |
| 41 mm | 68 pixels | 68 pixels |
| 44 mm | 72 pixels | 72 pixels |
| 45 mm | 76 pixels | 76 pixels |

This template supports full-color images. The image provider automatically masks the image to a circle.

Instead of providing multiple images with different resolutions, you can provide a single scaleable PDF asset. For more information, see `Supporting Multiple Watch Sizes`.

## Topics

### Creating the Template
- [init(imageProvider: CLKFullColorImageProvider)](clkcomplicationtemplategraphiccornercircularimage/init(imageprovider:).md)
  Creates a new template from the provided image.
### Setting the Complication Data
- [var imageProvider: CLKFullColorImageProvider](clkcomplicationtemplategraphiccornercircularimage/imageprovider.md)
  The image to display.

## Relationships

### Inherits From
- [CLKComplicationTemplate](clkcomplicationtemplate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CLKComplicationTemplateGraphicCornerCircularView](clkcomplicationtemplategraphiccornercircularview.md)
  A template for displaying a SwiftUI view in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerStackText](clkcomplicationtemplategraphiccornerstacktext.md)
  A template for displaying stacked text in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerTextImage](clkcomplicationtemplategraphiccornertextimage.md)
  A template for displaying an image and text in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerTextView](clkcomplicationtemplategraphiccornertextview.md)
  A template for displaying a SwiftUI view and text in the clock face’s corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornercircularimage)*