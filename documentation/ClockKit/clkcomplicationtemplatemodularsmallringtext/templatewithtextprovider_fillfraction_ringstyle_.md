# templateWithTextProvider:fillFraction:ringStyle:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a new template from the provided text, fill fraction, and ring style.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithTextProvider:(CLKTextProvider *) textProvider fillFraction:(float) fillFraction ringStyle:(CLKComplicationRingStyle) ringStyle;
```

## Parameters

- `textProvider`: A text provider for the text in the center of the template. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `fillFraction`: A value between `0.0` and `1.0` that indicates how much of the ring fills.
- `ringStyle`: The ring’s style. For a complete list of styles, see [`CLKComplicationRingStyle`](../clkcomplicationringstyle.md).

## See Also

### Creating the Template
- [init(textProvider: CLKTextProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)](./init%28textprovider,fillfraction,ringstyle%29.md)
  Creates a new template from the provided text, fill fraction, and ring style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallringtext/templatewithtextprovider:fillfraction:ringstyle:)*