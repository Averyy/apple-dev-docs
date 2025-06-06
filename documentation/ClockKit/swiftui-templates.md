# SwiftUI templates

**Framework**: ClockKit

Design complication templates using SwiftUI views.

#### Overview

ClockKit provides SwiftUI versions of the other graphic templates. These templates use a [`View`](https://developer.apple.com/documentation/SwiftUI/View) instance to draw some or all of the complication’s content. However, the following templates are particularly useful when drawing the complication with SwiftUI:

- [`CLKComplicationTemplateGraphicCircularView`](clkcomplicationtemplategraphiccircularview.md)
- [`CLKComplicationTemplateGraphicRectangularFullView`](clkcomplicationtemplategraphicrectangularfullview.md)
- [`CLKComplicationTemplateGraphicExtraLargeCircularView`](clkcomplicationtemplategraphicextralargecircularview.md)

These templates use a single SwiftUI view to fill the entire complication, providing a blank canvas that you can use to draw the entire complication.

## Topics

### Corner templates
- [class CLKComplicationTemplateGraphicCornerCircularView](clkcomplicationtemplategraphiccornercircularview.md)
  A template for displaying a SwiftUI view in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerGaugeView](clkcomplicationtemplategraphiccornergaugeview.md)
  A template for displaying a SwiftUI view and a gauge in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerTextView](clkcomplicationtemplategraphiccornertextview.md)
  A template for displaying a SwiftUI view and text in the clock face’s corner.
### Circular templates
- [class CLKComplicationTemplateGraphicCircularView](clkcomplicationtemplategraphiccircularview.md)
  A template for displaying a circular view.
- [class CLKComplicationTemplateGraphicCircularOpenGaugeView](clkcomplicationtemplategraphiccircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicCircularClosedGaugeView](clkcomplicationtemplategraphiccircularclosedgaugeview.md)
  A template for displaying a SwiftUI view inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicCircularStackViewText](clkcomplicationtemplategraphiccircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.
### Rectangular templates
- [class CLKComplicationTemplateGraphicRectangularStandardBodyView](clkcomplicationtemplategraphicrectangularstandardbodyview.md)
  A template for displaying a SwiftUI label and up to three rows of text.
- [class CLKComplicationTemplateGraphicRectangularTextGaugeView](clkcomplicationtemplategraphicrectangulartextgaugeview.md)
  A template for displaying a header row with a SwiftUI view and text, a second row of text, and a gauge.
- [class CLKComplicationTemplateGraphicRectangularLargeView](clkcomplicationtemplategraphicrectangularlargeview.md)
  A template for displaying a large rectangle containing header text and a SwiftUI view.
- [class CLKComplicationTemplateGraphicRectangularFullView](clkcomplicationtemplategraphicrectangularfullview.md)
  A template for displaying a SwiftUI view that fills the entire template.
### Extra large templates
- [class CLKComplicationTemplateGraphicExtraLargeCircularView](clkcomplicationtemplategraphicextralargecircularview.md)
  A template for displaying a circular SwiftUI view.
- [class CLKComplicationTemplateGraphicExtraLargeCircularOpenGaugeView](clkcomplicationtemplategraphicextralargecircularopengaugeview.md)
  A template for displaying a SwiftUI view, an open gauge, and text.
- [class CLKComplicationTemplateGraphicExtraLargeCircularClosedGaugeView](clkcomplicationtemplategraphicextralargecircularclosedgaugeview.md)
  A template for displaying an extra-large SwiftUI view inside a closed circular gauge.
- [class CLKComplicationTemplateGraphicExtraLargeCircularStackViewText](clkcomplicationtemplategraphicextralargecircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.

## See Also

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
- [Utilitarian](utilitarian.md)
  Use the utilitarian templates to display content on a variety of watch faces, including the Utility, Chronograph, Simple, and character watch faces.
- [Graphic](graphic.md)
  Display visually rich content on watch faces.
- [class CLKComplicationTemplate](clkcomplicationtemplate.md)
  An abstract class that defines the base behavior for all templates.
- [enum CLKComplicationFamily](clkcomplicationfamily.md)
  Constants indicating the template groups.
- [CLKComplicationSupportedFamilies](../BundleResources/Information-Property-List/CLKComplicationSupportedFamilies.md)
  The complication families for which the app can provide data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/swiftui-templates)*