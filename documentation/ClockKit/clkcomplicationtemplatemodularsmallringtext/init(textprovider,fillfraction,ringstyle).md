# init(textProvider:fillFraction:ringStyle:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a new template from the provided text, fill fraction, and ring style.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```swift
init(textProvider: CLKTextProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)
```

```objc
- (instancetype) initWithTextProvider:(CLKTextProvider *) textProvider fillFraction:(float) fillFraction ringStyle:(CLKComplicationRingStyle) ringStyle;
```

## Parameters

- `textProvider`: A text provider for the text in the center of the template. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `fillFraction`: A value between `0.0` and `1.0` that indicates how much of the ring fills.
- `ringStyle`: The ring’s style. For a complete list of styles, see [`CLKComplicationRingStyle`](../clkcomplicationringstyle.md).

## See Also

### Creating the Template
- [+ templateWithTextProvider:fillFraction:ringStyle:](./templatewithtextprovider_fillfraction_ringstyle_.md)
  Returns a new template from the provided text, fill fraction, and ring style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallringtext/init(textprovider:fillfraction:ringstyle:))*