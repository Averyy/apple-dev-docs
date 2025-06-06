# init(textProvider:fillFraction:ringStyle:)

**Framework**: ClockKit  
**Kind**: init

Creates a new template from the provided text, fill fraction, and ring style.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
init(textProvider: CLKTextProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)
```

## Parameters

- `textProvider`: A text provider for the text in the center of the template. For multicolor faces, like the Utility face, the system uses the text provider’s tint color for the text. For other faces, the system ignores the provided tint color, and uses a system color instead.
- `fillFraction`: A value between   and   that indicates how much of the ring fills.
- `ringStyle`: The ring’s style. For a complete list of styles, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargeringtext/init(textprovider:fillfraction:ringstyle:))*