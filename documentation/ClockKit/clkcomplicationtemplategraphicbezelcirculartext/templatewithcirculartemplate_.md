# templateWithCircularTemplate:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a circular template.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) to create complications. For more information, see Migrating to WidgetKit.

## Declaration

```objc
+ (instancetype) templateWithCircularTemplate:(CLKComplicationTemplateGraphicCircular *) circularTemplate;
```

## Parameters

- `circularTemplate`: A graphic circular template.

## See Also

### Creating the Template
- [init(circularTemplate: CLKComplicationTemplateGraphicCircular)](./init%28circulartemplate%29.md)
  Creates a circular template.
- [init(circularTemplate: CLKComplicationTemplateGraphicCircular, textProvider: CLKTextProvider?)](./init%28circulartemplate,textprovider%29.md)
  Creates a circular template with text that wraps around the bezel.
- [+ templateWithCircularTemplate:textProvider:](./templatewithcirculartemplate_textprovider_.md)
  Returns a circular template with text that wraps around the bezel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicbezelcirculartext/templatewithcirculartemplate:)*