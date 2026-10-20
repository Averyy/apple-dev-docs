# CLKComplicationTemplateModularLargeStandardBody

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A template for displaying a header row and two lines of text.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKComplicationTemplateModularLargeStandardBody
```

```objc
@interface CLKComplicationTemplateModularLargeStandardBody : CLKComplicationTemplate
```

#### Overview

This template belongs to the [`CLKComplicationFamily.modularLarge`](./clkcomplicationfamily/modularlarge.md) family.

![A diagram showing the layout of the modular large standard body complication. The diagram shows the header row, two lines of text, and an optional header image.](https://developer.apple.com/tutorials/images/com.apple.clockkit/media-2933747@2x.png)

The following table lists the dimensions of the image you use in this template. All dimensions are in pixels. All images must be specified as `@2x` images for display on Apple Watch, so the point-based dimensions are half the listed size. The width of the image must be between the specified minimum and maximum (inclusive).

| Apple Watch Size | Width | Height |
| --- | --- | --- |
| 38 mm | 22 pixels minimum ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) 64 pixels maximum | 22 pixels |
| 40 mm | 24 pixels minimum ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) 74 pixels maximum | 24 pixels |
| 41 mm | 25 pixels minimum ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) 78 pixels maximum | 25 pixels |
| 42 mm | 24 pixels minimum ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) 74 pixels maximum | 24 pixels |
| 44 mm | 28 pixels minimum ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) 84 pixels maximum | 28 pixels |
| 45 mm | 29 pixels minimum ![](https://developer.apple.com/tutorials/images/com.apple.clockkit/spacer.png) 88 pixels maximum | 29 pixels |

Instead of providing multiple images with different resolutions, you can provide a single, scaleable PDF asset. For more information, see `Manage Assets`.

## Topics

### Creating the Template
- [init(headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider)](./clkcomplicationtemplatemodularlargestandardbody/init%28headertextprovider,body1textprovider%29.md)
  Creates a new template that has a row of header text and a row of body text.
- [init(headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, body2TextProvider: CLKTextProvider?)](./clkcomplicationtemplatemodularlargestandardbody/init%28headertextprovider,body1textprovider,body2textprovider%29.md)
  Creates a new template that has a row of header text and two rows of body text.
- [init(headerImageProvider: CLKImageProvider?, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider)](./clkcomplicationtemplatemodularlargestandardbody/init%28headerimageprovider,headertextprovider,body1textprovider%29.md)
  Creates a new template that has a header row with an image and text, and a row of body text.
- [init(headerImageProvider: CLKImageProvider?, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, body2TextProvider: CLKTextProvider?)](./clkcomplicationtemplatemodularlargestandardbody/init%28headerimageprovider,headertextprovider,body1textprovider,body2textprovider%29.md)
  Creates a new template that has a header row with an image and text, and two rows of body text.
### Setting the Complication Data
- [var headerImageProvider: CLKImageProvider?](./clkcomplicationtemplatemodularlargestandardbody/headerimageprovider.md)
  An optional image to display in the header.
- [var headerTextProvider: CLKTextProvider](./clkcomplicationtemplatemodularlargestandardbody/headertextprovider.md)
  The text to display in the header line.
- [var body1TextProvider: CLKTextProvider](./clkcomplicationtemplatemodularlargestandardbody/body1textprovider.md)
  The top line of body text.
- [var body2TextProvider: CLKTextProvider?](./clkcomplicationtemplatemodularlargestandardbody/body2textprovider.md)
  An optional second line of body text.

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

### Body templates
- [class CLKComplicationTemplateModularLargeTallBody](./clkcomplicationtemplatemodularlargetallbody.md)
  A template for displaying a header row and row of tall body text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularlargestandardbody)*