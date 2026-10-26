# init(circularTemplate:textProvider:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a circular template with text that wraps around the bezel.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) to create complications. For more information, see Migrating to WidgetKit.

## Declaration

```swift
init(circularTemplate: CLKComplicationTemplateGraphicCircular, textProvider: CLKTextProvider?)
```

```objc
- (instancetype) initWithCircularTemplate:(CLKComplicationTemplateGraphicCircular *) circularTemplate textProvider:(CLKTextProvider *) textProvider;
```

## Parameters

- `circularTemplate`: A graphic circular template.
- `textProvider`: The text provider for the text element. The template ignores this text provider’s tint color, and always displays the text with a system color.

## See Also

### Creating the Template
- [init(circularTemplate: CLKComplicationTemplateGraphicCircular)](./init%28circulartemplate%29.md)
  Creates a circular template.
- [+ templateWithCircularTemplate:](./templatewithcirculartemplate_.md)
  Returns a circular template.
- [+ templateWithCircularTemplate:textProvider:](./templatewithcirculartemplate_textprovider_.md)
  Returns a circular template with text that wraps around the bezel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicbezelcirculartext/init(circulartemplate:textprovider:))*