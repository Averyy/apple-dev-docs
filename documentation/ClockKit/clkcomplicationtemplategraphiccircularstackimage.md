# CLKComplicationTemplateGraphicCircularStackImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying a full-color circular image and text.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicCircularStackImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCircular`](clkcomplicationfamily/graphiccircular.md) family.

![Diagram showing the layout of a circular template containing an image and text.](https://docs-assets.developer.apple.com/published/cf5c80f0ab30f6f4cf3dda1898fd58e1/media-3262157%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as @2x images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 56 pixels | 28 pixels |
| 41 mm | 59 pixels | 30 pixels |
| 44 mm | 62 pixels | 32 pixels |
| 45 mm | 67 pixels | 33 pixels |

This template supports full-color images.

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Supporting Multiple Watch Sizes`.

## Topics

### Creating the Template
- [init(line1ImageProvider: CLKFullColorImageProvider, line2TextProvider: CLKTextProvider)](clkcomplicationtemplategraphiccircularstackimage/init(line1imageprovider:line2textprovider:).md)
  Creates a template that has an image and a small amount of text.
### Setting the Complicaiton Data
- [var line1ImageProvider: CLKFullColorImageProvider](clkcomplicationtemplategraphiccircularstackimage/line1imageprovider.md)
  The image to display.
- [var line2TextProvider: CLKTextProvider](clkcomplicationtemplategraphiccircularstackimage/line2textprovider.md)
  The text to display below the image.

## Relationships

### Inherits From
- [CLKComplicationTemplateGraphicCircular](clkcomplicationtemplategraphiccircular.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CLKComplicationTemplateGraphicCircularImage](clkcomplicationtemplategraphiccircularimage.md)
  A template for displaying a full-color circular image.
- [class CLKComplicationTemplateGraphicCircularView](clkcomplicationtemplategraphiccircularview.md)
  A template for displaying a circular view.
- [class CLKComplicationTemplateGraphicCircularStackViewText](clkcomplicationtemplategraphiccircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.
- [class CLKComplicationTemplateGraphicCircularStackText](clkcomplicationtemplategraphiccircularstacktext.md)
  A template for displaying two rows of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularstackimage)*