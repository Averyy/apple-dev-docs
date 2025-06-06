# CLKComplicationTemplateGraphicCircularImage

**Framework**: ClockKit  
**Kind**: class

A template for displaying a full-color circular image.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicCircularImage
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCircular`](clkcomplicationfamily/graphiccircular.md) family. [`Figure 1`](clkcomplicationtemplategraphiccircularimage#3030695.md) shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of a circular image.](https://docs-assets.developer.apple.com/published/a4348cf8f05d3e98ca2fb2663a39e6d4/media-3030695%402x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as @2x images for display on Apple Watch, so the point-based dimensions are half the listed size.

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 40 mm | 84 pixels | 84 pixels |
| 41 mm | 89 pixels | 89 pixels |
| 44 mm | 94 pixels | 94 pixels |
| 45 mm | 100 pixels | 100 pixels |

This template supports full-color images. The image provider automatically masks the image to a circle.

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Supporting Multiple Watch Sizes`.

## Topics

### Creating the Template
- [init(imageProvider: CLKFullColorImageProvider)](clkcomplicationtemplategraphiccircularimage/init(imageprovider:).md)
  Creates a template that has a circular image.
### Setting the Complication Data
- [var imageProvider: CLKFullColorImageProvider](clkcomplicationtemplategraphiccircularimage/imageprovider.md)
  The image to display.

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

- [class CLKComplicationTemplateGraphicCircularView](clkcomplicationtemplategraphiccircularview.md)
  A template for displaying a circular view.
- [class CLKComplicationTemplateGraphicCircularStackImage](clkcomplicationtemplategraphiccircularstackimage.md)
  A template for displaying a full-color circular image and text.
- [class CLKComplicationTemplateGraphicCircularStackViewText](clkcomplicationtemplategraphiccircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.
- [class CLKComplicationTemplateGraphicCircularStackText](clkcomplicationtemplategraphiccircularstacktext.md)
  A template for displaying two rows of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularimage)*