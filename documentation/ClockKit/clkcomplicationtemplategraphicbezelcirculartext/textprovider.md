# textProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The text to display along the bezel.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) to create complications. For more information, see Migrating to WidgetKit.

## Declaration

```swift
@NSCopying
var textProvider: CLKTextProvider? { get set }
```

```objc
@property (nonatomic, copy, nullable) CLKTextProvider * textProvider;
```

#### Discussion

The complication ignores the text provider’s tint color. It always displays the bezel text as white.

## See Also

### Setting the Complication Data
- [var circularTemplate: CLKComplicationTemplateGraphicCircular](./circulartemplate.md)
  The circular template to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicbezelcirculartext/textprovider)*