# CLKComplicationTemplateGraphicRectangularLargeImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying a large rectangle containing header text and an image.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicRectangularLargeImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicRectangular`](clkcomplicationfamily/graphicrectangular.md) family. [`Figure 1`](clkcomplicationtemplategraphicrectangularlargeimage#3034025.md) shows the layout of the image and where the template might appear on the clock face.

![Diagram of a watch face showing the layout of a rectangular large image template.](https://docs-assets.developer.apple.com/published/d281acd014900ada4ca9b77eae032ae3/media-3034025%402x.png)

The table below lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as @2x images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 300 pixels | 94 pixels |
| 41 mm | 318 pixels | 100 pixels |
| 44 mm | 342 pixels | 108 pixels |
| 45 mm | 357 pixels | 112 pixels |

This template supports full-color images. The image provider automatically masks the image to a rounded rectangle with a 8-pixel corner radius.

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Supporting Multiple Watch Sizes`.

## Topics

### Creating the Template
- [init(textProvider: CLKTextProvider, imageProvider: CLKFullColorImageProvider)](clkcomplicationtemplategraphicrectangularlargeimage/init(textprovider:imageprovider:).md)
  Creates a new template with a text provider and an image provider.
### Setting the Complication Data
- [var textProvider: CLKTextProvider](clkcomplicationtemplategraphicrectangularlargeimage/textprovider.md)
  The header text to display in the complication.
- [var imageProvider: CLKFullColorImageProvider](clkcomplicationtemplategraphicrectangularlargeimage/imageprovider.md)
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

- [class CLKComplicationTemplateGraphicRectangularLargeView](clkcomplicationtemplategraphicrectangularlargeview.md)
  A template for displaying a large rectangle containing header text and a SwiftUI view.
- [class CLKComplicationTemplateGraphicRectangularFullImage](clkcomplicationtemplategraphicrectangularfullimage.md)
  A template for displaying a full-color image that fills the complication.
- [class CLKComplicationTemplateGraphicRectangularFullView](clkcomplicationtemplategraphicrectangularfullview.md)
  A template for displaying a SwiftUI view that fills the entire template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangularlargeimage)*