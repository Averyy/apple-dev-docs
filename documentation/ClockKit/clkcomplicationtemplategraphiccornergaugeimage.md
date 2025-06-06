# CLKComplicationTemplateGraphicCornerGaugeImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying an image and a gauge in the clock face’s corner.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicCornerGaugeImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCorner`](clkcomplicationfamily/graphiccorner.md) family. [`Figure 1`](clkcomplicationtemplategraphiccornergaugeimage#3030693.md) shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of an image and a gauge with trailing text.](https://docs-assets.developer.apple.com/published/79ef3eb287a4f7db6b49e5bbc33514cb/media-3030693%402x.png)

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
- [init(gaugeProvider: CLKGaugeProvider, imageProvider: CLKFullColorImageProvider)](clkcomplicationtemplategraphiccornergaugeimage/init(gaugeprovider:imageprovider:).md)
  Creates a new template that has a gauge and an image.
- [init(gaugeProvider: CLKGaugeProvider, leadingTextProvider: CLKTextProvider?, trailingTextProvider: CLKTextProvider?, imageProvider: CLKFullColorImageProvider)](clkcomplicationtemplategraphiccornergaugeimage/init(gaugeprovider:leadingtextprovider:trailingtextprovider:imageprovider:).md)
  Creates a new template that has a gauge with leading and trailing text and an image.
### Setting the Complication Data
- [var imageProvider: CLKFullColorImageProvider](clkcomplicationtemplategraphiccornergaugeimage/imageprovider.md)
  The image to display.
- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphiccornergaugeimage/gaugeprovider.md)
  The gauge to display in the complication.
- [var leadingTextProvider: CLKTextProvider?](clkcomplicationtemplategraphiccornergaugeimage/leadingtextprovider.md)
  The text to display on the leading edge of the gauge.
- [var trailingTextProvider: CLKTextProvider?](clkcomplicationtemplategraphiccornergaugeimage/trailingtextprovider.md)
  The text to display on the trailing edge of the gauge.

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

- [class CLKComplicationTemplateGraphicCornerGaugeView](clkcomplicationtemplategraphiccornergaugeview.md)
  A template for displaying a SwiftUI view and a gauge in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerGaugeText](clkcomplicationtemplategraphiccornergaugetext.md)
  A template for displaying text and a gauge in the clock face’s corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugeimage)*