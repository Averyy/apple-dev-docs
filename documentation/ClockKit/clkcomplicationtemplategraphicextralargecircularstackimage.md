# CLKComplicationTemplateGraphicExtraLargeCircularStackImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying an extra-large, full-color circular image and text.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicExtraLargeCircularStackImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicExtraLarge`](clkcomplicationfamily/graphicextralarge.md) family. [`Figure 1`](clkcomplicationtemplategraphicextralargecircularstackimage#3667231.md) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the image and text providers.](https://docs-assets.developer.apple.com/published/3bd6fc9881949e92ecde9bfa743bdc55/media-3667231%402x.png)

The table below lists the dimensions of the image you use in this template. Use @2x images for display on Apple Watch so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 160 pixels | 80 pixels |
| 41 mm | 170 pixels | 84 pixels |
| 44 mm | 174 pixels | 88 pixels |
| 45 mm | 190 pixels | 96 pixels |

This template supports full-color images.

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Supporting Multiple Watch Sizes`.

## Topics

### Creating the Template
- [init(line1ImageProvider: CLKFullColorImageProvider, line2TextProvider: CLKTextProvider)](clkcomplicationtemplategraphicextralargecircularstackimage/init(line1imageprovider:line2textprovider:).md)
  Creates a template with an image and a small amount of text.
### Setting the Complication Data
- [var line1ImageProvider: CLKFullColorImageProvider](clkcomplicationtemplategraphicextralargecircularstackimage/line1imageprovider.md)
  The image to display.
- [var line2TextProvider: CLKTextProvider](clkcomplicationtemplategraphicextralargecircularstackimage/line2textprovider.md)
  The text to display below the image.

## Relationships

### Inherits From
- [CLKComplicationTemplateGraphicExtraLargeCircular](clkcomplicationtemplategraphicextralargecircular.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CLKComplicationTemplateGraphicExtraLargeCircularImage](clkcomplicationtemplategraphicextralargecircularimage.md)
  A template for displaying an extra-large, full-color circular image.
- [class CLKComplicationTemplateGraphicExtraLargeCircularView](clkcomplicationtemplategraphicextralargecircularview.md)
  A template for displaying a circular SwiftUI view.
- [class CLKComplicationTemplateGraphicExtraLargeCircularStackViewText](clkcomplicationtemplategraphicextralargecircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.
- [class CLKComplicationTemplateGraphicExtraLargeCircularStackText](clkcomplicationtemplategraphicextralargecircularstacktext.md)
  A template for displaying two rows of text in an extra-large, circular complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularstackimage)*