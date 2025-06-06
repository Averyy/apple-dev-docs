# CLKComplicationTemplateGraphicRectangularFullImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying a full-color image that fills the complication.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicRectangularFullImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicRectangular`](clkcomplicationfamily/graphicrectangular.md) family.

![A diagram of a graphic rectangular full complication. The diagram shows an image of the moon filling the complication.](https://docs-assets.developer.apple.com/published/b75dd3557d6469f77b521a44992cf30f/media-3905732%402x.png)

The table below lists the dimensions of the image you use in this template. Use images with a [`scale`](https://developer.apple.com/documentation/UIKit/UIImage/scale) of `2.0` for display on Apple Watch so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 324 pixels | 138 pixels |
| 41 mm | 343 pixels | 146 pixels |
| 44 mm | 368 pixels | 156 pixels |
| 45 mm | 386 pixels | 164 pixels |

This template supports full-color images.

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Manage Assets`.

## Topics

### Creating the Template
- [init(imageProvider: CLKFullColorImageProvider)](clkcomplicationtemplategraphicrectangularfullimage/init(imageprovider:).md)
  Creates a template with a large rectangular image.
### Setting the Complication Data
- [var imageProvider: CLKFullColorImageProvider](clkcomplicationtemplategraphicrectangularfullimage/imageprovider.md)
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

- [class CLKComplicationTemplateGraphicRectangularLargeImage](clkcomplicationtemplategraphicrectangularlargeimage.md)
  A template for displaying a large rectangle containing header text and an image.
- [class CLKComplicationTemplateGraphicRectangularLargeView](clkcomplicationtemplategraphicrectangularlargeview.md)
  A template for displaying a large rectangle containing header text and a SwiftUI view.
- [class CLKComplicationTemplateGraphicRectangularFullView](clkcomplicationtemplategraphicrectangularfullview.md)
  A template for displaying a SwiftUI view that fills the entire template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangularfullimage)*