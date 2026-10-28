# CLKComplicationTemplateGraphicExtraLargeCircularStackText

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying two rows of text in an extra-large, circular complication.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateGraphicExtraLargeCircularStackText
```

```objc
@interface CLKComplicationTemplateGraphicExtraLargeCircularStackText : CLKComplicationTemplateGraphicExtraLargeCircular
```

## Overview

This template belongs to the [`CLKComplicationFamily.graphicExtraLarge`](./clkcomplicationfamily/graphicextralarge.md) family. [Figure 1](./clkcomplicationtemplategraphicextralargecircularstacktext.md#3667233) shows the layout of the complication and where it appears on the clock face.

![A diagram showing the layout of the complication that calls out the content produced by the text providers.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3667233@2x.png)

## Topics

### Creating the Template
- [init(line1TextProvider: CLKTextProvider, line2TextProvider: CLKTextProvider)](./clkcomplicationtemplategraphicextralargecircularstacktext/init%28line1textprovider,line2textprovider%29.md)
  Creates a new template with two rows of text.
- [+ templateWithLine1TextProvider:line2TextProvider:](./clkcomplicationtemplategraphicextralargecircularstacktext/templatewithline1textprovider_line2textprovider_.md)
  Returns a new template with two rows of text.
### Setting the Complication Data
- [var line1TextProvider: CLKTextProvider](./clkcomplicationtemplategraphicextralargecircularstacktext/line1textprovider.md)
  The text to display on the top row.
- [var line2TextProvider: CLKTextProvider](./clkcomplicationtemplategraphicextralargecircularstacktext/line2textprovider.md)
  The text to display on the bottom row.

## Relationships

### Inherits From
- [CLKComplicationTemplateGraphicExtraLargeCircular](./clkcomplicationtemplategraphicextralargecircular.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Text and images
- [class CLKComplicationTemplateGraphicExtraLargeCircularImage](./clkcomplicationtemplategraphicextralargecircularimage.md)
  A template for displaying an extra-large, full-color circular image.
- [class CLKComplicationTemplateGraphicExtraLargeCircularView](./clkcomplicationtemplategraphicextralargecircularview.md)
  A template for displaying a circular SwiftUI view.
- [class CLKComplicationTemplateGraphicExtraLargeCircularStackImage](./clkcomplicationtemplategraphicextralargecircularstackimage.md)
  A template for displaying an extra-large, full-color circular image and text.
- [class CLKComplicationTemplateGraphicExtraLargeCircularStackViewText](./clkcomplicationtemplategraphicextralargecircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularstacktext)*