# CLKComplicationTemplateGraphicCornerTextImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying an image and text in the clock face’s corner.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicCornerTextImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCorner`](clkcomplicationfamily/graphiccorner.md) family. [`Figure 1`](clkcomplicationtemplategraphiccornertextimage#3030694.md) shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of text and an image.](https://docs-assets.developer.apple.com/published/d6c7bad1c0dca58a3c49960829362b49/media-3030694%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as @2x images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 40 pixels | 40 pixels |
| 41 mm | 42 pixels | 42 pixels |
| 44 mm | 44 pixels | 44 pixels |
| 45 mm | 48 pixels | 48 pixels |

This template supports full-color images. The image provider automatically masks the image to a circle.

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Supporting Multiple Watch Sizes`.

## Topics

### Creating the Template
- [init(textProvider: CLKTextProvider, imageProvider: CLKFullColorImageProvider)](clkcomplicationtemplategraphiccornertextimage/init(textprovider:imageprovider:).md)
  Creates a template with a line of text and an image.
### Setting the Complication Data
- [var imageProvider: CLKFullColorImageProvider](clkcomplicationtemplategraphiccornertextimage/imageprovider.md)
  The image to display.
- [var textProvider: CLKTextProvider](clkcomplicationtemplategraphiccornertextimage/textprovider.md)
  The text to display in the complication.

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

- [class CLKComplicationTemplateGraphicCornerCircularImage](clkcomplicationtemplategraphiccornercircularimage.md)
  A template for displaying an image in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerCircularView](clkcomplicationtemplategraphiccornercircularview.md)
  A template for displaying a SwiftUI view in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerStackText](clkcomplicationtemplategraphiccornerstacktext.md)
  A template for displaying stacked text in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerTextView](clkcomplicationtemplategraphiccornertextview.md)
  A template for displaying a SwiftUI view and text in the clock face’s corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornertextimage)*