# CLKComplicationTemplateGraphicCornerGaugeText

**Framework**: ClockKit  
**Kind**: class

A template for displaying text and a gauge in the clock face’s corner.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKComplicationTemplateGraphicCornerGaugeText
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCorner`](clkcomplicationfamily/graphiccorner.md) family.  shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of the outer text and a gauge with leading and trailing text.](https://docs-assets.developer.apple.com/published/eaf2f5c597a0944670d5a0d631487f84/media-3030691%402x.png)

The system always displays the outer text as white. The gauge’s text can be multicolored.

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, outerTextProvider: CLKTextProvider)](clkcomplicationtemplategraphiccornergaugetext/init(gaugeprovider:outertextprovider:).md)
  Creates a template that has a gauge and an outer text element.
- [init(gaugeProvider: CLKGaugeProvider, leadingTextProvider: CLKTextProvider?, trailingTextProvider: CLKTextProvider?, outerTextProvider: CLKTextProvider)](clkcomplicationtemplategraphiccornergaugetext/init(gaugeprovider:leadingtextprovider:trailingtextprovider:outertextprovider:).md)
  Creates a template that has a gauge with leading and trailing text, and an outer text element.
### Setting the Complication Data
- [var outerTextProvider: CLKTextProvider](clkcomplicationtemplategraphiccornergaugetext/outertextprovider.md)
  The outer text to display in the complication.
- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphiccornergaugetext/gaugeprovider.md)
  The gauge to display in the complication.
- [var leadingTextProvider: CLKTextProvider?](clkcomplicationtemplategraphiccornergaugetext/leadingtextprovider.md)
  The text to display on the leading edge of the gague.
- [var trailingTextProvider: CLKTextProvider?](clkcomplicationtemplategraphiccornergaugetext/trailingtextprovider.md)
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

- [class CLKComplicationTemplateGraphicCornerGaugeImage](clkcomplicationtemplategraphiccornergaugeimage.md)
  A template for displaying an image and a gauge in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerGaugeView](clkcomplicationtemplategraphiccornergaugeview.md)
  A template for displaying a SwiftUI view and a gauge in the clock face’s corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugetext)*