# CLKComplicationTemplateGraphicCornerStackText

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying stacked text in the clock face’s corner.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateGraphicCornerStackText
```

```objc
@interface CLKComplicationTemplateGraphicCornerStackText : CLKComplicationTemplate
```

## Overview

This template belongs to the [`CLKComplicationFamily.graphicCorner`](./clkcomplicationfamily/graphiccorner.md) family.  shows the layout of the image and where the template might appear on the clock face.

![Diagram showing the layout of the outer and inner text.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3030692@2x.png)

The system always displays the outer text as white. The inner text can be multicolored.

## Topics

### Creating the Template
- [init(innerTextProvider: CLKTextProvider, outerTextProvider: CLKTextProvider)](./clkcomplicationtemplategraphiccornerstacktext/init%28innertextprovider,outertextprovider%29.md)
  Creates a template that has an inner line of text and an outer text element.
- [+ templateWithInnerTextProvider:outerTextProvider:](./clkcomplicationtemplategraphiccornerstacktext/templatewithinnertextprovider_outertextprovider_.md)
  Returns a template that has an inner line of text and an outer text element.
### Setting the Complication Data
- [var outerTextProvider: CLKTextProvider](./clkcomplicationtemplategraphiccornerstacktext/outertextprovider.md)
  The outer text to display in the complication.
- [var innerTextProvider: CLKTextProvider](./clkcomplicationtemplategraphiccornerstacktext/innertextprovider.md)
  The inner text to display in the complication.

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

### Text and image
- [class CLKComplicationTemplateGraphicCornerCircularImage](./clkcomplicationtemplategraphiccornercircularimage.md)
  A template for displaying an image in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerCircularView](./clkcomplicationtemplategraphiccornercircularview.md)
  A template for displaying a SwiftUI view in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerTextImage](./clkcomplicationtemplategraphiccornertextimage.md)
  A template for displaying an image and text in the clock face’s corner.
- [class CLKComplicationTemplateGraphicCornerTextView](./clkcomplicationtemplategraphiccornertextview.md)
  A template for displaying a SwiftUI view and text in the clock face’s corner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornerstacktext)*