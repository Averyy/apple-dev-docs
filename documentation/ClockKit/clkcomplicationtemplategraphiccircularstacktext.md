# CLKComplicationTemplateGraphicCircularStackText

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying two rows of text.

**Availability**:
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateGraphicCircularStackText
```

```objc
@interface CLKComplicationTemplateGraphicCircularStackText : CLKComplicationTemplateGraphicCircular
```

#### Overview

This template belongs to the [`CLKComplicationFamily.graphicCircular`](./clkcomplicationfamily/graphiccircular.md) family.

![Diagram showing the layout of a circular template containing two rows of text.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-3262158@2x.png)

## Topics

### Creating the Template
- [init(line1TextProvider: CLKTextProvider, line2TextProvider: CLKTextProvider)](./clkcomplicationtemplategraphiccircularstacktext/init%28line1textprovider,line2textprovider%29.md)
  Creates a new template that has two small rows of text.
### Setting the Complication Data
- [var line1TextProvider: CLKTextProvider](./clkcomplicationtemplategraphiccircularstacktext/line1textprovider.md)
  The text to display on the top row.
- [var line2TextProvider: CLKTextProvider](./clkcomplicationtemplategraphiccircularstacktext/line2textprovider.md)
  The text to display on the bottom row.

## Relationships

### Inherits From
- [CLKComplicationTemplateGraphicCircular](./clkcomplicationtemplategraphiccircular.md)
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
- [class CLKComplicationTemplateGraphicCircularImage](./clkcomplicationtemplategraphiccircularimage.md)
  A template for displaying a full-color circular image.
- [class CLKComplicationTemplateGraphicCircularView](./clkcomplicationtemplategraphiccircularview.md)
  A template for displaying a circular view.
- [class CLKComplicationTemplateGraphicCircularStackImage](./clkcomplicationtemplategraphiccircularstackimage.md)
  A template for displaying a full-color circular image and text.
- [class CLKComplicationTemplateGraphicCircularStackViewText](./clkcomplicationtemplategraphiccircularstackviewtext.md)
  A template for displaying a SwiftUI view and text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularstacktext)*