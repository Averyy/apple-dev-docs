# CLKComplicationTemplateGraphicCornerGaugeText

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying text and a gauge in the clock face’s corner.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateGraphicCornerGaugeText
```

```objc
@interface CLKComplicationTemplateGraphicCornerGaugeText : CLKComplicationTemplate
```

## Overview

This template belongs to the [`CLKComplicationFamily.graphicCorner`](./clkcomplicationfamily/graphiccorner.md) family.  shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of the outer text and a gauge with leading and trailing text.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3030691@2x.png)

The system always displays the outer text as white. The gauge’s text can be multicolored.

## Topics

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, outerTextProvider: CLKTextProvider)](./clkcomplicationtemplategraphiccornergaugetext/init%28gaugeprovider,outertextprovider%29.md)
  Creates a template that has a gauge and an outer text element.
- [init(gaugeProvider: CLKGaugeProvider, leadingTextProvider: CLKTextProvider?, trailingTextProvider: CLKTextProvider?, outerTextProvider: CLKTextProvider)](./clkcomplicationtemplategraphiccornergaugetext/init%28gaugeprovider,leadingtextprovider,trailingtextprovider,outertextprovider%29.md)
  Creates a template that has a gauge with leading and trailing text, and an outer text element.
- [+ templateWithGaugeProvider:outerTextProvider:](./clkcomplicationtemplategraphiccornergaugetext/templatewithgaugeprovider_outertextprovider_.md)
  Returns a template that has a gauge and an outer text element.
- [+ templateWithGaugeProvider:leadingTextProvider:trailingTextProvider:outerTextProvider:](./clkcomplicationtemplategraphiccornergaugetext/templatewithgaugeprovider_leadingtextprovider_trailingtextprovider_outertextprovider_.md)
  Returns a template that has a gauge with leading and trailing text, and an outer text element.
### Setting the Complication Data
- [var outerTextProvider: CLKTextProvider](./clkcomplicationtemplategraphiccornergaugetext/outertextprovider.md)
  The outer text to display in the complication.
- [var gaugeProvider: CLKGaugeProvider](./clkcomplicationtemplategraphiccornergaugetext/gaugeprovider.md)
  The gauge to display in the complication.
- [var leadingTextProvider: CLKTextProvider?](./clkcomplicationtemplategraphiccornergaugetext/leadingtextprovider.md)
  The text to display on the leading edge of the gague.
- [var trailingTextProvider: CLKTextProvider?](./clkcomplicationtemplategraphiccornergaugetext/trailingtextprovider.md)
  The text to display on the trailing edge of the gauge.

## Relationships

### Inherits From
- [CLKComplicationTemplate](./clkcomplicationtemplate.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Gauges
- [class CLKComplicationTemplateGraphicCornerGaugeImage](./clkcomplicationtemplategraphiccornergaugeimage.md)
  A template for displaying an image and a gauge in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerGaugeView](./clkcomplicationtemplategraphiccornergaugeview.md)
  A template for displaying a SwiftUI view and a gauge in the clock face’s corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugetext)*