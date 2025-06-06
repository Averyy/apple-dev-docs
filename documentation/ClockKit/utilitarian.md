# Utilitarian

**Framework**: ClockKit

Use the utilitarian templates to display content on a variety of watch faces, including the Utility, Chronograph, Simple, and character watch faces.

#### Overview

The small utilitarian templates occupy a short rectangular area in the corner of the watch face. The content can include a glyph or icon, or it can include a circular graph. The large utilitarian templates occupy a long rectangular area at the bottom of the watch face. That area can display a longer string of text and a small image.

![Examples of the Utilitarian small templates. From left to right they are small flat, square, ring text (open), ring text (closed), ring image (open), and ring image (closed).](https://docs-assets.developer.apple.com/published/d77d585b52dfb95b1a9a09e0dd1f7f94/media-2878969%402x.png)

![Utilitarian large template](https://docs-assets.developer.apple.com/published/105169f1a7e163c638d73150eda416eb/media-2878970%402x.png)

## Topics

### Utilitarian small
- [class CLKComplicationTemplateUtilitarianSmallFlat](clkcomplicationtemplateutilitariansmallflat.md)
  A template for displaying an image and text in a single line.
- [class CLKComplicationTemplateUtilitarianSmallRingImage](clkcomplicationtemplateutilitariansmallringimage.md)
  A template for displaying an image encircled by a configurable progress ring
- [class CLKComplicationTemplateUtilitarianSmallRingText](clkcomplicationtemplateutilitariansmallringtext.md)
  A template for displaying text encircled by a configurable progress ring.
- [class CLKComplicationTemplateUtilitarianSmallSquare](clkcomplicationtemplateutilitariansmallsquare.md)
  A template for displaying a single square image.
### Utilitarian large
- [class CLKComplicationTemplateUtilitarianLargeFlat](clkcomplicationtemplateutilitarianlargeflat.md)
  A template for displaying an image and string in a single long line.

## See Also

- [SwiftUI templates](swiftui-templates.md)
  Design complication templates using SwiftUI views.
- [enum ComplicationRenderingMode](complicationrenderingmode.md)
  The complication’s appearance, as specified by the watch face.
- [Data providers](data-providers.md)
  Feed data to a complication template.
- [Circular small](circular-small.md)
  Display small, circular content in the corners of the Color watch face.
- [Extra large](extra-large.md)
  Display content on the X-Large watch face.
- [Modular small](modular-small.md)
  Display content in the smaller spaces of the Modular watch face.
- [Modular large](modular-large.md)
  Display multiple rows of content in the large, central complication on the Modular watch face.
- [Graphic](graphic.md)
  Display visually rich content on watch faces.
- [class CLKComplicationTemplate](clkcomplicationtemplate.md)
  An abstract class that defines the base behavior for all templates.
- [enum CLKComplicationFamily](clkcomplicationfamily.md)
  Constants indicating the template groups.
- [CLKComplicationSupportedFamilies](../BundleResources/Information-Property-List/CLKComplicationSupportedFamilies.md)
  The complication families for which the app can provide data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/utilitarian)*